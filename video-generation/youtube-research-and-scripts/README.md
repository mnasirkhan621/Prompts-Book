# 🎯 YouTube Research, Hooks & Retention Scripting Suite
**Architect & Lead Developer:** **Muhammad Nasir Khan**  
**Repository:** Prompts Book | End-to-End Video Production Engine

---

## Overview

Generating photorealistic AI footage is only half the battle—winning attention on YouTube, Shorts, Reels, and TikTok requires **data-backed topic selection, psychological hooks, retention pacing, and anti-AI-slop spoken scripts**.

This module turns **Prompts Book** into a complete pre-production intelligence and scripting partner, pairing structured research frameworks with local Python automation inside [`tools-and-workflows/youtube-research/`](../../tools-and-workflows/youtube-research/) and native agentic skills inside [`.claude/skills/`](../../.claude/skills/).

---

## 📚 Module Index

| Guide | Core Architecture & Workflow | Linked Agent Skill(s) |
| :--- | :--- | :--- |
| [YouTube Research & Breakdown Protocol](youtube-research-and-analysis-protocol.md) | Outlier scoring (`views / median`), rolling-median breakout detection (`>= 3x`), frame-by-frame visual contact sheets, and cross-platform reel analysis. | `research`, `analyse`, `channel-analysis`, `outlier-pulse`, `breakout-detector`, `study`, `video-breakdown` |
| [Audience Bullseye & Hook Machine](audience-bullseye-and-hooks.md) | The 5-Ring Audience Bullseye (`3-2-2` content mix), data-backed 15–20 rule hook rubrics, and non-redundant Title / Thumbnail / Hook design. | `bullseye`, `hook-machine`, `about-me` |
| [Viral Script Engineering & Linting](viral-script-engineering-and-linting.md) | Retention structures, 150 WPM pacing timelines, banning 45+ AI-tell phrases, `[proof: ...]` visual cues, and automated auditing with `script_check.py`. | `script`, `about-me` |

---

## 🛠️ Quick CLI Reference

```bash
# Install dependencies (Python 3.10+, FFmpeg, Node.js recommended)
pip install -r requirements.txt

# 1. Watch & extract frames + contact sheets + transcript for any video (no API key needed)
python tools-and-workflows/youtube-research/yt.py watch https://youtu.be/VIDEO_ID

# 2. Scan a channel for outlier multipliers (requires YouTube Data API v3 key in .env)
python tools-and-workflows/youtube-research/yt.py channel @handle --days 90 --json

# 3. Extract Instagram Reels / TikTok frames, audio, and metrics
python tools-and-workflows/youtube-research/reel_fetch.py https://www.instagram.com/reel/XXXX/

# 4. Batch download max-resolution thumbnails + index CSV
python tools-and-workflows/youtube-research/thumbs.py https://www.youtube.com/@handle/videos --max 30

# 5. Audit any voiceover script for pacing, weak openers, and AI-tell phrases
python tools-and-workflows/youtube-research/script_check.py path/to/script.md
```
