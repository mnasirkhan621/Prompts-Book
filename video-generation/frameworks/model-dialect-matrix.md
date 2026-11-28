# Multi-Model Video Dialect Matrix
### *Syntactical Compilers for Leading Diffusion & Autoregressive Engines*
**Architect:** **Muhammad Nasir Khan**

Different AI video generation engines employ distinct text-encoder architectures (T5-XXL, CLIP, proprietary multimodal LLMs). A prompt structured for Kling will underperform in Runway or Sora if not translated into that engine's native dialect.

---

## 1. Engine Comparison Overview

| Engine | Primary Text Encoder | Dialect Style | Ideal Token Budget | Negative Prompts? | Key Strengths |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Kling 3.0 / 2.6** | Multimodal Diffusion | Front-weighted prose, named presets | 40 – 90 words | ✅ Field (Plain terms) | Physical realism, fluid liquid/cloth, complex anatomy |
| **Google Veo 3 / 3.1** | Gemini Multimodal Encoder | Shot-list order + Visual DNA + colon speech | 45 – 110 words | ✅ Field (Plain nouns) | Native 48kHz audio/lip-sync, specular/lighting physics |
| **Runway Gen-3 / Gen-4** | Structured Multi-Stream | Tri-part bracketed/colon syntax | 30 – 60 words | ❌ No (`no X` can summon X) | Cinematic lighting, speed ramps, photoreal faces |
| **OpenAI Sora / Sora 2** | Autoregressive Diffusion Transformer | Dense atmospheric narrative prose | 80 – 160 words | ❌ Fold positive rules | Physics simulation, long temporal continuity, complex camera |
| **Luma Dream Machine** | Video Diffusion Transformer | Trajectory keyframes (Start → End) | 40 – 80 words | ❌ No | Rapid dynamic motion, camera flythroughs |
| **Seedance 2.0 / 2.5** | Direct Director Engine | Coordinate, `@Image1/@Video1/@Audio1`, up to 30s beats | 50 – 150 words | ✅ Web field only | Frame-accurate cinematography, 30s multi-asset reference lock |
| **LTX-2 / 2.3 / 2.5** | Lightricks DiT + Audio | Single-take prose, screenplay cuts, Dub-It | 4–8 sentences | ❌ Describe positive target | Native synced dialogue/foley, multi-shot cuts, IC-LoRA editing |
| **MiniMax H3 (Hailuo 3)** | Structured Audiovisual Schema | `integrated_multimodal_description` + `<d>` tags | Schema-bound | ❌ Describe observables | T2VA/I2VA/FL2VA alignment, multi-speaker `<d>` audio continuity |
| **Wan 2.2 / Wan Animate 2** | MoE Diffusion | `[Subject] + [Scene] + [Motion] + [Camera]` | 50 – 110 words | ✅ Supported | Open-weights fidelity, character animation & I2V |

---

## 2. Dialect 1: Runway Gen-3 Alpha

Runway Gen-3 Alpha processes prompts most reliably when decomposed into explicit colon-separated tags: `[Camera]`, `[Action]`, `[Lighting]`.

### Runway Syntax Formula:
```text
[Camera Movement]: [Exact trajectory and speed].
[Subject]: [Physical appearance, clothing, and initial state].
[Action]: [Kinetic progression, primary movement].
[Environment & Lighting]: [Location, light sources, volumetric conditions, color grade].
```

### Runway Production Example:
```text
[Camera Movement]: Low-angle continuous tracking shot moving backward smoothly at walking pace.
[Subject]: A 35-year-old male detective in a damp wool coat, jaw tight, looking around attentively.
[Action]: Walks through the narrow alleyway as steam rises from underground grates; he raises an umbrella against rain.
[Environment & Lighting]: Neon cyan and amber signs reflecting in deep asphalt puddles, night atmosphere, 35mm film aesthetic with subtle grain.
```

---

## 3. Dialect 2: OpenAI Sora

OpenAI Sora is an autoregressive transformer that excels at understanding cause-and-effect narrative logic, physical weight, and spatial relationships written in rich, natural cinematographic prose.

### Sora Syntax Formula:
```text
[Comprehensive Scene Establishment in 1 continuous narrative paragraph].
Include: Spatial geometry, environmental physics, subject actions, optical camera behaviors, and atmospheric light interactions.
```

### Sora Production Example:
```text
A cinematic medium-wide shot captures a weathered astronaut in a scuffed white pressurized suit kneeling on the rust-colored gravel of an alien valley during a double sunset. Twin suns—one golden yellow, one crimson red—cast elongated chromatic shadows across the jagged obsidian ridges. As the astronaut scoops up a handful of crystalline sand, fine glowing dust particles drift weightlessly through her gloved fingers. The 50mm anamorphic lens glides forward in a slow, continuous dolly push, exhibiting subtle horizontal blue flares and authentic depth-of-field falloff. Atmospheric dust swirls gently in the low-gravity breeze, catching the warm dual-toned rim lighting.
```

