# The MCSLA Prompt Engineering Framework

The **MCSLA Formula** is the industry-standard five-layer architecture for constructing cinematic, stable, and high-fidelity video generation prompts across modern diffusion and autoregressive video models (Kling, Seedance, Runway Gen-3, Sora, Luma Dream Machine, Minimax).

---

## The 5 Layers of MCSLA

Every high-performing prompt is engineered by layering five distinct cinematographic dimensions:

| Layer | Element | Function | What to Specify | Example |
| :---: | :--- | :--- | :--- | :--- |
| **M** | **Model & Runtime** | Engine target & technical parameters | Engine name, aspect ratio, duration, frame rate | `Model: Kling 3.0 | 16:9 | 8s | 30fps` |
| **C** | **Camera** | Optical movement and framing | Named camera preset, travel speed, lens focal length, aperture | `Camera: Slow Dolly In from medium to close-up, 50mm F2.0 lens` |
| **S** | **Subject** | Physical anchor and character state | Observable attire, physical details, posture, micro-expressions | `A weathered detective in a wet trench coat, jaw clenched, eyes scanning` |
| **L** | **Look & Lighting** | Environmental lighting, color grade, and atmosphere | Key/fill ratios, volumetric mood, weather, color palette | `Sodium-vapor amber streetlamp, cold rain reflections, 2.35:1 anamorphic` |
| **A** | **Action & Audio** | Temporal dynamics, secondary motion, and audio cues | Single dominant action, settling beats, spoken dialogue in quotes, sound design | `He lights a match with one hand; wind flickers the flame. Audio: rain on pavement` |

---

## Canonical Prompt Schema

```text
[Subject & Physical Anchors]
[Environment & Atmospheric Setting]
[Dominant Action & Micro-Beats]
Camera: [Named Movement Preset] + [Lens/Framing Details]
Look: [Lighting Scheme] + [Color Grading] + [Texture/Aesthetic]
Audio: [Spoken Dialogue in Quotes] + [Ambient Room Tone] + [Synchronized SFX]
```

### Complete Production Example:

```text
Model: Kling 3.0 | Aspect: 16:9 | Duration: 8s

A seasoned botanist in stained canvas overalls stands inside a moonlit glass greenhouse.
Dense tropical ferns glisten with condensation, mist curling near the flagstone floor.
She reaches out with tweezers to delicately inspect a bioluminescent blue orchid that pulses with faint cold light.
Camera: Slow Dolly In from medium shot to tight insert close-up over 8 seconds. 85mm F1.4 lens, focus plane locked on the flower petals.
Look: Deep midnight blue ambient, soft cool backlight, volumetric light beams slicing through cracked glass panes.
Audio: Distant thunder rumble, quiet drip of water onto leaves, soft metallic click of tweezers.
```

---

## Golden Rules for MCSLA

1. **The First 25 Words Rule**: Video diffusion models give disproportionate attention to the opening tokens. Always place the **Subject** and **Primary Action** within the first 25 words.
2. **The One-Action Principle**: Never ask for multiple competing actions in a single 5–10s clip. Specify one primary action (e.g., *turns around*, *strikes a match*, *sprints down stairs*) and let natural physics handle secondary micro-movements.
3. **Strict Parameter Separation**: Technical parameters (aspect ratio, duration, resolution) belong in the prompt header/UI metadata, not mixed into prose descriptions.
