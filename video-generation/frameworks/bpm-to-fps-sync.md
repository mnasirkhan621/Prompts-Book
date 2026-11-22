# Audio-to-Video Synchronization: BPM to Frame Math
### *Mathematical Rhythm Engine for Editing Cuts & Motion Pacing*
**Architect:** **Muhammad Nasir Khan**

In professional motion design and commercial video production, cutting video to the music beat is essential. AI video generations (which render at standard frame rates of 24fps, 30fps, or 60fps) must have their action beats and transition holds mathematically synchronized to the track's **Beats Per Minute (BPM)**.

---

## 1. The Core Formula

$$\text{Frames Per Beat} = \frac{\text{FPS} \times 60}{\text{BPM}}$$

* **FPS**: Frame rate of the video project (24fps cinema, 30fps social/standard, 60fps high-speed).
* **BPM**: Music tempo generated via Suno or DAW.

---

## 2. Master BPM-to-Frame Lookup Table

| Music Tempo (BPM) | Common Genre Pairing | Frames per Quarter Note @ 24fps | Frames per Quarter Note @ 30fps | Frames per Quarter Note @ 60fps |
| :---: | :--- | :---: | :---: | :---: |
| **70 BPM** | Lo-Fi, Slow R&B, Heavy Blues | 20.6 frames | 25.7 frames | 51.4 frames |
| **80 BPM** | 90s Boom Bap, Slow Hip-Hop | 18 frames | 22.5 frames | 45 frames |
| **90 BPM** | Mid-tempo Pop, Reggae, Funk | 16 frames | 20 frames | 40 frames |
| **100 BPM** | Pop, Chillout, Modern R&B | 14.4 frames | 18 frames | 36 frames |
| **110 BPM** | Indie Rock, Nu-Disco | 13.1 frames | 16.4 frames | 32.7 frames |
| **120 BPM** | **House, Synthwave, Disco Pop** | **12 frames** | **15 frames** | **30 frames** |
| **124 BPM** | Cyberpunk Synthwave, Deep House | 11.6 frames | 14.5 frames | 29 frames |
| **128 BPM** | **EDM, Festival Electro, Techno** | **11.25 frames** | **14.06 frames** | **28.1 frames** |
| **140 BPM** | **Trap, Dubstep, Fast Rock** | **10.3 frames** | **12.8 frames** | **25.7 frames** |
| **150 BPM** | Hardcore, Phonk, Pop-Punk | 9.6 frames | 12 frames | 24 frames |
| **160 BPM** | Fast Drift Phonk, Drumstep | 9 frames | 11.25 frames | 22.5 frames |
| **174 BPM** | **Drum & Bass, Jungle** | **8.3 frames** | **10.3 frames** | **20.7 frames** |

---

## 3. Editing Cut Windows by Musical Bars

At standard **4/4 time signature**:
* **1 Bar (4 Beats)** = 1 measure of music. Ideal for medium-paced cuts.
* **2 Bars (8 Beats)** = Standard conversational phrase. Ideal for narrative drama.
* **1/2 Bar (2 Beats)** = High-energy cuts for kinetic action and sports montages.
* **1/4 Bar (1 Beat)** = Strobe cuts, punchy match-cuts, and impact hits.

### Standard 120 BPM Cut Intervals (at 30fps):
* **Every 1 Beat**: Cut exactly every **15 frames** (0.5 seconds).
* **Every 2 Beats**: Cut exactly every **30 frames** (1.0 second).
* **Every 4 Beats (1 Bar)**: Cut exactly every **60 frames** (2.0 seconds).
* **Every 8 Beats (2 Bars)**: Cut exactly every **120 frames** (4.0 seconds).

---

## 4. Prompting Video Action to Sync with Music Hits

When authoring a video prompt destined to align with a musical impact or drop:

### Synchronized Action Formula:
```text
At second [Calculated Timestamp], [Impact Action occurs precisely on the beat].
Camera: [Camera Move] decelerates and hard-freezes at second [Timestamp] on the bass hit.
```

### Production Example (120 BPM Drop at Second 4.0):
```text
Model: Kling 3.0 | Aspect: 16:9 | Duration: 6s | FPS: 30

A robotic warrior dashes through a neon alley from 0.0s to 3.9s.
At exactly second 4.0 (Beat 8 / Bar 2 at 120 BPM), he lands a crushing ground slam.
A radial shockwave of shattered pavement and blue energy erupts on impact.
Camera: Action Run low behind him, snapping to a frozen Dutch angle at second 4.0.
```
