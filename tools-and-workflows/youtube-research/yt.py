# YouTube research tool. YouTube Data API v3 for numbers, yt-dlp for captions/video, ffmpeg for frames, faster-whisper as transcript fallback.
# Key: tools-and-workflows/youtube-research/.env -> YOUTUBE_API_KEY=...  (only video/channel/comments/search need it; transcript/watch work without)
# Usage (run from anywhere):
#   python tools-and-workflows/youtube-research/yt.py video <url|id> [more...]            stats for videos
#   python tools-and-workflows/youtube-research/yt.py channel <@handle|url|id> [--days 60] [--max 200] [--shorts|--long]   uploads + outlier score (views / channel median)
#   python tools-and-workflows/youtube-research/yt.py comments <url|id> [--max 40] [--order relevance|time]
#   python tools-and-workflows/youtube-research/yt.py search "<query>" [--days 30] [--max 25]   recent videos for a query, with views/subs ratio
#   python tools-and-workflows/youtube-research/yt.py transcript <url|id> [--lang en]       captions as timestamped text (whisper fallback)
#   python tools-and-workflows/youtube-research/yt.py watch <url|id> [--every 2] [--lang en]  download <=480p, frames every N s + contact sheets + transcript
# Add --json to video/channel/comments/search for raw JSON. Output files land in youtube-studio/research/<id>/.
import json, os, re, statistics, subprocess, sys, glob
os.environ.setdefault('HF_HUB_DISABLE_SYMLINKS_WARNING', '1')
from datetime import datetime, timedelta, timezone

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(TOOL_DIR))
REFS = os.path.join(ROOT, 'youtube-studio', 'research')

def key():
    k = os.environ.get('YOUTUBE_API_KEY')
    for env in (os.path.join(TOOL_DIR, '.env'), os.path.join(ROOT, '.env')):
        if not k and os.path.exists(env):
            for line in open(env, encoding='utf-8'):
                if line.strip().startswith('YOUTUBE_API_KEY='): k = line.split('=', 1)[1].strip().strip('"\'')
    if not k: sys.exit('No YOUTUBE_API_KEY. Paste it into tools-and-workflows/youtube-research/.env as: YOUTUBE_API_KEY=your_key  (see tools-and-workflows/youtube-research/YT_API_KEY_SETUP.md)')
    return k

def api():
    from googleapiclient.discovery import build
    return build('youtube', 'v3', developerKey=key(), cache_discovery=False)

def vid_id(s):
    m = re.search(r'(?:v=|youtu\.be/|shorts/|embed/|live/)([\w-]{11})', s)
    return m.group(1) if m else s.strip()

def dur_s(iso):
    m = re.match(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', iso or '')
    d, h, mi, s = (int(x or 0) for x in m.groups()) if m else (0, 0, 0, 0)
    return d * 86400 + h * 3600 + mi * 60 + s

def fmt_dur(s): return f'{s // 60}:{s % 60:02d}'

def videos_info(yt, ids):
    out = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part='snippet,statistics,contentDetails', id=','.join(ids[i:i + 50])).execute()
        for v in r.get('items', []):
            st, sn = v.get('statistics', {}), v['snippet']
            out.append({'id': v['id'], 'title': sn['title'], 'channel': sn['channelTitle'], 'channelId': sn['channelId'],
                        'published': sn['publishedAt'], 'duration': dur_s(v['contentDetails'].get('duration')),
                        'views': int(st.get('viewCount', 0)), 'likes': int(st.get('likeCount', 0)), 'comments': int(st.get('commentCount', 0)),
                        'tags': sn.get('tags', []), 'description': sn.get('description', ''), 'url': f"https://youtu.be/{v['id']}"})
    return out

def resolve_channel(yt, s):
    s = s.strip()
    m = re.search(r'(UC[\w-]{22})', s)
    if m: r = yt.channels().list(part='snippet,statistics,contentDetails', id=m.group(1)).execute()
    else:
        h = re.search(r'@([\w.-]+)', s)
        r = yt.channels().list(part='snippet,statistics,contentDetails', forHandle='@' + (h.group(1) if h else s.lstrip('@'))).execute()
    if not r.get('items'): sys.exit(f'Channel not found: {s}')
    return r['items'][0]

def opt(args, name, default=None, cast=str):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return cast(v)
    return default

def flag(args, name):
    if name in args: args.remove(name); return True
    return False

def cmd_video(args):
    j = flag(args, '--json'); vs = videos_info(api(), [vid_id(a) for a in args])
    if j: return print(json.dumps(vs, indent=1, ensure_ascii=False))
    for v in vs:
        print(f"{v['title']}\n  {v['channel']} · {v['published'][:10]} · {fmt_dur(v['duration'])} · {v['views']:,} views · {v['likes']:,} likes · {v['comments']:,} comments · {v['url']}")

