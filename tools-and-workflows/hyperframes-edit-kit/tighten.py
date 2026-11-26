# Run inside the folder that holds voice.mp3 + words.json (from transcribe.py).
# Shrink pauses > MAXGAP to KEEP seconds; insert extra hold after given word times. Writes voice_tight.wav + words_tight.json + cuts.json
# Cadence (2026-10-31): each <break time="x"s/> in voiceover_cadence.txt keeps its pause at x seconds; no file = old behaviour.
import difflib, json, os, re, subprocess, sys
src, words_in = 'voice.mp3', 'words.json'
MAXGAP, KEEP = 0.30, 0.22
HOLDS = {}   # optional: {word_time_seconds: extra_hold_seconds}
def norm(w): return re.sub(r"[^a-z0-9']", '', w.lower())
def cadence_beats(path='voiceover_cadence.txt'):
    if not os.path.exists(path): return []
    said = [w for s in json.load(open(words_in, encoding='utf8')) for w in s['words']]
    script, marks = [], []
    for i, chunk in enumerate(re.split(r'<break time="([\d.]+)s"\s*/>', open(path, encoding='utf8').read())):
        if i % 2: marks.append((len(script) - 1, float(chunk)))
        else: script += [n for n in map(norm, chunk.split()) if n]
    blocks = difflib.SequenceMatcher(None, script, [norm(w['w']) for w in said], autojunk=False).get_matching_blocks()
    beats = []
    for at, amt in marks:
        hit = [b for b in blocks if b.size and b.a <= at]
        if hit: beats.append((said[hit[-1].b + min(at - hit[-1].a, hit[-1].size - 1)]['e'], amt))
    print('%d cadence beats (%d in script)' % (len(beats), len(marks)))
    return beats
BEATS = cadence_beats()
log = subprocess.run(['ffmpeg','-hide_banner','-i',src,'-af','silencedetect=n=-34dB:d=%s'%MAXGAP,'-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',log)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',log)]
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
# keep segments: speech + KEEP/2 padding each side of a gap
segs=[]; cur=0.0
for s,e in zip(st,en):
    if s<0.05: cur=max(0,e-0.05); continue
    if e>=dur-0.01: segs.append((cur,min(dur,s+0.25))); cur=None; break
    keep=next((min(amt,e-s) for t,amt in BEATS if s-0.3<=t<=e),KEEP)
    segs.append((cur,s+keep/2)); cur=e-keep/2
if cur is not None: segs.append((cur,dur))
# build with holds: insert silence after the segment that contains/precedes each hold time
pieces=[];t=0;mp=[]
for a,b in segs:
    mp.append((a,b,t)); pieces.append(('a',a,b)); t+=b-a
    for h,amt in HOLDS.items():
        if a < h <= b+0.3 and not any(p[0]=='s' and p[3]==h for p in pieces):
            pieces.append(('s',amt,0,h)); t+=amt
def remap(x):
    for a,b,n in mp:
        if a-0.15<=x<=b+0.15: return round(n+min(max(x-a,0),b-a),3)
    best=min(mp,key=lambda m:min(abs(x-m[0]),abs(x-m[1]))); return round(best[2] if x<best[0] else best[2]+best[1]-best[0],3)
# ffmpeg concat via filter
f=[];labels=[]
for i,p in enumerate(pieces):
    if p[0]=='a': f.append(f"[0:a]atrim={p[1]:.3f}:{p[2]:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={p[2]-p[1]-0.012:.3f}:d=0.012[p{i}]")
    else: f.append(f"anullsrc=r=44100:cl=stereo,atrim=0:{p[1]}[p{i}]")
    labels.append(f"[p{i}]")
f.append(''.join(labels)+f"concat=n={len(pieces)}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[o]")
open('tighten_filter.txt','w').write(';\n'.join(f))
subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-/filter_complex','tighten_filter.txt','-map','[o]','-ar','48000','voice_tight.wav'],check=True)
d=json.load(open(words_in,encoding='utf8'))
for s in d:
    for w in s['words']: w['s']=remap(w['s']); w['e']=remap(w['e'])
    s['start']=s['words'][0]['s']; s['end']=s['words'][-1]['e']
json.dump(d,open('words_tight.json','w',encoding='utf8'),indent=1)
json.dump({'segments_kept':segs,'holds':HOLDS,'map':mp},open('cuts.json','w'),indent=1)
print('orig %.1fs -> new %.1fs, %d pauses shortened'%(dur,t,len(segs)-1))
