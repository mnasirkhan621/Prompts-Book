# Word-level transcript for tighten.py: words.json = [{start,end,text,words:[{w,s,e}]}]
# usage (inside your audio folder): python <repo>/tools-and-workflows/hyperframes-edit-kit/transcribe.py voice.mp3 [script.txt]   (script = better spelling of names)
import json, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel
# decode with ffmpeg (installed PyAV is too new for faster-whisper's own decoder)
src = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'],
                                   capture_output=True, check=True).stdout, np.float32)
prompt = open(sys.argv[2], encoding='utf8').read()[:800] if len(sys.argv) > 2 else None
model = WhisperModel('small.en', device='cpu', compute_type='int8')
segs, _ = model.transcribe(src, word_timestamps=True, initial_prompt=prompt, vad_filter=False, beam_size=5)
out = []
for s in segs:
    ws = [{'w': w.word.strip(), 's': round(w.start, 3), 'e': round(w.end, 3)} for w in s.words if w.word.strip()]
    if ws: out.append({'start': ws[0]['s'], 'end': ws[-1]['e'], 'text': s.text.strip(), 'words': ws})
json.dump(out, open('words.json', 'w', encoding='utf8'), indent=1)
print(len(out), 'segments,', sum(len(s['words']) for s in out), 'words')