def cmd_channel(args):
    j = flag(args, '--json'); shorts = flag(args, '--shorts'); long_ = flag(args, '--long')
    days = opt(args, '--days', 60, int); mx = opt(args, '--max', 200, int)
    yt = api(); ch = resolve_channel(yt, args[0]); st = ch['statistics']
    uploads = ch['contentDetails']['relatedPlaylists']['uploads']
    since = datetime.now(timezone.utc) - timedelta(days=days); ids, tok = [], None
    while len(ids) < mx:
        r = yt.playlistItems().list(part='contentDetails', playlistId=uploads, maxResults=50, pageToken=tok).execute()
        stop = False
        for it in r['items']:
            if datetime.fromisoformat(it['contentDetails']['videoPublishedAt'].replace('Z', '+00:00')) < since: stop = True; break
            ids.append(it['contentDetails']['videoId'])
        tok = r.get('nextPageToken')
        if stop or not tok: break
    vs = videos_info(yt, ids[:mx])
    if shorts: vs = [v for v in vs if v['duration'] <= 180]
    if long_: vs = [v for v in vs if v['duration'] > 180]
    med = statistics.median([v['views'] for v in vs]) if vs else 0
    for v in vs: v['outlier'] = round(v['views'] / med, 2) if med else None
    info = {'channel': ch['snippet']['title'], 'id': ch['id'], 'subs': int(st.get('subscriberCount', 0)), 'views': int(st.get('viewCount', 0)),
            'videos': int(st.get('videoCount', 0)), 'window_days': days, 'median_views_in_window': med, 'uploads': vs}
    if j: return print(json.dumps(info, indent=1, ensure_ascii=False))
    print(f"{info['channel']} ({info['id']}) · {info['subs']:,} subs · {info['videos']} videos · median {med:,.0f} views over last {days} days ({len(vs)} uploads)")
    for v in sorted(vs, key=lambda v: v['published'], reverse=True):
        print(f"  {v['published'][:10]}  {v['outlier']:>6}x  {v['views']:>10,}  {fmt_dur(v['duration']):>6}  {v['title'][:70]}  {v['url']}")

def cmd_comments(args):
    j = flag(args, '--json'); mx = opt(args, '--max', 40, int); order = opt(args, '--order', 'relevance')
    r = api().commentThreads().list(part='snippet,replies', videoId=vid_id(args[0]), maxResults=min(mx, 100), order=order, textFormat='plainText').execute()
    cs = [{'author': t['snippet']['topLevelComment']['snippet']['authorDisplayName'], 'likes': t['snippet']['topLevelComment']['snippet']['likeCount'],
           'text': t['snippet']['topLevelComment']['snippet']['textDisplay'], 'replies': t['snippet']['totalReplyCount']} for t in r.get('items', [])]
    if j: return print(json.dumps(cs, indent=1, ensure_ascii=False))
    for c in cs: print(f"[{c['likes']} likes · {c['replies']} replies] {c['text'][:400]}")

