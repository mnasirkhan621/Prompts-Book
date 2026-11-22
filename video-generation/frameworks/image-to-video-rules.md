# Image-to-Video (I2V) Motion-First Rules

Image-to-Video (I2V) transforms a static reference frame or storyboard panel into dynamic motion. Applying text-to-video prompt strategies to I2V is the #1 cause of generation failure and visual artifacts.

---

## The Prime Law of I2V

> **NEVER re-describe what is already visible in the starting image.**
> **Prompt ONLY for what moves, changes, or catches light.**

When you re-describe static elements already present in the frame (e.g., *"a woman with brown hair and green eyes wearing a blue jacket"*), the model attempts to generate those features from scratch on top of the image, leading to face deformation, duplicate limbs, and texture warping.

---

## Comparison: Weak vs. Strong I2V Prompts

### ❌ Weak (Static Over-Description):
```text
A handsome cybernetic warrior standing in an alleyway with neon signs, wearing armor, looking intense with glowing blue cables in his shoulders.
```
*Why it fails:* The model already sees the warrior, the alley, the armor, and the cables. It has no clear instruction on how time progresses.

### ✅ Strong (Motion-Delta Prompt):
```text
Starting from the provided image as the initial frame.
Rain begins to stream down the surface of his visor. The blue cables in his shoulder pulse with increasing brightness.
He slowly turns his head 30 degrees toward the alley entrance, pupils dilating.
Camera: subtle handheld breathing camera with locked focal distance.
Atmospheric fog rolls slowly across the ground from left to right.
```
*Why it succeeds:* Explains the exact temporal progression, lighting changes, camera stability, and micro-movements.

---

## The 4 Pillars of I2V Motion Prompts

1. **Initial Frame Anchor**:
   Begin your prompt with a clear anchor:
   `"Starting from the provided image as the first frame..."`

2. **Primary Subject Motion**:
   Focus on kinetic shifts:
   - Head/body rotations: *"Turns slowly toward the light source over 4 seconds."*
   - Facial nuance: *"A subtle tightening of the jaw; eyes narrow in recognition."*
   - Hand movements: *"Fingers tap against the steering wheel in steady rhythm."*

3. **Environmental Dynamics (Secondary Motion)**:
   Bring life into the background so the scene doesn't feel frozen:
   - Wind / airflow: *"Breeze catches the curtains, gently rippling the linen fabric."*
   - Fluid / particulate dynamics: *"Cigarette smoke curls upward and disperses into the ceiling shadows."*
   - Light modulation: *"Fluorescent light flickers once at second 3, casting temporary shadows."*

4. **Camera Choreography**:
   Specify a single optical trajectory:
   - *"Camera maintains locked position with subtle optical breathing."*
   - *"Slow push-in toward the subject's right eye, travel distance under 15 cm."*

---

## I2V Reference Sheets & Storyboard Handoffs

When animating a multi-panel storyboard or reference sheet:
* **Isolate the single frame**: Crop and pass only the specific panel to animate as frame 1.
* **Match Motion to Framing**: If frame 1 is an Extreme Close-Up, prompt for micro-expressions, not full-body movement. If frame 1 is a Wide Shot, prioritize spatial travel and environment dynamics.
