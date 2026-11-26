# Viral Script Engineering & Automated Linting
**Architect & Lead Developer:** **Muhammad Nasir Khan**  
**Repository:** Prompts Book | Spoken Script Architecture

---

## 1. High-Retention Narrative Engines (`script` skill)

Great YouTube and short-form scripts read smoothly aloud at **~150 words per minute (WPM)** and sustain viewer curiosity through structural tension rather than hype:

1. **Problem/Fear $\rightarrow$ Tested Reassurance:** Validate a real bottleneck creators face, show concrete failure modes, and resolve with a reproducible solution.
2. **Open Question Early, Payoff Late:** Seed a clear overarching question immediately after the hook (*"So why does Model A drift while Model B holds?"*) and earn the answer chronologically.
3. **Visual Proof Discipline (`[proof: ...]`):** Every factual assertion, metric, or workflow step requires an explicit editor proof cue (generated clip, UI frame, waveform, chart) — never invent statistics.
4. **Mid-Roll Re-Hook Escalation (2:00–3:00 Mark):** On videos exceeding 3 minutes, explicitly signal the upcoming high-stakes payoff early (*"And at the end, the single parameter check that stops frame jitter..."*) and pivot smoothly at the 2-minute window.
5. **Clean Beat Linking:** Transition between sections with causal pivots (**"but"**, **"so"**, **"which means"**) instead of flat chronological chains (**"and then"**).
6. **Editor Cut Boundaries (`---`):** Place horizontal rules between narrative beats so voiceover tightening and HyperFrames shot planning map 1:1 to story segments.

---

## 2. Anti-AI-Tell Voiceover Standard

Audience retention drops immediately when audiences hear generic LLM syntax. Eliminate these structural and lexical patterns from every spoken script:

* **Banned LLM Buzzwords:** *delve, tapestry, testament to, game-changer, revolutionize, unleash, elevate, seamless, cutting-edge, buckle up, let's dive in, embark, landscape, leverage, robust, pivotal, let that sink in.*
* **Banned Binary Cliché (`not X, it's Y`):** Never write *"This isn't just a tool—it's a paradigm shift."* State what the thing actually does.
* **Breathable Ear Sentences:** Keep average spoken lines punchy; split dense 25+ word clauses for natural vocal delivery, varying rhythm with one longer conversational thought per section.
* **8th-Grade Concrete Clarity:** Explain concepts through observable examples rather than dictionary definitions. Cap inline lists at 3 items per section.

---

## 3. Automated Auditing with `script_check.py`

Run every draft through the local retention auditor before stepping up to the microphone:

```bash
# Long-form YouTube script check (default 150 WPM)
python tools-and-workflows/youtube-research/script_check.py my_script.md

# Vertical Short / Reel check (enforces tight <=12 word opener rule)
python tools-and-workflows/youtube-research/script_check.py my_reel.md --short --wpm 160
```

### What `script_check.py` Measures
* **Runtime & Part Pacing Map:** Calculates spoken word count, estimated duration per `## Part ...` / `=== PART ... ===` heading, and where re-hooks land.
* **Weak Opener Failures (`FAIL`):** Flags instant bounce killers (`"Hey guys"`, `"In this video"`, `"Today we're going to"`).
* **Mandatory Outro Match (`FAIL`):** Verifies the script closes cleanly on your locked sign-off line stored in `youtube-studio/brand/outro.txt`.
* **AI-Tell & Rhythm Warnings (`WARN`):** Flags AI-tell phrases, `it's not X, it's Y` syntax, sentences over 25 words, excessive `"and then"` chaining, and missing long-video teases.
* **Claim Verification Prompts (`INFO`):** Highlights numbers, percentages, and dollar claims so you confirm visual `[proof: ...]` backing.
