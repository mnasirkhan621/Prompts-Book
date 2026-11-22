# Audio Frequency Spectrum Allocation Guide
### *EQ Partitioning and Video Dialogue Masking Prevention*
**Architect:** **Muhammad Nasir Khan**

When generating AI music tracks to accompany video dialogue or narration, prompt descriptors and post-EQ must carve out space in the frequency spectrum to prevent vocal masking.

---

## 1. Frequency Band Allocations

| Frequency Range | Musical Elements | Common AI Artifacts | Corrective Prompting / EQ Actions |
| :--- | :--- | :--- | :--- |
| **20 Hz – 60 Hz (Sub-Bass)** | 808 sub, kick drum thud | Muddy rumble, distortion | Use `tight punchy sub-bass` rather than `overdriven 808` |
| **60 Hz – 250 Hz (Bass)** | Bass guitar, low piano resonance | Frequency masking of male voice | High-pass non-bass instruments at 100 Hz |
| **250 Hz – 500 Hz (Low-Mids)** | Body of acoustic guitars, snare body | Boxy, hollow acoustic feel | Dip slightly in DAW: -2.5 dB at 350 Hz |
| **1 kHz – 4 kHz (Speech Presence)** | Primary clarity of human speech | Harsh vocal sibilance in AI stems | In prompt: specify `warm analog mix, subdued upper-mids` |
| **6 kHz – 10 kHz (Treble / Air)** | Cymbals, vocal breathiness | Synthetic digital phase artifacts | Use `smooth vintage tape saturation, gentle high-end roll-off` |
