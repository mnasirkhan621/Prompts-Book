---
name: bullseye
description: Build the creator's audience bullseye - five rings from their exact niche (center) out to the broadest audience - and set their content mix per week (default 3-2-2). Use when the creator asks who their audience is, how narrow or broad a video idea is, what their content mix should be, or whether an idea is "too broad". Needs no data tools.
---

# Audience Bullseye Builder

## Idea
Ring 5 (center) = the creator's exact niche. Each ring outward is broader. Mix per 7 videos: **3 in ring 5, 2 in rings 3-4, 2 in ring 2. Never ring 1** (too broad: views from people who will never care about the niche).

## Process
1. Read `youtube-studio/brand/about_me/who_i_am.md` and workspace rules (`CLAUDE.md`, `GEMINI.md`). Don't re-ask what's there.
2. Interview one question at a time (best guess as option 1) to pin down **one ideal viewer**: who they are, what they're stuck on, what they'd pay for, where they hang out.
3. Draft the 5 rings in the creator's words. Example shape for an "AI video creators" channel:
   - 5: creators generating AI films and YouTube videos end-to-end
   - 4: video editors and motion designers adopting AI workflows
   - 3: content creators looking for faster scripting and editing tools
   - 2: tech and productivity enthusiasts curious about generative AI
   - 1: general news or broad entertainment (avoid)
4. For each ring: rough audience size (mark as estimate), what a video for that ring sounds like, and one example title.
5. Tag existing and planned videos with their ring and check the mix.

## Output
- `youtube-studio/brand/about_me/bullseye.md`: the rings, the ideal viewer, the mix rule, and a table of planned videos by ring.
- Optional: a simple bullseye graphic as an artifact, in the creator's colours if `youtube-studio/brand/design.json` exists.
- When the creator proposes an idea later, say which ring it hits in one line.
