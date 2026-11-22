# Anti-Slop & Observable Physics Guidelines

Video generation models process physical instructions, spatial measurements, and optical properties. Abstract praise and emotional buzzwords confuse diffusion models, producing generic, over-filtered "AI slop."

---

## The "Sensor / Camera Measurable" Test

Before including any word or phrase in a video prompt, ask:
> **"Can a camera sensor, light meter, or physical microphone measure this?"**

| Unmeasurable Slop (Banned) | Observable Physical Replacement |
| :--- | :--- |
| *Stunning, breathtaking, beautiful* | *Symmetrical bone structure, high cheekbones, natural skin pores under diffused softbox* |
| *Epic cinematic masterpiece* | *2.35:1 anamorphic ratio, shallow depth of field, high dynamic range with deep shadow detail* |
| *Hyper-realistic, photorealistic 8K* | *Fine woven wool texture, visible water droplets beaded on leather, crisp 35mm film grain* |
| *Award-winning cinematography* | *Low-key lighting, single 5600K key light from 45 degrees, subtle atmospheric haze* |
| *Angry / Enraged* | *Forehead veins pulsing, nostrils flaring, rapid irregular breathing, jaw clenched tight* |
| *Sad / Depressed* | *Eyes glassy with unshed tears, shoulders sagging, gaze fixed downwards, slow shallow breath* |
| *Crazy fast motion* | *Subject accelerates across frame at 25 km/h, shutter angle 180 degrees, directional motion blur* |

---

## Decomposing Abstract Emotions

AI models cannot generate "sadness" or "confidence" directly; they generate faces and bodies. Decompose every emotional beat into anatomical cues:

### 1. Anger / Tension / Edge
* **Face:** Knitted eyebrows, tight lips drawn thin, visible pulse in temple or carotid artery.
* **Body:** Rigid posture, white knuckles gripping an object, jerky head turns.
* **Camera Sync:** Slight handheld camera jitter, broken breathing rhythm, tight framing.

### 2. Calm / Command / Authority
* **Face:** Steady unblinking eye contact, neutral relaxed brow, slow deliberate speech cadence.
* **Body:** Minimal wasted movement, upright posture, hands resting still.
* **Camera Sync:** Smooth mechanical dolly, stabilized gimbal track, centered symmetry.

### 3. Vulnerability / Grief
* **Face:** Trembling chin, micro-twitches around the eyelids, corners of mouth drooping.
* **Body:** Slumped shoulders, head tilted down, arms pulled inward protectively.
* **Camera Sync:** Slow pull-back away from the subject ("leaving the character alone"), granting spatial isolation.

### 4. Shock / Realization
* **Face:** Sudden pupil dilation, jaw dropping slightly, sudden stillness after movement.
* **Body:** Complete freeze of all voluntary motion for 1–2 seconds.
* **Camera Sync:** Static camera hold followed by sudden micro push-in or subtle Dolly Zoom.

---

## Eliminating Prompt Clutter

* **No Negative Prompts in Modern Video**: Leading engines (Kling, Seedance, Sora, Luma) do not use negative prompt boxes. Phrase every constraint as a **positive instruction** (*"Rectilinear wide lens with zero barrel distortion"* instead of *"no fisheye, no distortion"*).
* **Word Count Discipline**:
  - **Short-form cinematic prompts**: 40–90 words deliver optimal adherence without prompt degradation.
  - **Complex multi-beat scenes**: 100–180 words maximum, grouped into logical sections.
