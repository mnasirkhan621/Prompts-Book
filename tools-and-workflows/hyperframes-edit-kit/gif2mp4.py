# GIF / animated WebP -> 1280-wide-max H.264 mp4 (or alpha WebM) of a set length (Pillow decodes, ffmpeg encodes).
# GIFs loop by default; pass "once" to play through and hold the last frame (for one-off reactions whose restart looks unclean).
# usage: python tools-and-workflows/hyperframes-edit-kit/gif2mp4.py in.gif out.mp4 seconds [once]
import sys, subprocess, tempfile, pathlib
from PIL import Image
import json, os
_dj = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "youtube-studio", "brand", "design.json")
_bg = json.load(open(_dj, encoding="utf8")).get("background", "#111214") if os.path.exists(_dj) else "#111214"
BG = tuple(int(_bg.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) + (255,)   # transparent GIF parts get your background colour
src, out, secs = sys.argv[1], sys.argv[2], float(sys.argv[3])
im = Image.open(src); n = getattr(im, "n_frames", 1)
frames, durs = [], []
for i in range(n):
    im.seek(i); fr = im.convert("RGBA"); bg = Image.new("RGBA", fr.size, BG); bg.alpha_composite(fr)
    frames.append(fr if out.endswith(".webm") else bg.convert("RGB")); durs.append(max(20, im.info.get("duration", 100)) / 1000)
with tempfile.TemporaryDirectory() as d:
    lst, t, k = [], 0.0, 0
    once = len(sys.argv) > 4 and sys.argv[4] == "once"
    while t < secs:                      # once: play through, then the last frame holds; else loop the cycle
        i = min(k, n - 1) if once else k % n
        p = pathlib.Path(d) / f"f{k:05d}.png"; frames[i].save(p)
        dur = secs - t if once and k >= n - 1 else durs[i]
        lst.append(f"file '{p.as_posix()}'\nduration {dur}"); t += dur; k += 1
    lst.append(f"file '{p.as_posix()}'")
    (pathlib.Path(d) / "l.txt").write_text("\n".join(lst))
    alpha = out.endswith(".webm")      # transparent stickers keep their alpha (an mp4 shows a faint box on charcoal)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(pathlib.Path(d) / "l.txt"),
                    "-vf", f"scale='min(1280,iw*3)':-2:flags=lanczos,fps=30,format={'yuva420p' if alpha else 'yuv420p'}", "-t", str(secs)]
                   + (["-c:v", "libvpx-vp9", "-b:v", "3M", "-auto-alt-ref", "0"] if alpha else ["-c:v", "libx264", "-crf", "18"]) + [out], check=True)
print("ok", out, n, "frames")
