# Lens, Aperture & Optical Framing Guide

Specifying physical lens parameters and optical characteristics grounds the video generation engine in real-world physics, controlling depth of field, perspective compression, and spatial geometry.

---

## Lens Selection by Shot Purpose

| Shot Purpose | Recommended Focal Length | Field of View (FOV) | Recommended Aperture | Optical Result |
| :--- | :--- | :--- | :--- | :--- |
| **Tight Emotional Close-Up** | 85mm or 100mm | 29° – 24° | F1.4 – F1.8 | Extreme shallow depth of field, creamy background blur (bokeh), flattering facial compression |
| **Dialogue & Two-Shot** | 50mm | 47° | F2.0 – F2.8 | Natural human perspective, realistic spatial proportions between foreground and background |
| **Establishing & Wide Landscape** | 24mm or 35mm | 84° – 63° | F4.0 – F8.0 | Deep depth of field, vast environmental context, architectural scale |
| **Macro / Fine Detail** | 100mm Macro | 24° | F2.8 – F4.0 | Razor-thin focus plane, extreme magnification of textures, pores, and droplets |
| **Action & Dynamic Motion** | 28mm Anamorphic | 75° | F2.8 | Horizontal lens flares, wide cinematic scope, subtle edge falloff without fisheye warp |

---

## Optical Clauses for Production Prompts

To lock optical stability and prevent AI lens hallucinations, append these standard clauses to your prompts:

### 1. The Focus-Lock Clause (For Close-ups & Inserts)
Prevents autofocus hunting, unnatural breathing, or sudden blur shifts:
```text
"Focus plane locked strictly on [subject/object] from first frame to last — zero focus hunting, zero rack focus."
```

### 2. The Rectilinear Integrity Clause (For Wide Lenses)
Prevents wide lenses (24mm–35mm) from curving into unwanted fisheye or barrel distortion:
```text
"Straight rectilinear lines, natural architectural geometry, zero barrel distortion, zero wide-angle warp."
```

### 3. The Anamorphic Look Clause
Creates authentic Hollywood wide-screen texture:
```text
"2.35:1 anamorphic format, oval bokeh highlights, subtle horizontal blue lens flares, gentle vintage edge falloff."
```

---

## Shot Size Reference

| Code | Shot Type | Subject Framing | Primary Function |
| :---: | :--- | :--- | :--- |
| **EWS** | Extreme Wide Shot | Subject tiny or invisible | Geography, isolation, world-building |
| **WS** | Wide Shot | Full body head-to-toe with head room | Character in context, spatial orientation |
| **MLS** | Cowboy / Medium Long Shot | Mid-thigh to top of head | Standoffs, physical readiness, holster action |
| **MS** | Medium Shot | Waist to top of head | Standard conversational narrative, active hand gestures |
| **MCU** | Medium Close-Up | Mid-chest to top of head | Emotionally engaged dialogue, clear eye reactions |
| **CU** | Close-Up | Chin to hairline fills frame | High emotional stakes, dramatic revelations |
| **ECU** | Extreme Close-Up | A single feature (iris, lips, fingernail) | Sensory intensity, tension peaks, micro-details |
