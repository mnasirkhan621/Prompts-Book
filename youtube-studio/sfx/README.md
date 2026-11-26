# youtube-studio/sfx/

Place your own sound effect files here (all audio binaries remain local and are excluded by `.gitignore`). The HyperFrames Edit Kit (`tools-and-workflows/hyperframes-edit-kit/edit_kit/build.py`) automatically discovers these base names in any standard audio format (`.wav`, `.mp3`, `.ogg`, `.m4a`):

- **Core UI & Transition Cue Set:** `click`, `whoosh`, `pop`, `ding`, `typing`
- **Emphasis & Impact Cue Set (Optional):** `error`, `hit`, `boom`, `scratch`

Only use audio files you hold rights to (your own recordings or royalty-free packs). Missing SFX files are gracefully skipped without breaking builds.
