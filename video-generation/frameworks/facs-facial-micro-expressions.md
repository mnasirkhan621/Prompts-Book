# FACS: Facial Action Coding System for AI Video Generation
**Architect & Chief Engineer:** Muhammad Nasir Khan  
**Repository:** Prompts Book | Universal AI Cinematography System  
**Standard:** Anatomical Micro-Performance & Muscle-Level Video Direction

---

## 1. Executive Summary: Why Mood Labels Fail

When directing human actors in AI video generation (Seedance 2.0/2.5, Kling 4.0, Runway Gen-3, Hailuo MiniMax), prompting abstract emotional labels produces generic, lifeless caricature:

```
❌ NAIVE PROMPT:   "A woman looks sad and then smiles happily at the camera."
   RESULT:         Exaggerated cartoonish grimace followed by an eerie, plastic stock-photo grin.

✅ FACS PROMPT:    "Close-up, 85mm. Character exhibits AU1+AU4 inner brow elevation and AU15 lip corner depression, transitioning at 0:03 into an asymmetric AU12 lip-corner pull with absence of AU6 eye crinkling, creating a forced, fragile social smile."
   RESULT:         Authentic, psychologically nuanced micro-performance with subtle epidermal tension.
```

The **Facial Action Coding System (FACS)**, developed by Paul Ekman and Wallace V. Friesen, decomposes human facial movement into discrete anatomical **Action Units (AUs)** corresponding to specific muscular contractions. Leading video diffusion architectures parse AU codes and physiological muscle descriptions with dramatically higher fidelity than emotional adjectives.

---

## 2. Master Action Unit (AU) Reference Table

| AU Code | Anatomical Muscle | Visible Physical Manifestation | Cinematic & Psychological Utility |
| :--- | :--- | :--- | :--- |
| **AU 1** | *Frontalis, pars medialis* | Inner corners of the eyebrows pull upward. | Vulnerability, despair, pleading, profound empathy. |
| **AU 2** | *Frontalis, pars lateralis* | Outer edges of the eyebrows lift upward. | Incredulity, surprise, questioning, skepticism. |
| **AU 4** | *Corrugator supercilii / Depressor* | Eyebrows draw down and pull tightly together. | Concentration, rage, severe cognitive strain, grief. |
| **AU 5** | *Levator palpebrae superioris* | Upper eyelids widen, exposing upper sclera (whites). | Terror, sudden shock, manic fixation, hyper-alertness. |
| **AU 6** | *Orbicularis oculi, pars orbitalis* | Cheeks elevate; skin crinkles into outer crow's feet. | **The authenticity marker**: genuine joy, visceral pain. |
| **AU 7** | *Orbicularis oculi, pars palpebralis* | Lower eyelids tighten and narrow the ocular aperture. | Suspicion, predatory focus, intense scrutiny, doubt. |
| **AU 9** | *Levator labii superioris alaeque nasi* | Nasal bridge wrinkles, upper lip pulls slightly up. | Physical disgust, visceral revulsion, foul odor. |
| **AU 10** | *Levator labii superioris* | Center of upper lip pulls upward, baring teeth. | Moral contempt, snarl, superior disdain, hostility. |
| **AU 12** | *Zygomaticus major* | Lip corners pull diagonally upward toward cheekbones. | Smiling, amusement, social appeasement, masking. |
| **AU 14** | *Buccinator* | Lip corner compresses and tightens into subtle dimple. | Contempt, smirking arrogance, unilateral skepticism. |
| **AU 15** | *Depressor anguli oris* | Corners of the mouth pull downward into frown. | Grief, dejection, despondency, suppressed crying. |
| **AU 17** | *Mentalis* | Chin skin puckers and pushes lower lip upward. | Doubt, holding back tears, childish defiance, petulance. |
| **AU 20** | *Risorius / Platysma* | Lips stretch laterally and horizontally backward. | Abject panic, shrieking terror, excruciating agony. |
| **AU 23** | *Orbicularis oris* | Vermilion borders of lips tighten and thin out. | Anger control, frustration, biting back a harsh reply. |
| **AU 24** | *Orbicularis oris* | Lips press firmly together into a flat horizontal line. | Determination, secret-keeping, suppressed emotion. |
| **AU 26** | *Masseter relaxation* | Mandible drops downward naturally; teeth separate. | Awe, slack-jawed shock, exhaustion, numbness. |

---

## 3. The Duchenne Marker: Distinguishing Genuine vs. Masked Emotion

In cinematic storytelling, the most powerful performances stem from **conflicted characters whose exterior masks their interior turmoil**. FACS allows you to program this tension mechanically.

```
+---------------------------------------------------------------------------------------+
|                              THE DUCHENNE JOY EQUATION                                |
+---------------------------------------------------------------------------------------+
|  GENUINE DUCHENNE JOY  =  AU 6 (Cheek Raiser / Crow's Feet) + AU 12 (Lip Corner Pull) |
|  FORCED / MASKED SMILE =  AU 12 (Lip Corner Pull) ALONE [AU 6 is completely absent]  |
+---------------------------------------------------------------------------------------+
```

