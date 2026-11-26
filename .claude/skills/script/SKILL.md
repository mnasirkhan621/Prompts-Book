---
name: script
description: Write, rewrite or punch up a YouTube or reel script so it sounds like the creator (human, honest, engaging) and follows the patterns that make videos hold attention. Use whenever the creator asks to write a script, brainstorm a video, fix "boring" or "AI-sounding" lines, merge drafts, or plan a series of videos that must not contradict each other.
---

# Script Skill

## Before Writing, Read
1. `youtube-studio/brand/about_me/voice.md` (how the creator talks, what they hate, AI tells to cut). If it's missing, run `about-me` first.
2. `youtube-studio/brand/about_me/who_i_am.md` and `bullseye.md` (who the viewer is).
3. `youtube-studio/brand/hook_rubric.md` if it exists (from `hook-machine`).
4. If the video belongs to a series, the series plan: stay in this video's lane, use the shared stance, don't repeat what another video owns.

## Grill First
Ask one question at a time (with your recommended answer) until these are clear: who the viewer is, the one takeaway, the title and thumbnail idea, what's cut, the length (default under 5:00 ~= 650-750 words). Personal claims must be true: ask before writing "I tried / I talked to / for X years".

## Patterns That Hold Viewers
1. **Fear or problem -> reassurance ending.** Name the worry viewers already feel, then leave them calmer with a real answer.
2. **Then vs now in the first ~12 s.** Paint how it used to be, then the turn. Do NOT spoil the answer in the hook.
3. **Open question early, paid off late.** "So what's really happening?" answered near the end.
4. **Proof on screen** for every claim (charts, posts, real pages). Write `[proof: ...]` notes for the editor; never invent stats.
5. **A clear stance** people can argue with in the comments, without guru hype.
6. **A short, self-aware CTA** at the end, never at the start.
7. **Retention:** the first seconds show what the title and thumbnail promised; right after the hook, say what's coming ("...and at the end, ..."); add a rehook around 2-3 min; end soon after the payoff.

## Don't
- Generic advice anyone could give. The answer must be the creator's own story, setup or test.
- A rant with no answer. Rant -> turn ("I used to think...") -> their answer -> outro.
- Contradicting another video in the series, or repeating a point twice in one video.
- Copying another creator's wording. Take ideas and structure, write it in the creator's words.
- Cut-off setups. Every new section needs a lead-in from the last line.

## Writing Rules
- The creator's own lines stay word for word (fix grammar and spelling only). Mark which lines are theirs when you hand it over.
- Engaging = honesty + one light joke per section + a direct question to the viewer about every 30 s + "..." pauses before reveals.
- Link beats with "but" or "so", not "and then". Vary sentence length: short lines, plus one longer "thinking out loud" sentence per section.
- Plain words (~8th grade), one idea per sentence, an example instead of a definition.
- One list of three per section, max. No neat moral line at the end of every section.
- `---` between beats (the editor cuts there). Website links next to tool names.

## Finish
1. Run `python tools-and-workflows/youtube-research/script_check.py <script.md>` (add `--short` for reels). It prints words, length at 150 wpm and when each part starts, and flags weak openers, AI phrases, 25+ word sentences, "and then" chains, number claims, a missing tease on long videos and a missing outro line (set yours in `youtube-studio/brand/outro.txt`). Fix every FAIL; warnings are things to look at, not orders.
2. Read it top to bottom: does the hook's question get answered? Does the outro match what the video gave?
3. Tell the creator what changed, what was cut, and anything that needs their OK (unverified facts, claims about them).
