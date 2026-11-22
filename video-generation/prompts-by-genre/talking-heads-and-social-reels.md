# Talking Heads, AI Presenters & Social Reels
### *Character Consistency, Scroll-Stopping Hooks, and Lipsync Production Rules*
**Architect:** **Muhammad Nasir Khan**

Generating photorealistic talking heads and founder video clips for Instagram Reels, YouTube Shorts, and TikTok requires strict facial anchor controls and temporal pacing to prevent facial drift and audio sync delays.

---

## 1. The 6-Part Talking Head Prompt Formula

To keep an avatar or presenter's bone structure and facial likeness identical across multi-take recordings:

$$\text{[Reference Anchor]} + \text{[Granular Emotion]} + \text{[Camera & Framing]} + \text{[Wardrobe]} + \text{[Setting]} + \text{[Performance Framework]}$$

### Anatomy Breakdown:
1. **Reference Anchor / Soul ID**: Explicitly cite the reference asset (`[Reference: face-01.png]`) or provide exact facial bone structure metrics.
2. **Granular Emotion**: Never use generic words like "happy" or "serious." Describe micro-muscles: *"subtle confident smirk, relaxed brow, steady direct eye contact"*.
3. **Camera & Framing**: Vertical `9:16` layout, centered eye-level framing, subtle 50mm or 85mm optical compression.
4. **Wardrobe**: Specific tactile clothing: *"matte black crewneck sweater, rolled sleeves, silver ring on left thumb"*.
5. **Setting & Lighting**: Clean modern studio or blurred office bokeh: *"5600K key softbox from 45 degrees, soft background bokeh blur, subtle warm rim light"*.
6. **Performance & Dialogue Framework**: Spoken dialogue enclosed in quotes for lipsync synchronization.

---

## 2. Scroll-Stopping Hook Mechanics (The First 2 Seconds)

On vertical platforms (TikTok, Reels, Shorts), the first 2 seconds decide retention. Pair an aggressive optical move with dialogue delivery:

### The Crash-Zoom Hook Template:
```text
Model: Kling 3.0 / Seedance 2.0 | Aspect: 9:16 | Duration: 6s | FPS: 30

Vertical 9:16 POV talking-head clip of [Reference: presenter-01.png].
At second 0.0, the presenter speaks directly to camera: "Stop scrolling — this changes everything."
Camera: Rapid Crash Zoom In on the first word from Medium Shot to tight Close-Up, instantly stabilizing at second 1.2.
Look: Punchy creator studio lighting, vibrant warm key light, dark minimalist studio background with subtle neon teal edge rim.
Audio: Spoken dialogue clear and dry, punchy sub-bass hit synchronized exactly with the crash zoom impact.
```

---

## 3. Multi-Cut Founder Consistency: Identity Block vs. Motion Block

When building multi-shot founder or explainer videos, split your generation instructions into two distinct blocks:

```text
[IDENTITY BLOCK - FIXED ACROSS ALL SHOTS]:
A 32-year-old male founder with short dark tapered hair, trimmed beard, sharp brown eyes, wearing a charcoal wool crewneck sweater.

[MOTION BLOCK - SHOT 1]:
Looks directly into lens, nodding slightly as he begins explaining: "Here is the breakdown."
Camera: Eye-level Medium Close-Up, locked-off static framing.

[MOTION BLOCK - SHOT 2]:
Turns slightly to screen-right, gesturing with his right hand open toward a floating graphic, then returns gaze to camera.
Camera: Smooth 50mm F2.0 push-in over 5 seconds.
```

---

## 4. The 8-Second Lipsync Threshold Rule

* **Sub-8 Seconds (Optimal)**: AI lipsync and facial coherence remain 99% locked when clips are kept under 8 seconds.
* **Over 10 Seconds (Degradation Zone)**: Audio sync drift, blinking anomalies, and unnatural micro-twitching increase noticeably beyond 8–10 seconds.
* **Production Best Practice**: Record longer scripts in **4-to-7 second punchy modular beats**, then edit them together with B-roll cutaways.
