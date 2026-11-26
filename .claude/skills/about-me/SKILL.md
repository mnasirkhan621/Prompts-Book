---
name: about-me
description: Interview the creator and write or refresh their "About Me" context files (youtube-studio/brand/about_me/who_i_am.md, how_you_work.md, voice.md, competitors.md), so every session starts knowing who they are. Use on first setup, when the creator says "run the about me interview" or "update my context", or when their goals, projects or way of working changed.
---

# About Me Interviewer

Goal: give the AI assistant deep, permanent context about the creator, so every session (scripts, thumbnails, edits, strategy) starts knowing who they are, what they're aiming for and how they like to work.

## Files
| File | Holds |
|---|---|
| `youtube-studio/brand/about_me/who_i_am.md` | Background, current projects, goals and where they stand against them, struggles, the audience they serve |
| `youtube-studio/brand/about_me/how_you_work.md` | How the assistant should work with them: when to ask vs act, how they give feedback, what annoys them, schedule, tools, who does what, what "done" means |
| `youtube-studio/brand/about_me/voice.md` | How they talk and write: favourite phrases, words they never use, AI-sounding lines to cut |
| `youtube-studio/brand/about_me/competitors.md` | Channels to track for `outlier-pulse` and `breakout-detector` (name, handle, why, long or short) |

## Process
1. Read what already exists first (`CLAUDE.md`, `GEMINI.md`, the files above, `youtube-studio/brand/design.md`). Never ask something the repo already answers. Show what you already know and ask them to correct it.
2. Interview **one question at a time**, with your best guess as the first answer option (use structured questions when available), 10 to 15 questions in total. Cover: who they are, goals (numbers and dates), current status, struggles, audience (one ideal viewer), how they want you to work, how they talk (ask for 2-3 of their own old scripts or captions to learn the voice), competitors to track.
3. Use their exact words where possible. Mark guesses `(unconfirmed)`.
4. Write the files, each under ~60 lines, plain bullets, dated at the top.
5. Keep `youtube-studio/brand/about_me/` updated as the source of truth before strategy, scripts, edits, or thumbnails.

## Refresh
Show a short diff of what changed (old -> new) and update the date. Don't delete old goals: move them to a "Past goals" section with the outcome.