### Prompting the Uncanny / Psychopathic Smile
When an antagonist smiles without warmth, prompt the omission of AU 6 and the activation of unblinking gaze:
```
"Tight close-up, 100mm macro lens. Character performs an isolated AU12 lip-corner pull while ocular muscles remain completely frozen (AU6 absent); unblinking eyelids, cold predator gaze, jaw locked."
```

---

## 4. Master Emotional Recipes (FACS Formulas)

### 4.1 Suppressed Agony / Holding Back Tears
- **Anatomical Formula:** `AU 1 + AU 4 + AU 15 + AU 17 + AU 24`
- **Physical Manifestation:** Inner brows knit sharply upward into an inverted V; chin skin dimples as mentalis fires; lips press tightly together to prevent trembling; watery meniscus forms on lower eyelid.
- **Production Prompt:**
  ```
  "Extreme close-up, 85mm prime at f/1.4. Subject displays AU1 inner brow elevation paired with AU4 brow knit. AU17 chin raiser puckers the chin pad while AU24 presses lips into a tight bloodless seam. Tremor in the throat, glistening tear film on lower lash line without overflowing."
  ```

### 4.2 Cold Calculation / Strategic Scrutiny
- **Anatomical Formula:** `AU 7 + AU 23 + subtle head tilt (15 degrees)`
- **Physical Manifestation:** Lower eyelids narrow by 30%, eyes focus on a single focal plane across the room; lips tighten without parting; carotid pulse visible at neck.
- **Production Prompt:**
  ```
  "Medium close-up, 50mm anamorphic. Detective observes suspect: AU7 lower eyelid tightening, unblinking fixation, AU23 subtle lip border compression. Minimal facial micro-movement, zero breathing disturbance."
  ```

### 4.3 Visceral Horror / Immediate Threat
- **Anatomical Formula:** `AU 1 + AU 2 + AU 4 + AU 5 + AU 20 + AU 26`
- **Physical Manifestation:** Eyebrows hoisted high and pulled together into horizontal forehead furrows; upper lids retract exposing full whites; mouth stretches horizontally and drops open.
- **Production Prompt:**
  ```
  "Over-the-shoulder medium shot. Character turns toward doorway: rapid onset of AU1+AU2+AU4 brow hoist, AU5 eyelid retraction exposing white sclera above irises, AU20 lateral mouth stretch and AU26 jaw slack. Rapid thoracic breathing."
  ```

### 4.4 Bitter Contempt / Asymmetric Dismissal
- **Anatomical Formula:** `Unilateral AU 14 + AU 10 + AU 7`
- **Physical Manifestation:** Single corner of the mouth pulls tightly inward with a small dimple; nostrils flare slightly on one side; eyes narrow cynically.
- **Production Prompt:**
  ```
  "Low-angle close-up. Antagonist reacts to defense argument: unilateral AU14 dimple on right cheek, slight right AU10 upper lip curl exposing canine tooth, AU7 eyelid squint. Slow deliberate head shake."
  ```

---

## 5. Temporal Micro-Beat Choreography in Dialogue

In high-end video generation (Kling 4.0, Seedance 2.0), facial performance must evolve across time codes. Do not prompt a static face; choreograph the **micro-beat lifecycle**:

```
[0.0s - 1.5s]  BASELINE (NEUTRAL TENSION)
               - Relaxed ocular aperture, natural resting jaw posture.
               - Gentle involuntary blink at 0.8s.

[1.5s - 3.2s]  MICRO-EXPRESSION INCEPTION
               - Involuntary onset of AU4 (inner brow furrow) + AU17 (chin bunch).
               - 0.3s micro-swallow visible in anterior neck tendons.

[3.2s - 5.0s]  SOCIAL OVERRIDE / SUPPRESSION
               - Subject forces AU12 smile to mask distress; AU6 fails to fire.
               - Gaze averts 10 degrees down-right before returning to lens.
```

---

## 6. Model Compatibility Matrix for FACS Prompting

| AI Video Model | FACS Code Parsing (`AU12`) | Anatomical Text (`cheek raiser`) | Recommended Prompting Dialect |
| :--- | :--- | :--- | :--- |
| **Higgsfield Seedance 2.0 / 2.5** | **Excellent (95%)** | **Excellent (98%)** | Hybrid: `"AU12 (lip corner pull) + AU6 (cheek raiser)"` |
| **Kling AI 4.0 / 1.5** | **Good (85%)** | **Very High (95%)** | Descriptive Anatomical: `"lips pull upward into smile, eyes crinkle at crow's feet"` |
| **Hailuo AI / MiniMax** | **Moderate (70%)** | **Superior (99%)** | Physical Action: `"tightens lower eyelids, furrows inner brow, clamps jaw shut"` |
| **Runway Gen-3 Alpha** | **Good (80%)** | **Very High (92%)** | Mixed: `"micro-expression of brow lowering AU4, clenched jaw"` |
| **Wan 2.1 / CogVideoX** | **Moderate (65%)** | **High (90%)** | Physical Action: `"eyes widen in sudden shock, mouth drops open"` |
