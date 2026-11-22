# Storyboard Sheets & Timed Beat Sheets

Professional video creation follows a disciplined pre-production flow: **Brief → Timed Beat Sheet → Storyboard Contact Sheet → Video Render**. Generating individual random scenes without a storyboard blueprint leads to continuity breakdown.

---

## 1. Timed Beat Sheet Blueprint

Before generating video prompts, break the duration into discrete chronological beats:

| Beat # | Time Code | Framing / Angle | Dominant Action & Transition | On-Screen Copy / Voiceover | Sound Design Cue |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **01** | `0.0s – 2.0s` | EWS / Establishing | Hook: Fast push-in across stormy landscape toward fortress | "In a world of noise..." | Ominous sub-bass riser |
| **02** | `2.0s – 4.5s` | MCU / Eye-Level | Hero: Operative turns to camera, visor lights engage | "One signal cuts through." | Electronic servo boot chime |
| **03** | `4.5s – 7.0s` | ECU / 100mm Macro | Feature: Micro-circuitry ignites with golden pulse | "Precision redefined." | High-frequency hum |
| **04** | `7.0s – 8.5s` | Dynamic 360 Orbit | Climax: Energy burst propels hero into vertical flight | *No VO (Music peak)* | Heavy sonic boom impact |
| **05** | `8.5s – 10.0s` | Centered Locked Hold | Resolution: Complete stillness, stark brand reveal | "AETHER. Available Now." | Clean resonant bell chime |

---

## 2. Generating a Storyboard Sheet with AI Images

To maintain 100% visual and stylistic consistency across frames, generate **a single multi-panel storyboard grid sheet** in one image generation call (e.g., GPT Image 2, Midjourney v6/v7, or Flux) rather than generating disconnected individual images.

### Storyboard Grid Prompt Formula:

```text
A professional cinematic storyboard sheet featuring a 6-panel grid layout (2 rows of 3 panels), 16:9 aspect ratio per panel.
Each panel is clearly numbered "Frame 1" to "Frame 6" with thin clean dark borders between frames.
Unified visual style across all frames: [Style, Color Palette, Character Appearance].
Panel 1: [Beat 1 description, camera angle, action].
Panel 2: [Beat 2 description, camera angle, action].
Panel 3: [Beat 3 description, camera angle, action].
Panel 4: [Beat 4 description, camera angle, action].
Panel 5: [Beat 5 description, camera angle, action].
Panel 6: [Beat 6 description, final logo lockup].
Production notes and camera directions annotated cleanly outside the bottom of each frame.
```