---

## 4. Dialect 3: Luma Dream Machine

Luma Dream Machine is exceptionally sensitive to start-frame to end-frame transitions and spatial vectors.

### Luma Syntax Formula:
```text
[Initial State] -> [Kinetic Transition / Camera Vector] -> [Final Frame State].
```

### Luma Production Example:
```text
Beginning with an extreme close-up on a vintage chrome wristwatch second hand ticking past 12.
Camera accelerates rapidly upward in a continuous vertical crane move, pulling through the ceiling rafters into a wide aerial view of the bustling 1940s train station terminal below.
Soft morning sunlight beams stream through the vaulted glass windows, illuminating hundreds of passengers in motion.
```

---

## 5. Dialect 4: Seedance 2.0 & Cinema Studio

Seedance uses precise director terminology, FOV degrees, and explicit duration bounds.

### Seedance Syntax Formula:
```text
Camera: [Named Preset] over [X]s, FOV [XX] degrees, [Aperture].
Subject: [Character Identifier / Appearance].
Action: [Primary Action] at second [X.X], resolving into [Secondary Action] by second [X.X].
Look: [Lighting & Environment Specs].
```

### Seedance Production Example:
```text
Camera: Slow Dolly In over 8 seconds, FOV 29 degrees (85mm equivalent), F1.8 aperture with locked focus plane.
Subject: Female pilot with short dark hair in a charcoal flight suit.
Action: Sits motionless in the cockpit from 0-3s; at second 4, her eyes narrow and she pushes the throttle lever forward; holds gaze through second 8.
Look: Emergency red console lighting contrasting with cold starfield ambient glow outside the glass.
```

---

## 6. Dialect 5: Google Veo 3 / Veo 3.1

Veo 3 / 3.1 weights opening tokens most heavily and renders native 48kHz audio alongside video. Lead with shot size, single camera move, and material specificity; anchor spoken dialogue with a colon so it is not rendered as on-screen text. See [`veo3-prompting-guide.md`](veo3-prompting-guide.md) for Visual DNA multi-shot consistency.

### Veo 3.1 Syntax Formula:
```text
[Shot Size & Camera Move], [Lens & Angle], [Subject with Material Texture], [Single Action], [Context & Time], [Visual DNA Lighting & Palette]. Audio: [Ambient/SFX]. [Speaker] speaks [tone]: "[Line]"
```

### Veo 3.1 Production Example:
```text
Medium close-up, slow dolly forward, 35mm lens with shallow depth of field.
A weathered watchmaker with silver stubble and oil-smudged fingertips adjusts a brass gear with steel tweezers inside a dim workshop at dusk.
Warm 3200K desk lamp side-light, lifted blacks, subtle 35mm grain.
Audio: quiet room tone, delicate metallic tweezer click, steady mechanical ticking. Watchmaker speaks softly: "One tooth off, and the whole week drifts."
```

---

## 7. Next-Gen 2026 Models (Seedance 2.5, LTX-2.5, MiniMax H3, Ovi, Wan 2.2)

Complete per-model prompting rules, screenplay formats, `<d>` speech tags, and official reference examples live in [`.claude/skills/video-prompting/SKILL.md`](../../.claude/skills/video-prompting/SKILL.md):
* **Seedance 2.5:** [`references/models/seedance2-5/prompting.md`](../../.claude/skills/video-prompting/references/models/seedance2-5/prompting.md) (4–30s continuous takes, up to 50 `@Image/@Video/@Audio` references, cause-before-reaction beats)
* **LTX-2.5:** [`references/models/ltx2-5/prompting.md`](../../.claude/skills/video-prompting/references/models/ltx2-5/prompting.md) (Single-shot flow, explicit cut transitions, screenplay dialogue, Dub-It speech replacement)
* **MiniMax H3 (Hailuo 3):** [`references/models/minimax-h3/prompting.md`](../../.claude/skills/video-prompting/references/models/minimax-h3/prompting.md) (`integrated_multimodal_description`, `overall_soundscape`, `non_diegetic_music`, and `<d>[English] ... </d>` speech tags)
* **Ovi & Wan 2.2 / Animate 2:** [`references/models/ovi/prompting.md`](../../.claude/skills/video-prompting/references/models/ovi/prompting.md) & [`references/models/wan22/prompting.md`](../../.claude/skills/video-prompting/references/models/wan22/prompting.md)
