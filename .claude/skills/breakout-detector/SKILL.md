---
name: breakout-detector
description: Find the exact video where a creator broke out (a sudden spike after a flat stretch), then reverse-engineer what changed in topic, hook, format or packaging. Use when the creator finds a smaller channel that grew fast, asks "when did X blow up" or "what made them grow", or wants to study a channel's turning point.
---

# Creator Breakout Detector

## Inputs
- Channel (handle, URL or ID).
- Look-back: default **730 days**. Use 45-100 days for young channels.
- Long-form, Shorts, or both.

## Run
1. `python tools-and-workflows/youtube-research/yt.py channel <id|@handle> --days 730 --max 500 --json`: every video in range with views and publish date (needs API key in `tools-and-workflows/youtube-research/.env`; ~1 unit per 50 videos).
2. Sort by date. Compute a rolling median of the previous 5-10 videos; a **breakout** is a video at >= 3x that median, especially when the videos after it stay higher (a new baseline, not a one-off). Note that API returns current view totals, so older videos had longer to accumulate views.
3. Subscriber history isn't in the YouTube Data API. If the growth curve matters, note what public stats show and clearly cite the source.
4. Pick the main breakout (plus up to 2 smaller ones). For each, compare it with the 5 videos before it: topic, title, thumbnail, length, hook (`python tools-and-workflows/youtube-research/yt.py transcript <url>`, first ~20 s), format, posting time. Run `python tools-and-workflows/youtube-research/yt.py watch <url>` on the breakout only and read its contact sheets in `youtube-studio/research/<id>/sheets/`.
5. Note what stayed after the breakout (did the creator repeat the winning pattern?).
6. If the key is missing or something fails, stop at what you have and say what's missing. Never invent data.

## Output
- A chronological chart (views per video, breakout marked in one accent colour) as an artifact, plus a table: before vs breakout vs after.
- **"What you can take"**: 3 patterns adapted to the creator's brand and bullseye, never copied wording.
- Save notes to `youtube-studio/research/breakout_<channel>_<YYYY-MM-DD>.md`.
- For a full creative breakdown of the breakout video, hand off to `video-breakdown`.
