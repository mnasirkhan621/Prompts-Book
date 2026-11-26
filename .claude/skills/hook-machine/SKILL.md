---
name: hook-machine
description: Build and use a data-backed hook rubric - extract real hooks from winning videos (your channel or a competitor's), turn their patterns into 15-20 rules, then write new hooks for a topic or grade the creator's own hook and offer better versions. Use when the creator asks for hooks, an opening line, "is this hook good", or "make my intro stronger".
---

# Hook Machine

## 1. Build or Refresh the Rubric (`youtube-studio/brand/hook_rubric.md`)
1. Source channels: the creator's own winners first; if there are few, one or two competitors from `youtube-studio/brand/about_me/competitors.md` or a channel they name.
2. Pick winners (outlier >= 2x) with `python tools-and-workflows/youtube-research/yt.py channel <channel> --days 180 --json` (API key in `tools-and-workflows/youtube-research/.env`); reuse `youtube-studio/research/*` notes if a channel analysis already exists.
3. For each winner, `python tools-and-workflows/youtube-research/yt.py transcript <url>` (no key needed): copy the **exact first ~15-20 s**, the title and the thumbnail text (read frames 0001-0003 from `python tools-and-workflows/youtube-research/yt.py watch <url>` in `youtube-studio/research/<id>/frames/` for the on-screen hook). Aim for 15-30 hooks.
4. Cluster them: what pattern opens each one (then-vs-now, bold claim against common belief, personal confession, question, number or result first, story in motion), what the visual does, how fast the tension rises, when the "why stay" promise lands.
5. Merge with the fixed principles below and with the `script` skill. Write **15-20 numbered rules**, each with one real example and its source video.
6. If the API key is missing, ask for winner URLs directly (transcripts work without a key), build from what you have and mark it "partial".

**Fixed principles (always in the rubric):**
- The first line names a tension the viewer already feels. No greeting, no "in this video".
- Don't give away the answer in the hook.
- Say it the way the creator talks (`youtube-studio/brand/about_me/voice.md`): honest, plain words, no hype.
- Title, thumbnail and hook each add something; they never repeat each other word for word.
- A visual change within the first 2 s; the hook is readable as on-screen text.
- Under ~15 s / ~40 words to the open question.

## 2. Use It
- **New topic:** write 8-10 hooks across different rule patterns, grade each 1-10 against the rubric (show which rules it hits or misses), and recommend the top 2.
- **Grade the creator's hook:** score it, say which rules it misses in plain words, then give 3 better versions that keep their own words and idea where possible. Their line stays the baseline: never silently replace it.
- Check every hook against the title and thumbnail planned for that video.
