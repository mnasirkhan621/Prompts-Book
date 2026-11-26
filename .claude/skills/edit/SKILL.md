---
name: edit
description: Edit a long YouTube video (or a reel) in code from the creator's voiceover - word screens, website and app screens with markers, b-roll, GIFs and memes, versus cards, bars, gauges, flows, node diagrams, maps, re-created chats and terminals - in their own design system, rendered with HyperFrames. Use when the creator says "edit this video", "make the edit", "build the video", or drops a voiceover and assets for a new video.
---

# Edit a Video in Code (HyperFrames)

Engine: [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML -> MP4, run with `npx hyperframes`). The kit in `tools-and-workflows/hyperframes-edit-kit/edit_kit/` compiles `shots.py` into HyperFrames GSAP timelines cleanly. Verify `npx hyperframes` is installed by the user (if missing, direct them to the HyperFrames repo setup).

## Before Anything
1. **Design system check.** If `youtube-studio/brand/design.json` doesn't exist, first check if another brand file exists in the workspace (see `design-system` skill). If found, import it and proceed. If none exists, suggest building one first (~10 minutes) or proceed using the kit's clean neutral default (`#F6F6F4` off-white, `#141414` ink, `#2563EB` accent).
   Check `youtube-studio/sfx/` has a file for each sound the shots use (`click`, `whoosh`, `pop`, `ding`, `typing`, etc.); warn if any are missing before building.
2. Read the script and ask what's unclear (which screen a line means, which file, exact text). Never guess: ask with options.
3. Gather assets with the creator: screen recordings/screenshots of the real thing they talk about, original or AI-generated b-roll, GIFs, logos. Only use media they have rights to.

## Steps
1. Scaffold project: `python tools-and-workflows/hyperframes-edit-kit/edit_kit/new_video.py youtube-studio/videos/<name>` -> place voiceover at `audio/voice.mp3` and visual assets inside `assets/`.
2. Word timings:
   `cd youtube-studio/videos/<name>/audio && python ../../../../tools-and-workflows/hyperframes-edit-kit/transcribe.py voice.mp3 ../script.txt && python ../../../../tools-and-workflows/hyperframes-edit-kit/tighten.py`
   (Cuts silences > 0.30s down to 0.22s, preserves intentional `<break time="..."/>` cadence beats, normalizes to `-14 LUFS`, writes `words_tight.json` & `voice_tight.wav`).
3. Author `youtube-studio/videos/<name>/shots.py`: one shot dict per visual change, using shot kinds from `tools-and-workflows/hyperframes-edit-kit/edit_kit/KINDS.md`.
4. Compile timeline: `python tools-and-workflows/hyperframes-edit-kit/edit_kit/build.py youtube-studio/videos/<name>` -> inspect and fix any warnings.
5. **Beat plan storyboard first:** `python tools-and-workflows/hyperframes-edit-kit/edit_kit/storyboard.py youtube-studio/videos/<name>` and present `storyboard/storyboard.jpg` (one still per shot with its trigger phrase). Wait for creator approval before rendering.
6. Render: `cd youtube-studio/videos/<name>/project && npx hyperframes check && npx hyperframes render . -o ../renders/<name>_v01.mp4`. Never overwrite an existing render: increment `_v02`, `_v03`.
7. **Self-check the render:** extract review frames (~1 fps contact sheet with ffmpeg) to inspect visually, then run `python tools-and-workflows/hyperframes-edit-kit/edit_kit/final_check.py youtube-studio/videos/<name> youtube-studio/videos/<name>/renders/<name>_v01.mp4` (re-transcribes rendered audio to ensure no SFX masked spoken words, and reports LUFS loudness + true peak). Fix issues, re-render if needed, then summarize changes.

## Default Editing Rules (Overridable in `youtube-studio/brand/design.md`)
**Pace and Structure**
- Visual change every 2-3 s. Avoid dead screen time; cap holds at `max_hold` (~4.5 s) unless an active screen recording needs longer.
- Reveals sync directly to the voice word onset (`build.py` snaps animations automatically).
- Visuals are literal and factual: real numbers, real UI screens, real names.
- On-screen text uses the creator's exact script words, never a paraphrase. Full big-word screens are punctuation (max 3-4 per video).
- Hook delivers immediate stakes in the first seconds with zero generic intro card.

**Screens, B-Roll & GIFs**
- Show whole application windows, not tiny unreadable crops. One clean zoom/focus move per shot, never dizzying drift.
- Full-screen b-roll (`kind="full"`) plays clean with **no text overlays, stamps, or captions on top** (give spoken phrases their own text shot).
- Do not stretch short GIFs (`kind="gif"`) past their runtime; chain or pair appropriately.

**Explainers & Sound**
- Never use the same chart kind twice consecutively. Bars/gauges use verified data only.
- Sound cues fire strictly where a visual changes, under the voice, never stacked (minimum 0.35 s gap enforced automatically).
- Zero tacky preset transitions (spin/glitch/star-wipes) or simultaneous colliding entrances.

## After Creator Feedback
Append every locked revision note as a dated rule inside `youtube-studio/brand/design.md`, then rebuild only affected sections (supports `ONLY=<section>` in `build.py`).
