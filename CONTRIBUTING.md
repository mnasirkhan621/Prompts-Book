# Contributing to Prompts Book
### *World-Class Standards for AI Video & Audio Prompt Engineering*
**Architect:** **Muhammad Nasir Khan**

Thank you for your interest in contributing to **Prompts Book**. To maintain our standing as the global benchmark for AI Video and Audio prompts, all submissions must adhere to the following standards.

---

## 1. Submission Guidelines

### For Video Prompts:
* **Enforce MCSLA**: Every video prompt must include Model, Camera, Subject, Look, and Action/Audio.
* **Zero Slop**: Must not contain unmeasurable adjectives (`stunning`, `epic`, `breathtaking`, `photorealistic`).
* **Run the Linter**: Run `python tools-and-workflows/prompt_linter.py --video "<your_prompt>"` and achieve a score of **90/100 or higher**.

### For Audio Prompts:
* **7-Element Architecture**: Include Era, Genre, Mood, Instruments, Vocals, Production, and BPM/Key.
* **Character Budget**: Keep style prompts under 450 characters (hard limit 950).
* **Balanced Lyrics**: Maintain consistent syllabic counts across rhyming lines.

---

## 2. Pull Request Process

1. Fork the repository and create your branch: `git checkout -b feature/new-genre-prompts`.
2. Add your original prompt templates to the appropriate genre directory.
3. Verify all formatting in standard Markdown.
4. Submit your pull request with a clear description of the tested model and parameters.
