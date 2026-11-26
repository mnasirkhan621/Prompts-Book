---
name: design-system
description: Grill the creator until they have their own visual system for videos and thumbnails - colors, fonts, text style, captions, sound rules, editing pace and things they never do - then write it to youtube-studio/brand/design.md and youtube-studio/brand/design.json, which the other skills and tools read. If the creator already made a brand somewhere in the project, it finds and imports it instead of asking again. Use on first setup, when the creator says "build my design system", "what should my videos look like", "pick my colors/fonts", or when another skill needs brand values and design.md doesn't exist yet.
---

# Design System Builder (Grill Me)

This kit ships with **no forced brand**. Every creator builds their own here. Never invent a style for them and never copy another creator's look: ask, show, and let them pick.

## First: Find a Brand They Already Made
Many creators already built a brand before running this skill (via a style guide, Canva brand kit, notes, or prior config). **Never make them do it twice.** Before any question:
1. If `youtube-studio/brand/design.json` exists with the keys below, use it and stop here (unless they asked to change something).
2. Otherwise search the project folder (skip `.git`, `node_modules`, `youtube-studio/videos/`, `renders/`) for brand files: names containing `design`, `brand`, `style`, `theme` or `identity` (`.md`, `.json`, `.txt`, `.yaml`), plus workspace rule files (`CLAUDE.md`, `GEMINI.md`, `AGENT.md`) mentioning colours or fonts.
3. If you find one, read it and summarize what you found in one message for confirmation.
4. On confirmation: write `youtube-studio/brand/design.json` with the kit's keys from it (copying their values accurately), and copy or link the original as `youtube-studio/brand/design.md`. Then ask **only** about missing fields (typically sound files in `youtube-studio/sfx/`, `max_hold`, captions), one question at a time, best guess first.
5. If two files disagree, show both values and ask which one wins.
6. Found nothing? Run the full grill below.

## Before Asking
1. Read `youtube-studio/brand/about_me/` (run `about-me` first if empty: the style must fit the person and audience).
2. If `youtube-studio/brand/design.md` exists, show it and ask only about what they want to change.
3. Ask for 2-5 references they love (videos, channels, thumbnails, websites). If they give links, analyze them using the local `video-breakdown` skill and extract patterns (never clone).

## Grill, One Question at a Time
Ask one question at a time with 2-4 concrete options (your recommendation first). **Show, don't describe** whenever it's visual: render a small preview (HTML artifact or inline preview) of each option on a 16:9 frame and a thumbnail-size frame.

Go through these branches in order:
1. **Personality:** three words for how the channel should feel (calm, loud, nerdy, luxury, playful...). Everything after must fit them.
2. **Background:** dark, light, or a texture or colour. Show 3 swatches with sample text.
3. **Accent colour:** one main accent (4 options on the chosen background). Ask if a second colour is ever allowed.
4. **Text colour:** checked for contrast on the background (target >= 4.5:1 WCAG AA and state the ratio).
5. **Fonts:** max 3: title font, body/caption font, and optional monospace font for code/URLs. Use free Google Fonts unless licensed. Show each with their real channel name.
6. **Big text style:** flat colour, gradient, outline, glow or shadow.
7. **Thumbnails:** face or no face, word count (3-5 max), font pairing.
8. **Captions:** on/off, 1 or 2 lines, word highlight vs static, vertical safe zone (above ~70% height to stay clear of the player progress bar).
9. **Sound:** music yes/no, sound effects (`click`, `whoosh`, `pop`, `ding`, `typing`; optional `error`, `hit`, `boom`, `scratch`), and loudness rule (voice clearly dominant over SFX, no stacked SFX). Verify matching files exist in `youtube-studio/sfx/` (royalty-free or self-recorded only).
10. **Pace:** target interval between visual changes (e.g., 2-3 s in tutorials). Save longest hold in seconds as `max_hold`.
11. **Never list:** forbidden effects/patterns (flashing, glitch transitions, shaky cam, AI-slop stock overlays, colliding simultaneous entrances).
12. **Formats:** which video formats they produce (tutorial, essay, list, talking head, reels).

If an answer contradicts a previous rule (e.g., "calm" channel with violent glitch wipes), point it out and let the creator decide.

## Write the Result
1. `youtube-studio/brand/design.md`: short, readable, dated: each decision with one line of why. End with the "Never" list.
2. `youtube-studio/brand/design.json` (the tools read these keys):
```json
{
  "background": "#111111",
  "text": "#FFFFFF",
  "accent": "#FFCC00",
  "accent_2": null,
  "font_title": "Font Name",
  "font_body": "Font Name",
  "font_mono": "Font Name",
  "caption_size": 56,
  "caption_position": "bottom",
  "sfx": ["click", "whoosh", "pop", "ding"],
  "music": false,
  "max_hold": 4.5
}
```
The values above are placeholders: fill in the creator's own choices.
3. Verify every sound listed in `design.json -> sfx` has a matching audio file in `youtube-studio/sfx/` and flag missing ones.
4. Deliver a one-page style guide HTML artifact previewing swatches, typography, sample thumbnail, sample caption frame, and Never list.

## Later Changes
When the creator locks a new rule, append it to `youtube-studio/brand/design.md` with the date, update `design.json` if needed, and keep a brief "Changed" note for history.
