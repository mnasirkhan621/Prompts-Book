# YouTube Production Studio Workspace
**Architect & Lead Developer:** **Muhammad Nasir Khan**

This directory serves as the local working state for the **Prompts Book YouTube Research & HyperFrames Code-Editing Pipeline**. All downloaded research clips, thumbnails, personal creator brand profiles, sound effects, and rendered videos live cleanly here without cluttering the repository root.

## Directory Layout

* **`brand/`**: Stores your creator context (`about_me/who_i_am.md`, `how_you_work.md`, `voice.md`, `competitors.md`, `bullseye.md`), locked `hook_rubric.md`, `outro.txt`, and visual design system tokens (`design.md`, `design.json`).
* **`research/`**: Gitignored workspace where [`yt.py`](../tools-and-workflows/youtube-research/yt.py), [`reel_fetch.py`](../tools-and-workflows/youtube-research/reel_fetch.py), and [`thumbs.py`](../tools-and-workflows/youtube-research/thumbs.py) save transcripts, extracted video frames, contact sheets, thumbnails, and channel analysis notes.
* **`sfx/`**: Gitignored folder where you place your own licensed sound effects (`click`, `whoosh`, `pop`, `ding`, `typing`, `error`, `hit`, `boom`, `scratch`) for the HyperFrames Edit Kit.
* **`videos/`**: Gitignored workspace where [`new_video.py`](../tools-and-workflows/hyperframes-edit-kit/edit_kit/new_video.py) initializes per-video folders (`audio/`, `assets/`, `storyboard/`, `project/`, `renders/`).
