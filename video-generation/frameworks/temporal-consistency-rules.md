# Temporal Consistency & Multi-Shot Continuity Rules
### *Maintaining Character Identity and Lighting Across Video Takes*
**Architect:** **Muhammad Nasir Khan**

Maintaining temporal consistency across consecutive video generations requires decoupling character identity from motion dynamics.

---

## 1. The Two-Block Rule for Recurring Characters

To prevent an AI character's facial structure or costume from morphing across shots, split every multi-shot prompt into two explicit blocks:

```text
[IDENTITY BLOCK]:
[Exact Age, Facial Structure, Skin Tone, Hair Color & Cut, Specific Uniform/Attire].
(Keep this block 100% identical word-for-word across Shot 1, Shot 2, and Shot 3).

[MOTION BLOCK]:
[Scene Action, Camera Trajectory, Lighting Modulation, Spatial Progression].
(Vary this block per shot to advance the scene narrative).
```

---

## 2. Motion Bucket / Motion Scale Parameters

Different engines use motion strength sliders:
* **Low Motion (1 – 3 / 20% – 35%)**: Micro-expressions, dialogue close-ups, subtle breathing. Preserves 99% facial fidelity.
* **Medium Motion (4 – 6 / 40% – 60%)**: Natural walking, hand gestures, steady camera tracks.
* **High Motion (7 – 10 / 70% – 100%)**: Running sprints, combat strikes, vehicular high-speed drifts. Prone to minor anatomical deformation if prompt lacks clear anatomical constraints.
