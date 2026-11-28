# Google Veo 3 / Veo 3.1 Prompting & Visual DNA Guide
### *Shot-List Ordering, Native 48kHz Audio/Dialogue & Multi-Shot Continuity*
**Architect:** **Muhammad Nasir Khan** *(with MIT frameworks integrated from `kdowswell/veo-tools`)*

Google **Veo 3** and **Veo 3.1** combine high-precision optical physics with native synchronous 48kHz audio (dialogue lip-sync, foley SFX, ambient beds). Treating Veo like a loose brainstorming chatbot wastes generation credits; treating it like a structured shot-list produces consistent cinema.

---

## 1. The 5-Element Veo Shot-List Formula

Veo assigns higher attention weight to tokens near the start of the prompt. Always lead with cinematography and lock to **one primary camera vector**:

```text
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance] + [Audio / Dialogue]
```

* **Cinematography:** Shot size + angle + single camera movement + lens (`Medium close-up, eye-level, slow dolly forward, 35mm lens, shallow depth of field`).
* **Subject:** Specific physical materials and textures (`brushed titanium with hairline micro-scratches`, `weathered wool trench coat`).
* **Action:** One dominant movement in present continuous tense (`turning a brass dial`, `steam rising slowly`).
* **Context:** Grounded location and time of day (`corner concrete studio at dusk, rain streaking tall windows`).
* **Style & Ambiance:** Light direction, color palette, Kelvin tone (`3200K warm side key, 4:1 contrast, lifted blacks, subtle 35mm grain`).
* **Audio / Dialogue:** Explicit foley/ambient bed and colon-anchored speech (`Audio: distant rain patter, crisp brass click. Architect speaks calmly: "Sequence locked."`).

---

## 2. Native Dialogue & Audio Formatting Rules

1. **Colon-Anchored Speech:** Bind spoken lines to a physical subject and verb before quotation marks (`Developer speaks quietly: "Check the latency."`) rather than floating bare quotes, which can hallucinate literal on-screen text captions.
2. **No On-Screen Text Requests:** Veo struggles with arbitrary legible UI overlays or brand logos. Keep text/logos out of the prompt and composite them cleanly in post-production (`HyperFrames` or After Effects).
3. **Plain-Noun Negative Prompts:** Veo's negative-prompt parameter expects **plain descriptive noun phrases** (`blurry, watermark, text overlay, extra fingers, morphing geometry`), not imperative negations (`no text`, `don't blur`).

---

## 3. Visual DNA for Multi-Shot Sequences

When stitching 3–6 Veo clips via `tools-and-workflows/veo-tools/veo-multi-generate.ts`, lock four **Visual DNA** strings verbatim across every shot prompt while varying only shot size, camera trajectory, and subject action:

| Parameter | Lock Across All Clips | Example String |
| :--- | :--- | :--- |
| **Color Palette** | Exact primary/accent/shadow treatment | `deep slate #0f172a, warm amber #f59e0b accents, lifted blacks` |
| **Lighting Style** | Direction, softness, contrast ratio | `soft diffused side-lit key with subtle rim separation` |
| **Atmosphere** | Mood and particulate texture | `contemplative tech studio, subtle airborne dust motes` |
| **Camera Energy** | Baseline pacing | `measured slow mechanical movement` |

Presets live in [`.claude/skills/veo-multi-shot/templates/visual-dna/`](../../.claude/skills/veo-multi-shot/templates/visual-dna/tech-saas.md).

---

## 4. Seamless Loop & Hero Background Rules

For website hero backgrounds and ambient UI loops (4s–6s clips processed via `tools-and-workflows/veo-tools/create-loop.sh`):
* Always declare `locked camera` or `static camera` plus `seamless loop`.
* Restrict motion to gentle, continuous physics (`particles drifting slowly`, `light shifting imperceptibly`, `mist rolling gently`).
* Avoid directional travel (`walking across frame`, `cars driving left-to-right`) when using forward-reverse-crossfade looping.

---

## 5. Production Example (Veo 3.1 Native Audio)

```text
Model: Veo 3.1 | Aspect: 16:9 | Duration: 8s | Resolution: 1080p | Native Audio: On

Medium close-up, eye-level, Slow Dolly In on a 35mm lens with shallow depth of field.
A software architect in a charcoal merino crewneck leans over a matte basalt table, resting fingers on brushed aluminum keys as dust motes drift across warm 3200K left amber light and cool 6000K right cyan rim light.
He turns his gaze calmly toward the screen and taps a single anodized enter key.
Look: Soft Cross lighting, 4:1 contrast ratio, lifted blacks, crisp 35mm film grain.
Audio: Quiet concrete room tone, single crisp mechanical keystroke click, warm low analog synth drone.
```

---

## Related Skills & Tools

* Single-shot & loop skill: [`.claude/skills/veo/SKILL.md`](../../.claude/skills/veo/SKILL.md)
* Multi-shot Visual DNA skill: [`.claude/skills/veo-multi-shot/SKILL.md`](../../.claude/skills/veo-multi-shot/SKILL.md)
* Seamless loop maker skill: [`.claude/skills/video-loop/SKILL.md`](../../.claude/skills/video-loop/SKILL.md)
* GCP/Vertex AI setup skill: [`.claude/skills/veo-setup/SKILL.md`](../../.claude/skills/veo-setup/SKILL.md)
* Executable CLI & FFmpeg tools: [`tools-and-workflows/veo-tools/README.md`](../../tools-and-workflows/veo-tools/README.md)
