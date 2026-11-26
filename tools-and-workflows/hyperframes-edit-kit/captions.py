# Make captions from words.json (transcribe.py) or words_tight.json (tighten.py).
# Writes an .srt (works everywhere) and a styled .ass (your colours and font from youtube-studio/brand/design.json,
# key words in your accent colour). Import either into CapCut, Premiere, DaVinci, or burn the .ass in with ffmpeg:
#   ffmpeg -i video.mp4 -vf "ass=captions.ass" -c:a copy out.mp4
# usage: python tools-and-workflows/hyperframes-edit-kit/captions.py words_tight.json captions [--max 32] [--key 12.40 --key 30.05]
#   captions   -> output name (captions.srt + captions.ass)
#   --max N    -> max characters per line (default 32; ~32 for 9:16 reels, ~44 for 16:9)
#   --key T    -> start time (seconds) of a word to show in the accent colour; repeat for more words
#   --size WxH -> video size for the .ass (default 1920x1080; use 1080x1920 for reels)
import json, os, sys

args = sys.argv[1:]
if len(args) < 2: sys.exit(__doc__ or 'usage: python tools-and-workflows/hyperframes-edit-kit/captions.py words.json out_name [--max 32] [--key T ...] [--size WxH]')
words_f, out = args[0], args[1]
def opt(name, default):
    return args[args.index(name) + 1] if name in args else default
MAXC = int(opt('--max', 32))
W, H = map(int, opt('--size', '1920x1080').lower().split('x'))
KEYS = {f'{float(args[i + 1]):.2f}' for i, a in enumerate(args) if a == '--key'}

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
design_f = os.path.join(root, 'youtube-studio', 'brand', 'design.json')
d = json.load(open(design_f, encoding='utf8')) if os.path.exists(design_f) else {}
if not d: print('No youtube-studio/brand/design.json yet: using plain white captions. Run the design-system skill to set your own.')
text_c, accent_c = d.get('text', '#FFFFFF'), d.get('accent', '#FFFFFF')
font = d.get('font_body', 'Arial'); size = int(d.get('caption_size', 56))
pos_top = d.get('caption_position', 'bottom') == 'top'

ws = [w for s in json.load(open(words_f, encoding='utf8')) for w in s['words']]
groups, cur = [], []
for i, w in enumerate(ws):
    gap = w['s'] - cur[-1]['e'] if cur else 0
    if cur and (len(' '.join(x['w'] for x in cur + [w])) > MAXC or gap >= 0.35):
        groups.append(cur); cur = []
    cur.append(w)
    if w['w'][-1] in '.?!':
        groups.append(cur); cur = []
if cur: groups.append(cur)

def ts(t, sep):
    h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
    return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.', sep) if sep == ',' else f'{h}:{m:02d}:{s:05.2f}'
def ass_col(hexc):
    h = hexc.lstrip('#'); return f'&H00{h[4:6]}{h[2:4]}{h[0:2]}'.upper()

srt, ev = [], []
for gi, g in enumerate(groups):
    start = max(0.0, g[0]['s'] - 0.05)
    nxt = groups[gi + 1][0]['s'] - 0.05 if gi + 1 < len(groups) else g[-1]['e'] + 0.6
    end = min(nxt, g[-1]['e'] + 0.6)
    line = ' '.join(w['w'] for w in g)
    srt.append(f'{gi + 1}\n{ts(start, ",")} --> {ts(end, ",")}\n{line}\n')
    styled = ' '.join(('{\\c' + ass_col(accent_c) + '&}' + w['w'] + '{\\c' + ass_col(text_c) + '&}')
                      if f"{w['s']:.2f}" in KEYS else w['w'] for w in g)
    ev.append(f'Dialogue: 0,{ts(start, ".")},{ts(end, ".")},Cap,,0,0,0,,{styled}')

open(out + '.srt', 'w', encoding='utf8').write('\n'.join(srt))
margin = int(H * 0.3) if not pos_top else int(H * 0.12)   # keep clear of the progress bar
open(out + '.ass', 'w', encoding='utf8').write(f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{font},{size},{ass_col(text_c)},{ass_col(accent_c)},&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,{8 if pos_top else 2},60,60,{margin},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
''' + '\n'.join(ev) + '\n')
print(f'{len(groups)} caption lines -> {out}.srt + {out}.ass')
