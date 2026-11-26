# Download YouTube thumbnails (biggest size available) for one video, many videos, a playlist or a channel.
# No API key needed (uses yt-dlp to list playlists/channels).
# usage:
#   python tools-and-workflows/youtube-research/thumbs.py <video url|id> [more...]
#   python tools-and-workflows/youtube-research/thumbs.py <playlist url>
#   python tools-and-workflows/youtube-research/thumbs.py <channel url, e.g. https://www.youtube.com/@name/videos> [--max 30]
# Saves youtube-studio/research/thumbnails/<video id>.jpg and an index.csv with title + link.
import csv, json, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'youtube-studio', 'research', 'thumbnails')
args = sys.argv[1:]
if not args: sys.exit('usage: python tools-and-workflows/youtube-research/thumbs.py <video|playlist|channel url> [more...] [--max 30]')
MAX = int(args[args.index('--max') + 1]) if '--max' in args else 30
links = [a for i, a in enumerate(args) if not a.startswith('--') and (i == 0 or args[i - 1] != '--max')]

def vid_id(s):
    m = re.search(r'(?:v=|youtu\.be/|shorts/|embed/|live/)([\w-]{11})', s)
    return m.group(1) if m else (s if re.fullmatch(r'[\w-]{11}', s) else None)

videos = []   # (id, title)
for link in links:
    if vid_id(link) and 'list=' not in link:
        videos.append((vid_id(link), '')); continue
    p = subprocess.run(['yt-dlp', '--flat-playlist', '-J', '--playlist-end', str(MAX), '--no-warnings', link],
                       capture_output=True, text=True, encoding='utf8')
    if p.returncode: print(f'FAILED {link}'); continue
    for e in json.loads(p.stdout).get('entries') or []:
        if e.get('id') and len(e['id']) == 11: videos.append((e['id'], e.get('title') or ''))

os.makedirs(OUT, exist_ok=True)
rows = []
for v, title in videos:
    dest = os.path.join(OUT, f'{v}.jpg')
    for size in ('maxresdefault', 'sddefault', 'hqdefault'):
        try:
            data = urllib.request.urlopen(f'https://i.ytimg.com/vi/{v}/{size}.jpg', timeout=20).read()
            if len(data) > 2000:   # YouTube serves a tiny grey placeholder when a size doesn't exist
                open(dest, 'wb').write(data); rows.append((v, title, f'https://youtu.be/{v}', size)); break
        except Exception:
            continue
    else:
        print(f'no thumbnail for {v}')
idx = os.path.join(OUT, 'index.csv')
new = not os.path.exists(idx)
with open(idx, 'a', newline='', encoding='utf8') as f:
    w = csv.writer(f)
    if new: w.writerow(['id', 'title', 'url', 'size'])
    w.writerows(rows)
print(f'{len(rows)} thumbnails saved in {OUT}')
