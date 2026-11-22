# Character Consistency & Multi-Shot Soul ID Standard
**Architect & Chief Engineer:** Muhammad Nasir Khan  
**Repository:** Prompts Book | Universal AI Cinematography System  
**Standard:** Temporal Identity Preservation & Multi-Model Character Anchoring

---

## 1. Executive Summary

The #1 operational failure in AI narrative filmmaking is **Character Face Drift**—the phenomenon where a protagonist’s bone structure, ethnicity, age, or clothing mutates between cuts. 

This guide codifies the **Universal Soul ID Protocol**, standardizing identity management across **Higgsfield Soul 2.0 / Cinema Studio**, **Kling 4.0 Omni-Reference (`@Image1`/`@Image2`)**, **Runway Gen-3 Actor Mode**, and **Midjourney `--cref`**.

```
+---------------------------------------------------------------------------------------+
|                       THE DUAL-BLOCK SEPARATION LAW (HARD RULE)                       |
+---------------------------------------------------------------------------------------+
|  IDENTITY BLOCK (Static) --> Bone structure, eye geometry, hairline, scars, wardrobe |
|                              [ZERO camera, ZERO verbs, ZERO temporal changes]        |
|  -----------------------------------------------------------------------------------  |
|  MOTION BLOCK (Dynamic)   --> Camera movement, action choreography, FACS facial cues  |
|                              [ZERO face re-descriptions, ZERO wardrobe re-listing]    |
+---------------------------------------------------------------------------------------+
```

---

## 2. The Single-Prompt 6-Panel Character Sheet (3x2 Grid)

Before generating motion clips, creators must anchor an immutable multi-angle identity plate. Generating single images sequentially causes progressive drift; instead, generate an all-in-one **3x2 six-panel character turn-around sheet** in a single generation at 16:9 ratio.

### 2.1 The Master 6-Panel Sheet Template
```
3x2 grid character reference sheet, neutral 18% neutral grey photographic studio background, flat even softbox lighting, zero colored rim light, zero artistic post-processing.
[Panel 1: Frontal portrait, eye-level, neutral resting expression]
[Panel 2: Three-quarter left portrait, subtle head turn 30 degrees]
[Panel 3: Three-quarter right portrait, subtle head turn 30 degrees]
[Panel 4: Left side profile, 90-degree ear-to-nose plane]
[Panel 5: Full-length body standing pose, natural posture, clean footwear]
[Panel 6: Dynamic action pose, torso twist, walking stride]
Subject: [Character Name], 32-year-old Scandinavian male, high cheekbones, rugged jawline, short textured ash-brown hair, steel-grey eyes, faint linear scar along left eyebrow arch, wearing matte charcoal utilitarian jacket over washed cotton henley. Biological realism, photographic skin pores, no digital airbrushing.
```

---

## 3. The 10-Attribute Character Anchor Block

When executing recurring shots in complex narrative pipelines, bind the character through these 10 parameters:

1. **Identity Tag:** Unique identifier (e.g., `Soul ID [SubjectAlpha]` or `@Image1`).
2. **Screen Position:** Coordinate quadrant (e.g., *Rule of thirds left intersection*).
3. **Depth Layer:** Foreground, midground, background plane.
4. **Frame Occupancy:** Percentage of vertical screen height occupied by subject (e.g., *65% vertical frame*).
5. **Body Orientation:** Cardinal staging (e.g., *Facing 45 degrees camera-right*).
6. **Pose / Stance:** Weight distribution (e.g., *Weight on rear foot, shoulders back*).
7. **Gaze Vector:** Focus target (e.g., *Eye contact 10 degrees above lens*).
8. **Contact Points:** Tactile interactions (e.g., *Left hand gripping steering wheel, right hand hovering over gear shifter*).
9. **State Lock:** Temporal wear condition (e.g., *Wet rain streaks across shoulders, grease smudge on right collar*).
10. **Facial Expression (FACS):** Active muscular tension (e.g., *AU4 brow furrow, AU24 lip compression*).

---

## 4. Multi-Model Implementation Dialects

### 4.1 Higgsfield Soul ID Workflow
- Generate hero face using **Soul Cinema** or **Soul 2.0**.
- Lock face via **Soul ID** database assignment.
- Structure prompt strictly using the Identity-Motion split:
  ```
  [Identity]: Using Soul ID [AlphaHero].
  [Motion]: Character sits inside subway carriage as fluorescent lights flicker overhead. Camera Dolly In slowly toward his face over 5 seconds. Cool cyan color grading, 16:9, 24fps.
  ```

### 4.2 Kling 4.0 Omni-Reference Syntax
In Kling 4.0, pass the reference character sheet as `@Image1` and the background environment as `@Image2`:
```
@Image1 defines the character design. Preserve his facial structure, haircut, and charcoal jacket exactly.
@Image2 defines the scene background. Preserve its architectural geometry and lighting.
The character in @Image1 enters from frame left, walks toward the desk, and places the briefcase down. Smooth lateral tracking shot, locked horizon.
```

### 4.3 Runway Gen-3 Alpha Actor Mode
In Runway Gen-3, pass the actor anchor image to the Actor slot:
```
Actor anchor locked. Medium shot, eye level. The subject turns slowly from the frosted glass window to face the camera, maintaining calm stoic expression with subtle jaw clench. Warm interior key light, cold rain outside.
```

---

## 5. Preventing Costume & Damage Drift (Multi-Form State Tracking)

When a character undergoes narrative progression (e.g., clean suit $\rightarrow$ torn suit $\rightarrow$ battle-damaged armor), **never rely on text prompts alone to alter the costume while preserving the face**.

### The Split-Panel Mannequin Protocol
Generate an intermediary reference plate before the scene:
- **Left Half (Ghost Mannequin):** Flat photograph of the new wardrobe / damage state on a neutral mannequin.
- **Right Half (Identity Face):** Exact crop of the approved character portrait with the explicit command:
  ```
  "Combine face and skull structure from RIGHT panel 100% identically with the damaged tactical wardrobe from LEFT panel. Output single unified full-body reference image."
  ```
- Store this new render as `Character_State_02_Damaged` and invoke it for that act.
