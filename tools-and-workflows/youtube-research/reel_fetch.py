# Download Instagram/TikTok reels for study: video, audio, 1 fps frames + contact sheet, meta.json (likes, comments, views if public).
# usage: python tools-and-workflows/youtube-research/reel_fetch.py <link> [more links...]   -> youtube-studio/research/reels/<id>/
# YouTube links: use `python tools-and-workflows/youtube-research/yt.py watch <url>` instead (captions + frames in youtube-studio/research/<id>/).
import json, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent.parent / 'youtube-studio' / 'research' / 'reels'
for link in sys.argv[1:]:
    link = link.split('?')[0]
    p = subprocess.run(['yt-dlp', '-J', '--no-warnings', link], capture_output=True, text=True, encoding='utf8')
    if p.returncode:
        print(f'FAILED {link}: {p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "no output"}')
        continue
    info = json.loads(p.stdout)
    out = root / info['id']
    (out / 'frames').mkdir(parents=True, exist_ok=True)
    meta = {k: info.get(k) for k in ('id', 'uploader', 'channel', 'upload_date', 'duration', 'view_count',
                                     'like_count', 'comment_count', 'description')}
    meta['url'] = link
    (out / 'meta.json').write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding='utf8')
    video = out / 'video.mp4'
    if not video.exists():
        subprocess.run(['yt-dlp', '-q', '--no-warnings', '-f', 'mp4/best', '-o', str(video), link], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(video), '-vn', str(out / 'audio.mp3')], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(video), '-vf', 'fps=1,scale=360:-2',
                    str(out / 'frames' / '%03d.jpg')], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(video), '-vf', 'fps=1,scale=180:-2,tile=6x5',
                    '-frames:v', '1', str(out / 'contact.jpg')], check=True)
    print(f'OK {info["id"]} -> {out}  likes={meta["like_count"]} comments={meta["comment_count"]} views={meta["view_count"]}')
