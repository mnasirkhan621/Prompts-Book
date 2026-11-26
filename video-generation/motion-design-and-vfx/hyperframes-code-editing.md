# HyperFrames Code-to-Video Production Engine
**Architect & Lead Developer:** **Muhammad Nasir Khan**  
**Repository:** Prompts Book | Programmatic Motion Design & Editing

---

## 1. Overview: Editing YouTube Videos in Code

Traditional timeline editors require painstaking manual keyframing for every kinetic headline, metric bar, terminal simulation, diagram reveal, and sound effect. By integrating **Code-to-Video Editing** via **[HyperFrames](https://github.com/heygen-com/hyperframes)** (`tools-and-workflows/hyperframes-edit-kit/`), you generate visual AI clips with **Prompts Book**, record a voiceover, and compile a synchronized GSAP + HTML5 $\rightarrow$ MP4 production edit deterministically in code.

```text
Voiceover (voice.mp3) ─▶ transcribe.py (Whisper word timestamps) ─▶ tighten.py (-14 LUFS)
                                                                            │
Brand System (design.json) + AI B-Roll + shots.py ──▶ build.py ─────────────┤
                                                        │                   │
                                                        ▼                   ▼
   final_check.py ◀── npx hyperframes render ◀── storyboard.py (Beat Approval)
```

---

## 2. End-to-End 7-Step Production Pipeline (`edit` skill)

### Step 1: Scaffold the Project
```bash
python tools-and-workflows/hyperframes-edit-kit/edit_kit/new_video.py youtube-studio/videos/my_video
```
Creates `audio/`, `assets/{screens,broll,gifs,logos}/`, `renders/`, and starter `shots.py`.

### Step 2: Word-Timestamp Extraction & Pacing Tightening
```bash
cd youtube-studio/videos/my_video/audio
python ../../../../tools-and-workflows/hyperframes-edit-kit/transcribe.py voice.mp3 ../script.txt
python ../../../../tools-and-workflows/hyperframes-edit-kit/tighten.py
```
* **`transcribe.py`**: Runs `faster-whisper` (`small.en`) via FFmpeg PCM decoding to capture word-level timestamps (`words.json`). Pass your script file so proper nouns and technical terms spell accurately.
* **`tighten.py`**: Automatically trims dead pauses longer than `0.30s` down to `0.22s`, respects intentional `<break time="x"s/>` tags inside `voiceover_cadence.txt`, normalizes vocal loudness via FFmpeg EBU R128 (`-14 LUFS`, `-1.5 dBFS` true peak), and outputs `voice_tight.wav` + `words_tight.json`.

### Step 3: Optional Burned / External Captions
```bash
python tools-and-workflows/hyperframes-edit-kit/captions.py words_tight.json captions --max 32
```
Generates both `.srt` and styled `.ass` subtitles mapped directly to `youtube-studio/brand/design.json` colors and fonts, automatically lifting bottom margins clear of platform progress bars. Pass `--key <seconds>` to color-highlight specific anchor words.

### Step 4: Author `shots.py` with Word-Synced Triggers
Each entry in `SHOTS` targets an exact spoken phrase (`at="..."`) from `words_tight.json`. Inside a shot, parameters ending in `_at` or tuple cue words trigger GSAP animations on the exact millisecond that word is spoken.

*See the full API reference in [`KINDS.md`](../../tools-and-workflows/hyperframes-edit-kit/edit_kit/KINDS.md).*

### Step 5: Compile & Approve Storyboard Before Rendering
```bash
python tools-and-workflows/hyperframes-edit-kit/edit_kit/build.py youtube-studio/videos/my_video
python tools-and-workflows/hyperframes-edit-kit/edit_kit/storyboard.py youtube-studio/videos/my_video
```
* **`build.py`**: Re-themes all compositions via [`theme.py`](../../tools-and-workflows/hyperframes-edit-kit/edit_kit/theme.py) against `youtube-studio/brand/design.json`, validates GIF durations, strips forbidden overlays off `full` B-roll, enforces a minimum `0.35s` gap between audio SFX triggers, and writes modular HyperFrames HTML compositions + `shot_times.json`.
* **`storyboard.py`**: Captures one PNG snapshot right as each shot's entrance completes and stitches a numbered grid contact sheet (`storyboard/storyboard.jpg`) so directors can verify every cut before spending compute rendering.

### Step 6: Render Composition
```bash
cd youtube-studio/videos/my_video/project
npx hyperframes check
npx hyperframes render . -o ../renders/my_video_v01.mp4
```
Use environment variable `ONLY=<section_name>` with `build.py` during rapid iteration to re-compile and preview a single chapter instead of the entire video.

### Step 7: Automated Audio/Word Final Verification
```bash
python tools-and-workflows/hyperframes-edit-kit/edit_kit/final_check.py youtube-studio/videos/my_video youtube-studio/videos/my_video/renders/my_video_v01.mp4
```
Re-transcribes the **rendered final MP4 audio** and diffs spoken words against `words_tight.json` to catch any sound effect masking dialogue, printing integrated loudness (`LUFS`) and true peak (`dBFS`).

---

## 3. Supported Programmatic Shot Kinds (`KINDS.md`)

| Category | Shot Kind | Functional Behavior |
| :--- | :--- | :--- |
| **Typography** | `words`, `chips`, `strike2`, `chapter` | Word-by-word animated reveals, color-coded pills, strikethrough-to-replacement transitions, chapter bumpers. |
| **Data & Proof** | `pick2`, `bars2`, `gauge`, `meter`, `tries` | Animated versus cards, data-proportional dual bar races, swinging dial needles, token depletion meters, multi-test check sequences. |
| **Diagrams** | `flow`, `nodes`, `hub`, `card` | Icon pipelines connected dynamically, center-and-satellite node graphs, blurred roadmap hubs that unblur per chapter. |
| **Footage** | `screen`, `full`, `split`, `gif`, `film`, `rec` | Framed browser/app recordings with callout boxes (`mark`), clean full-bleed AI B-roll, side-by-side splits, converted GIF/WebM cards (`gif2mp4.py`), missing-clip placeholders. |
| **Simulated UI** | `chat`, `term`, `file`, `prompts`, `sketch`, `ytwall` | Live-typed AI chat threads, animated terminals, scrolling highlighted code/markdown docs, stacked prompt cards, UI wireframes, real thumbnail walls. |

---

## 4. Non-Negotiable Production Rules
1. **Clean B-Roll Law:** Full-screen AI-generated footage (`kind="full"`) never carries text captions or stamps (`build.py` strips them automatically); give key statements dedicated typographic shots.
2. **Design Token Discipline (`design-system`):** Colors (`background`, `text`, `accent`) and fonts (`font_title`, `font_body`, `font_mono`) live in `youtube-studio/brand/design.json` and propagate globally via linear color interpolation in `theme.py`.
3. **Never Stretch Short GIFs:** Pre-convert looping GIFs/stickers with `gif2mp4.py` matching exact slot duration (passing `"once"` to freeze clean one-off reactions).
4. **No Overlapping SFX:** Trigger cues (`click`, `whoosh`, `pop`, `ding`, `typing`) strictly on visual changes, sitting comfortably beneath narration with minimum `0.35s` spacing.
