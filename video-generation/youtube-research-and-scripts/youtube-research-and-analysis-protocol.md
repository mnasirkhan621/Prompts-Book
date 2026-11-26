# YouTube Research, Outlier Detection & Visual Breakdown Protocol
**Architect & Lead Developer:** **Muhammad Nasir Khan**  
**Repository:** Prompts Book | Pre-Production Intelligence Engine

---

## 1. The Cardinal Rule: Watch Frames, Not Just Transcripts

Evaluating viral videos solely by reading their text transcripts misses 70% of what holds viewer retention: **cut frequency, visual proof timing, camera framing shifts, B-roll density, and on-screen typography**.

Our research pipeline enforces multimodal analysis via [`yt.py`](../../tools-and-workflows/youtube-research/yt.py) and [`reel_fetch.py`](../../tools-and-workflows/youtube-research/reel_fetch.py), writing all media locally into [`youtube-studio/research/`](../../youtube-studio/research/) (excluded from Git).

```text
Video URL ──▶ yt.py watch ──▶ <=480p MP4 + Transcript + Frames (2s) + 4x3 Contact Sheets
                                      │
                                      ▼
                       Line-by-Line Multimodal Sync:
         [Timestamp] | [Spoken Hook/Beat] | [Visual Cut/Framing] | [Retention Mechanism]
```

---

## 2. Mathematical Outlier & Breakout Scoring

Raw view counts mislead creators when comparing channels of wildly different subscriber bases. Instead, measure **Outlier Velocity** relative to each channel's own baseline:

### 2.1 Outlier Multiplier Formula (`outlier-pulse` / `channel-analysis`)
$$\text{Outlier Score} = \frac{\text{Video Views}}{\text{Channel Median Views (Window)}}$$

* **Baseline Window:** Default `60 days` for your own channel, `90–120 days` for competitor channels.
* **Winner Threshold:** Videos scoring $\ge 2.0\times$ median (or $\ge 1.5\times$ / $\ge 25\text{K}$ views in weekly competitor scans).
* **Views Per Hour (VPH):** $\frac{\text{Views}}{\text{Hours Since Publish}}$ identifies active algorithmic momentum on videos under 7 days old.
* **Discovery Ratio (`yt.py search`):** Ranks non-subscribed search results by **Views-to-Subscriber Ratio** ($\frac{\text{Views}}{\text{Subs}}$) to spot breakout topics from small channels.

### 2.2 Breakout Inflection Detection (`breakout-detector`)
To pinpoint the exact upload where a dormant or linear channel experienced exponential growth:
1. Scan `730 days` of upload history (`--days 730 --max 500 --json`).
2. Sort chronologically and calculate a **rolling median of the preceding 5–10 uploads**.
3. Flag inflection videos achieving $\ge 3.0\times$ rolling median **where subsequent uploads hold a permanently elevated floor**.
4. Compare the breakout upload against its 5 predecessors across 6 dimensions: **Topic Timing**, **Title Packaging**, **Thumbnail Focal Contrast**, **Video Length**, **First-20s Transcript Hook**, and **Visual Format**.

---

## 3. Multimodal Breakdown Checklist (`analyse` & `video-breakdown`)

When studying any winning video or short-form Reel (`study` skill), audit these 6 layers without inventing unverified metrics:

1. **Transcript Integrity:** Capture exact spoken words in original language with timestamps `[0:00]`.
2. **On-Screen Hook Text (0:00–0:03):** Inspect frames `0001`–`0003` to verify whether visual text complements rather than duplicates the spoken line.
3. **Editing Cadence:** Measure cuts per 10 seconds, caption styling, zoom keyframes, and clean vs. overlaid B-roll intervals.
4. **Structural Arc:** Timestamp Hook $\rightarrow$ Setup $\rightarrow$ Re-hook / Mid-video Escalation $\rightarrow$ Payoff $\rightarrow$ CTA.
5. **Comment Sentiment Audit (`yt.py comments`):** Extract top comments to discover which moments viewers quoted, debated, or felt emotionally anchored to.
6. **Clean Adaptation Rule:** Extract structural mechanisms and pacing blueprints—**never copy competitor phrasing or redistribute third-party clips**. Recreate visual proof cleanly via AI generation or original screen captures.