def cmd_search(args):
    j = flag(args, '--json'); days = opt(args, '--days', 30, int); mx = opt(args, '--max', 25, int)
    yt = api(); after = (datetime.now(timezone.utc) - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')
    r = yt.search().list(part='id', q=args[0], type='video', order='viewCount', publishedAfter=after, maxResults=min(mx, 50)).execute()
    vs = videos_info(yt, [i['id']['videoId'] for i in r.get('items', [])])
    chs = {}
    cids = list({v['channelId'] for v in vs})
    for i in range(0, len(cids), 50):
        for c in yt.channels().list(part='statistics', id=','.join(cids[i:i + 50])).execute().get('items', []):
            chs[c['id']] = int(c['statistics'].get('subscriberCount', 0) or 0)
    for v in vs: v['subs'] = chs.get(v['channelId'], 0); v['views_per_sub'] = round(v['views'] / v['subs'], 2) if v['subs'] else None
    vs.sort(key=lambda v: v['views_per_sub'] or 0, reverse=True)
    if j: return print(json.dumps(vs, indent=1, ensure_ascii=False))
    for v in vs:
        print(f"  {v['views_per_sub']:>6}x subs  {v['views']:>10,} views  {v['subs']:>9,} subs  {v['published'][:10]}  {v['channel'][:20]:20}  {v['title'][:60]}  {v['url']}")

def ytdlp(*a): return subprocess.run([sys.executable, '-m', 'yt_dlp', '--no-warnings', '--js-runtimes', 'node', *a], capture_output=True, text=True, encoding='utf-8', errors='replace')

def ts(t): t = int(t); return f'{t // 60}:{t % 60:02d}'

def parse_vtt(path, chunk=10):
    lines, seen, cur_t = [], set(), 0.0
    for block in open(path, encoding='utf-8').read().split('\n\n'):
        m = re.search(r'(\d+):(\d+):([\d.]+) -->', block)
        if not m: continue
        t = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
        for raw in block.split('\n')[1:]:
            txt = re.sub(r'<[^>]+>', '', raw).strip()
            if not txt or '-->' in txt or txt in seen: continue
            seen.add(txt); lines.append((t, txt))
    out, buf, start = [], [], 0
    for t, txt in lines:
        if not buf: start = t
        buf.append(txt)
        if t - start >= chunk: out.append(f'[{ts(start)}] ' + ' '.join(buf)); buf = []
    if buf: out.append(f'[{ts(start)}] ' + ' '.join(buf))
    return '\n'.join(out)

def transcript(v, lang='en'):
    d = os.path.join(REFS, v); os.makedirs(d, exist_ok=True)
    out = os.path.join(d, f'transcript_{lang}.txt')
    if os.path.exists(out): return open(out, encoding='utf-8').read()
    ytdlp('--skip-download', '--write-subs', '--write-auto-subs', '--sub-langs', f'{lang}-orig,{lang}', '--sub-format', 'vtt',
          '-o', os.path.join(d, 'subs.%(ext)s'), f'https://www.youtube.com/watch?v={v}')
    vtts = sorted(glob.glob(os.path.join(d, 'subs*.vtt')), key=lambda p: ('orig' not in p, len(p)))
    if vtts: text = parse_vtt(vtts[0])
    else:
        print('No captions; transcribing audio with faster-whisper (slower)...', file=sys.stderr)
        ytdlp('-f', 'bestaudio', '-x', '--audio-format', 'mp3', '-o', os.path.join(d, 'audio.%(ext)s'), f'https://www.youtube.com/watch?v={v}')
        from faster_whisper import WhisperModel
        import numpy as np   # decode with ffmpeg: newer PyAV breaks faster-whisper's own decoder
        pcm = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(d, 'audio.mp3'), '-ac', '1', '-ar', '16000',
                                            '-f', 'f32le', '-'], capture_output=True, check=True).stdout, np.float32)
        segs, _ = WhisperModel('small', device='cpu', compute_type='int8').transcribe(pcm, language=lang)
        text = '\n'.join(f'[{ts(s.start)}] {s.text.strip()}' for s in segs)
    open(out, 'w', encoding='utf-8').write(text)
    return text

def cmd_transcript(args):
    lang = opt(args, '--lang', 'en'); print(transcript(vid_id(args[0]), lang))

def cmd_watch(args):
    every = opt(args, '--every', 2, float); lang = opt(args, '--lang', 'en'); v = vid_id(args[0])
    d = os.path.join(REFS, v); fr = os.path.join(d, 'frames'); sh = os.path.join(d, 'sheets')
    os.makedirs(fr, exist_ok=True); os.makedirs(sh, exist_ok=True)
    mp4 = os.path.join(d, 'video.mp4')
    if not os.path.exists(mp4):
        r = ytdlp('-f', 'bv*[height<=480]+ba/b[height<=480]/b', '--merge-output-format', 'mp4', '-o', mp4, f'https://www.youtube.com/watch?v={v}')
        if not os.path.exists(mp4): sys.exit('Download failed:\n' + r.stderr[-800:])
    for f in glob.glob(os.path.join(fr, '*.jpg')) + glob.glob(os.path.join(sh, '*.jpg')): os.remove(f)
    subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-vf', f'fps=1/{every},scale=480:-2', '-q:v', '4', os.path.join(fr, '%04d.jpg')], check=True)
    # contact sheets: 4x3 frames each, so one image = 12 frames
    subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-vf', f'fps=1/{every},scale=320:-2,tile=4x3:padding=4:margin=4', '-q:v', '4', os.path.join(sh, 'sheet_%03d.jpg')], check=True)
    n = len(glob.glob(os.path.join(fr, '*.jpg'))); sheets = sorted(glob.glob(os.path.join(sh, '*.jpg')))
    per = 12 * every
    print(f'Video: {mp4}\nFrames: {n} (every {every}s) in {fr}  -> frame k is at (k-1)*{every}s')
    print(f'Contact sheets: {len(sheets)} in {sh} (left-to-right, top-to-bottom, 12 frames each):')
    for i, p in enumerate(sheets): print(f'  {os.path.basename(p)}  {ts(i * per)}-{ts((i + 1) * per)}')
    try: t = transcript(v, lang); print(f'Transcript: {os.path.join(d, "transcript_" + lang + ".txt")} ({len(t.split())} words)')
    except Exception as e: print(f'Transcript failed: {e}')

CMDS = {'video': cmd_video, 'channel': cmd_channel, 'comments': cmd_comments, 'search': cmd_search, 'transcript': cmd_transcript, 'watch': cmd_watch}
if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3 or sys.argv[1] not in CMDS: sys.exit(open(__file__, encoding='utf-8').read().split('\nimport')[0])
    CMDS[sys.argv[1]](sys.argv[2:])
