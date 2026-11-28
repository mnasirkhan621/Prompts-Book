# Veo 3 / 3.1 CLI & FFmpeg Assembly Tools
### *Vertex AI Video Generation, Multi-Shot Orchestration, Crossfade Assembly & Seamless Loops*
**Upstream Source:** [`kdowswell/veo-tools`](https://github.com/kdowswell/veo-tools) (MIT License — Copyright (c) 2025 Kurt Dowswell)  
**Integrated into:** **Prompts Book** by Muhammad Nasir Khan

---

## Included Utilities

| Script | Runtime | Purpose |
| :--- | :--- | :--- |
| [`veo-generate.ts`](veo-generate.ts) | Node / `ts-node` | Single-shot Google Veo 3.1 generation via Vertex AI with LRO polling & download |
| [`veo-multi-generate.ts`](veo-multi-generate.ts) | Node / `ts-node` | Multi-shot batch generator with Visual DNA keyword consistency checks |
| [`assemble-clips.sh`](assemble-clips.sh) | Bash + FFmpeg | Concatenate clips with `cut`, `crossfade`, or `fade-black` transitions & optional audio |
| [`create-loop.sh`](create-loop.sh) | Bash + FFmpeg | Forward-reverse-crossfade mathematical seamless infinite loop generator |

---

## Prerequisites & Environment

1. **Google Cloud & Vertex AI** (for `veo-generate.ts` / `veo-multi-generate.ts`):
   - `gcloud` CLI authenticated (`gcloud auth application-default login` or service account key)
   - Environment variables:
     - `GOOGLE_CLOUD_PROJECT`
     - `GOOGLE_CLOUD_LOCATION` (default: `us-central1`)
     - `GOOGLE_APPLICATION_CREDENTIALS`
   - See [`.claude/skills/veo-setup/SKILL.md`](../../.claude/skills/veo-setup/SKILL.md) for full setup instructions.
2. **FFmpeg** (for `assemble-clips.sh` and `create-loop.sh`) and **Node.js** (`npx ts-node`).

---

## Quick Usage

```bash
# Single clip via Google Veo 3.1
npx ts-node tools-and-workflows/veo-tools/veo-generate.ts \
  --prompt "Slow dolly forward through brutalist concrete atrium, single warm amber beam shifting across wall, seamless loop, locked camera" \
  --aspect-ratio 16:9 --duration 6 --resolution 720p --output ./hero.mp4

# Multi-shot Visual DNA batch + crossfade assembly
npx ts-node tools-and-workflows/veo-tools/veo-multi-generate.ts \
  --shots "Shot 1 prompt:::Shot 2 prompt:::Shot 3 prompt" \
  --durations "6,6,6" --assemble --transition crossfade --output ./output/ --project-name "launch"

# Convert any clip into a seamless infinite loop
bash tools-and-workflows/veo-tools/create-loop.sh hero.mp4 hero-loop.mp4 0.5
```
