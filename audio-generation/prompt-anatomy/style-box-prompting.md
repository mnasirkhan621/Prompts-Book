# Style Prompt Box Optimization & Character Limits

The **Style of Music** box in Suno AI is the primary steering wheel for audio generation. Navigating its limits and training patterns is essential for consistent generation.

---

## Character Limit Rules

* **Hard Character Limit**: **950 characters** (characters beyond 950 are silently truncated by Suno).
* **Optimal Prompt Sweet Spot**: **120 – 350 characters**.
* **Why Shorter Often Wins**: Over-stacking dozens of contradictory genre tags causes **"prompt fatigue"**, forcing the model to average everything out into bland, generic pop.

---

## Strategic Tag Rules

### 1. The Two-Genre Maximum Rule
Combine at most **two primary genres** in a single prompt (e.g., *synthwave + industrial* or *afrobeats + neo-soul*). Stacking three or more conflicting genres (e.g., *country metal jazz edm*) confuses the style-mesh network.

### 2. Comma-Separated Priority Ordering
Suno weights tokens from left to right. Place your absolute must-have elements at the beginning of the prompt:
* **Position 1 (Left):** Primary Genre & Era (`1990s grunge rock, ...`)
* **Position 2 (Middle):** Key Instruments & Mood (`distorted telecaster, heavy fuzz bass, brooding, ...`)
* **Position 3 (Right):** Production details, BPM, and Key (`dry room mix, BPM: 116, Key: E Minor`)

### 3. Language Rule
Always write your **Style Prompt in English**, even if your song lyrics are in Spanish, Japanese, French, or Russian. Suno's acoustic genre embeddings were indexed primarily on English descriptive terms.
