# Adobe After Effects & Hybrid AI Motion Pipeline

The hybrid workflow pairs generative AI video models (for rich atmospheric background plates, complex particle textures, and dynamic fluid dynamics) with native Adobe After Effects components (for crisp editable typography, vector logos, timing tweaks, and alpha channel compositing).

---

## The Rule of Native Layer Separation

Never attempt to have generative video models render fine text or exact corporate vector logos directly inside the video stream. Video models hallucinate letterforms and introduce motion compression artifacts.

| Layer Type | Execution Engine | Best Practice |
| :--- | :--- | :--- |
| **Atmospheric Plates & Backgrounds** | Generative AI (Kling / Seedance / Runway) | Generate clean video without text, export in ProRes 422 or high-bitrate MP4 |
| **Typography & Titles** | Native After Effects Text Layers | Use vector type with animators (Tracking, Opacity, Position ramp) |
| **Brand Logos & UI Icons** | Native After Effects Shape / Vector Layers | Import SVG/AI vector files; animate with trim paths or 3D transform |
| **VFX Overlays & Dust** | Hybrid (AI Plate + AE Blend Modes) | Composite via `Screen`, `Add`, or `Luma Matte` modes |
| **Audio Stems** | Dedicated DAW / Suno Stems | Keep Music, VO, and SFX on separate timeline audio tracks |

---

## Prompting AI Video for After Effects Compositing

When generating plates destined for AE compositing, instruct the AI model to leave designated negative space for typography:

```text
Model: Kling 3.0 | Aspect: 16:9 | Duration: 8s

A clean, minimalist 3D abstract fluid simulation.
A single ribbon of iridescent liquid glass twists slowly along the right third of the frame.
The left two-thirds of the composition consists of an open, uncluttered, matte dark charcoal space.
Camera: Extremely subtle forward drift along the Z-axis, zero rotation, locked horizon.
Look: Soft studio lighting, realistic chromatic refraction on the glass ribbon edges, deep clean matte shadows on the left.
(Designed specifically as a backdrop plate for left-aligned headline typography).
```
