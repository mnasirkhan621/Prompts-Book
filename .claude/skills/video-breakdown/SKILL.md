---
name: video-breakdown
description: Analyze a reference YouTube video or Short (why it went viral, its hook, pacing, b-roll, sound effects) by watching it fully, not just the transcript, then turn the lessons into the creator's own rules. Use when the creator pastes YouTube/TikTok/Instagram links and asks why they worked, what to learn, or how a video was edited.
---

# Reference Video Breakdown

## 1. Gather with `tools-and-workflows/youtube-research/yt.py` (Free)
- `python tools-and-workflows/youtube-research/yt.py video <url>`: views, likes, comments, duration, publish date. *(needs API key in `tools-and-workflows/youtube-research/.env`)*
- `python tools-and-workflows/youtube-research/yt.py channel <channelId|@handle> --days 120`: the channel's other uploads and each one's **outlier x** (views / channel median), to see how far above normal the video is. *(needs API key)*
- `python tools-and-workflows/youtube-research/yt.py watch <url> [--lang xx]`: **watch the whole video**. Downloads <=480p into `youtube-studio/research/<id>/`, saves a frame every 2 s plus contact sheets (12 frames per image) and the transcript. **Read every sheet** in order and line it up with the transcript to log the hook (exact words + what's on screen), every visual change, cut rhythm, on-screen text style, b-roll, structure and CTA. For one moment, read the single frames (`frame k` is at `(k-1)*2 s`). No key needed.
- Sound: infer sound effects and music from transcript tags (`[music]`) and cut moments, marking audio observations as inferred unless an audio analysis tool is available.
- `python tools-and-workflows/youtube-research/yt.py transcript <url> [--lang xx]`: exact wording (captions, falls back to Whisper). No key needed.
- `python tools-and-workflows/youtube-research/yt.py comments <url> --max 60`: top comments show what people felt and quoted. *(needs API key)*
- TikTok and Reels: `watch` works on any URL `yt-dlp` supports; otherwise use `tools-and-workflows/youtube-research/reel_fetch.py`, or ask for the file.

## 2. Report
- Table: views vs channel average, length, comments.
- What the videos share (topic timing, hook, structure, pacing, proof, humour, comment debate, CTA).
- **What to take and what to skip**, checked against the creator's goals and audience in `youtube-studio/brand/about_me/`, and their style notes in `youtube-studio/brand/style.md` if they keep one.

## 3. Turn Lessons Into Reusable Rules
- Editing and visual lessons -> `youtube-studio/brand/style.md`; script patterns -> `youtube-studio/brand/hook_rubric.md` or the `script` skill. Only lock when the creator confirms, with the date.

## Rules
- Never cut clips out of another creator's video. Recreate visual beats cleanly with AI generation, free stock, or original screen captures.
- Ideas and structure can be borrowed. Wording can't: rewrite it in the creator's voice (`youtube-studio/brand/about_me/voice.md`).
- Videos are downloaded only for private analysis.
