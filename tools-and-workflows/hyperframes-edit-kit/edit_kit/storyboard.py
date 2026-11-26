# Beat plan storyboard: one still per shot (taken just after the shot's animation lands) on one contact sheet,
# each labelled with its number, kind and the words it starts on. Show it to the creator and wait for "go" before rendering.
# usage: python tools-and-workflows/hyperframes-edit-kit/edit_kit/storyboard.py <video folder>      (run build.py first)
# writes <video>/storyboard/storyboard.jpg (+ the single frames)
import json, pathlib, shutil, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

V = pathlib.Path(sys.argv[1]).resolve(); P = V / "project"; out = V / "storyboard"
shots = json.loads((V / "shot_times.json").read_text(encoding="utf8"))
ats = [round(min(s["t"] + 1.0, (s["t"] + s["e"]) / 2), 2) for s in shots]
if out.exists(): shutil.rmtree(out)
out.mkdir()
npx = shutil.which("npx") or "npx"
subprocess.run([npx, "--yes", "hyperframes@0.8.226", "snapshot", str(P), "--at", ",".join(map(str, ats)), "--no-end", "-o", str(out / "frames")], check=True)
frames = sorted((out / "frames").glob("*.png"))
if len(frames) != len(shots): print(f"! got {len(frames)} frames for {len(shots)} shots")
TW, TH, cols = 480, 270, 4
rows = (len(frames) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (TW + 16) + 16, rows * (TH + 70) + 16), (24, 24, 24))
try: font = ImageFont.truetype("arial.ttf", 18)
except OSError: font = ImageFont.load_default()
dr = ImageDraw.Draw(sheet)
for q, (f, s) in enumerate(zip(frames, shots)):
    x, y = 16 + (q % cols) * (TW + 16), 16 + (q // cols) * (TH + 70)
    sheet.paste(Image.open(f).convert("RGB").resize((TW, TH)), (x, y))
    dr.text((x, y + TH + 6), f"{s['k']}  {s['kind']}  {s['t']:.1f}s", fill=(255, 210, 0), font=font)
    dr.text((x, y + TH + 30), ("\"" + s["at"] + "\"")[:52], fill=(220, 220, 220), font=font)
sheet.save(out / "storyboard.jpg", quality=88)
print(f"storyboard: {out / 'storyboard.jpg'} ({len(frames)} shots)")
