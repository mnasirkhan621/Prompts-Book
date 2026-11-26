# Start a new video: python tools-and-workflows/hyperframes-edit-kit/edit_kit/new_video.py youtube-studio/videos/my_video
# Makes audio/ (put voice.mp3 here), assets/ (your screenshots, recordings, b-roll, GIFs, logos), renders/ and a starter shots.py.
import pathlib, shutil, sys
KIT = pathlib.Path(__file__).resolve().parent
V = pathlib.Path(sys.argv[1])
for d in ("audio", "assets/screens", "assets/broll", "assets/gifs", "assets/logos", "renders"): (V / d).mkdir(parents=True, exist_ok=True)
if not (V / "shots.py").exists(): shutil.copy(KIT / "shots_template.py", V / "shots.py")
print(f"""ready: {V}
next:
  1. put your voiceover in {V / 'audio' / 'voice.mp3'}
  2. cd {V / 'audio'} && python <repo>/tools-and-workflows/hyperframes-edit-kit/transcribe.py voice.mp3 && python <repo>/tools-and-workflows/hyperframes-edit-kit/tighten.py
  3. fill {V / 'shots.py'} (kinds: tools-and-workflows/hyperframes-edit-kit/edit_kit/KINDS.md)
  4. python tools-and-workflows/hyperframes-edit-kit/edit_kit/build.py {V}  then  python tools-and-workflows/hyperframes-edit-kit/edit_kit/storyboard.py {V}""")
