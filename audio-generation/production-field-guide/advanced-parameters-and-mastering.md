# Advanced Suno Parameters & Audio Mastering

Getting studio-grade audio fidelity out of AI music generators requires optimizing generation settings and applying targeted post-production mastering.

---

## 1. Dialing in Tempo & Key Locks

Suno adheres remarkably well to explicit BPM and Key notation when formatted correctly:

* **BPM Notation:** Always format with prefix: `BPM: 124` or `124 BPM`.
* **Key Notation:** Always specify Mode: `Key: C# Minor` or `Key: F Major`.
* **Tempo Selection Guide:**
  - `65 – 85 BPM`: Lo-Fi, Slow R&B, Cinematic Ambient, Doom Metal
  - `90 – 110 BPM`: Boom Bap Hip-Hop, Indie Pop, Mid-tempo Funk
  - `120 – 130 BPM`: House, Synthwave, Disco, Pop, Modern Rock
  - `140 – 160 BPM`: Trap, Dubstep, Drum & Bass (Half-time), Pop Punk
  - `170 – 180 BPM`: Drum & Bass, Jungle, Thrash Metal

---

## 2. Production Aesthetic Descriptors

Use these high-fidelity studio descriptors in your Style Prompt to control the acoustic mix:

| Mix Objective | Production Tags to Use |
| :--- | :--- |
| **Warm Vintage Vinyl** | `warm analog tape saturation, subtle vinyl crackle, rounded low-end, 1970s studio console` |
| **Punchy Modern Streaming Master** | `crisp modern mastering, punchy transient drums, sidechain compression, ultra-wide stereo image` |
| **Lo-Fi Bedroom Vibe** | `lo-fi cassette flutter, detuned chorus, muted highs, boxy room reverb, intimate dry vocal` |
| **Massive Stadium Anthem** | `huge arena reverb, wall of sound, massive sub-bass, towering stacked vocal layers` |
| **Intimate Acoustic Room** | `dry close-mic recording, natural wooden room acoustics, zero digital reverb, tactile pick noise` |

---

## 3. Post-Generation Stems & Mastering Chain

When exporting finished Suno audio for use in video projects:

1. **Stem Separation**:
   Export stems (Vocals and Instrumental backing track separately) using Suno's built-in stem splitter or external tools (Demucs / UVR5).
2. **Subtractive EQ**:
   - Apply a high-pass filter at `30 Hz` to remove sub-audible mud.
   - Dip between `250 Hz – 400 Hz` to clean up AI vocal "boxiness".
   - Dip slightly around `3.5 kHz – 4.5 kHz` if AI high-frequency sibilance sounds harsh.
3. **Dynamic Control (Sidechaining to Video VO)**:
   When mixing Suno music underneath video dialogue or voiceover, route the voiceover track to sidechain compress the music track by `2.5 dB – 4 dB` at 1 kHz–3 kHz whenever dialogue occurs.
