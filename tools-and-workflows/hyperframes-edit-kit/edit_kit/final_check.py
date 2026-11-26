# Final check on a rendered video: transcribes the render's own audio and compares it with the voice words,
# so no sound effect hid a word. Also prints the loudness.
# usage: python tools-and-workflows/hyperframes-edit-kit/edit_kit/final_check.py <video folder> <render.mp4>
import difflib, json, pathlib, re, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

V = pathlib.Path(sys.argv[1]).resolve(); mp4 = sys.argv[2]
wf = V / "audio" / ("words_tight.json" if (V / "audio" / "words_tight.json").exists() else "words.json")
norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
want = [norm(w["w"]) for s in json.loads(wf.read_text(encoding="utf8")) for w in s["words"]]
pcm = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                                   capture_output=True, check=True).stdout, np.float32)
segs, _ = WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(pcm, word_timestamps=True, beam_size=5)
got, at = [], []
for s in segs:
    for w in s.words: got.append(norm(w.word)); at.append(w.start)
sm = difflib.SequenceMatcher(None, want, got, autojunk=False)
lost = []
for op, a, b, c, d in sm.get_opcodes():
    if op in ("delete", "replace"): lost.append((" ".join(want[a:b]), at[min(c, len(at) - 1)] if at else 0))
print(f"words in the voice: {len(want)}, heard in the render: {len(got)}, match {sm.ratio() * 100:.1f}%")
for txt, t in lost[:40]: print(f"  {int(t // 60)}:{t % 60:05.2f}  missing or changed: {txt}")
if not lost: print("  every word is clear")
loud = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
m = re.findall(r"I:\s+(-?[\d.]+) LUFS", loud); pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", loud)
if m: print(f"loudness {m[-1]} LUFS (YouTube target about -14), true peak {pk[-1] if pk else '?'} dBFS")
print("Whisper mishears some words on its own: check each listed spot by ear before changing the edit.")
