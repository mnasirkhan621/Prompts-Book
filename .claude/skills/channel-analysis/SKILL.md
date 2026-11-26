---
name: channel-analysis
description: Deep-analyze a whole YouTube channel (your own or a competitor's) over a date range and produce a visual report of the best topics, hooks, formats and non-obvious patterns, comparing winners against losers. Use when the creator says "analyze my channel", "analyze <channel>", "what's working for X", or asks for a recurring channel report.
---

# Deep Channel Analysis

## Inputs (ask if missing, one question at a time)
- Channel (handle, URL or ID): the creator's own or one from `youtube-studio/brand/about_me/competitors.md`.
- Date range: default **last 60 days** for the creator's own channel, 90 for competitors.
- All videos (default, so winners can be compared with losers) or only the top 10-15 by outlier score.
- Format: long-form, Shorts, or both.

## Gather with `tools-and-workflows/youtube-research/yt.py` (free)
1. `python tools-and-workflows/youtube-research/yt.py channel <channel> --days 60 --json` (`--long` / `--shorts` to filter): subs, uploads in range with views, likes, comments and duration, and each video's **outlier x** = views / the median in that window. Needs the API key in `tools-and-workflows/youtube-research/.env`; if missing, point to `tools-and-workflows/youtube-research/YT_API_KEY_SETUP.md`.
2. Split into **winners** (outlier >= 2x) and **the rest**.
3. For every winner plus about 5 average videos: `python tools-and-workflows/youtube-research/yt.py transcript <url>` and take the **first ~20 seconds** (the hook) and the structure.
4. Top 1-3 winners: `python tools-and-workflows/youtube-research/yt.py watch <url>` and read the contact sheets in `youtube-studio/research/<id>/sheets/` for format, visuals and packaging.
5. `python tools-and-workflows/youtube-research/yt.py comments <url>` on the top 2 winners: what people quote and feel.
6. Never invent numbers. If something fails (quota, private video), say so and add a "missing data" note.

## Analyze
For winners vs the rest, compare: **topics**, **hooks** (first-line pattern: question, then-vs-now, bold claim, story), **formats** (talking head, essay, tutorial, list, battle), **titles and thumbnails**, **length**, **publish timing**, and the **non-obvious patterns** (what ALL winners share that no average video has). Each insight needs 2+ example videos as proof.

## Output
- An HTML report published as an artifact: headline insight, a winners table with thumbnails and links, sections for topics, hooks, formats and non-obvious patterns, and **"Do next: 3 video ideas"** that fit the creator (`youtube-studio/brand/about_me/`).
- Save the raw notes to `youtube-studio/research/<channel>_<YYYY-MM-DD>.md` so other skills (`hook-machine`) can reuse them.
- Offer a recurring refresh every 2 weeks only if the creator asks.
