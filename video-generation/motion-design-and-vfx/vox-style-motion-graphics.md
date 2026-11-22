# Vox-Style Editorial Motion Graphics & Paper Dioramas
### *Mixed-Media Paper Collage, Data Explainer, and Historical Diorama Prompts*
**Architect:** **Muhammad Nasir Khan**

Vox-style motion graphics combine mixed-media hand-cut paper collages, archival photography, halftone print dots, and bold kinetic typography with deliberate 2.5D parallax motion.

---

## 1. The 5-Part Keyframe Image Prompt Formula

Every scene in a Vox-style explainer begins by generating a static high-contrast paper collage keyframe (via Flux Dev, Seedream, or Midjourney v6) before animating it:

```text
[1 STYLE BLOCK]:
Mixed-media hand-cut paper collage, editorial zine style. Torn paper edges, scissor-cut borders, tape corners, halftone print dot patterns, paper drop shadows. Figures are printed-texture cut-outs from vintage photography or woodblocks. NOT 3D, NOT CGI. Visible paper grain and print imperfections. High contrast.

[2 SCENE DETAILS]:
SCENE as layered paper cut-outs: [Subject details], [Props], [Accent geometric shapes]; elements have clean cut-out outlines, casting subtle drop shadows on layers below.

[3 BACKGROUND]:
On a bold flat [Color] cardboard paper background.

[4 TEXT BANNER (Headline)]:
A torn paper banner with a big bold headline "[HEADLINE TEXT]" written in heavy sans-serif capital letters.

[5 TECHNICAL]:
Flat-lay scanned look, straight-on composition, 16:9 or 9:16 aspect ratio.
```

---

## 2. The 4 Core Design Themes

| Theme | Color Palette | Typography | Texture & Finish | Best Topics |
| :--- | :--- | :--- | :--- | :--- |
| **Swiss Modern** | Pure red, jet black, clean white, slate gray | Heavy grotesque sans-serif (Helvetica) | Clean scissor cuts, subtle matte paper grain | Finance, technology, modern economics |
| **American Retro** | Aged sepia, mustard yellow, teal blue, cherry red | Bold slab-serifs or vintage display | Ben-Day dots, coffee stains, aged parchment | History, automotive, mid-century culture |
| **Punk Zine** | Duotone: neon yellow + black, hot pink + navy | Stencil, distressed stamp, ransom cutout | Heavy xerox copy grain, high-contrast, tape strips | Subcultures, crypto, revolutionary tech |
| **Chinese Ink** | Charcoal black, soft parchment cream, vermilion | Elegant brush-stroke lettering | Ink washes, soft deckled edges, rice paper fiber | Geopolitics, Eastern philosophy, trade |

---

## 3. Flat-Safe Animation Camera Trajectories

When animating flat paper-collage frames with Seedance or Kling, avoid extreme 3D rotations which distort text and flat geometry. Use **flat-safe 2.5D camera moves**:

* **`push_in`**: Uniform Ken Burns zoom-in; enhances tension and focus without perspective warp.
* **`pull_out`**: Uniform zoom-out; reveals broader historical or economic context.
* **`parallax`**: Front, middle, and background paper cutouts move at differential speeds across the X-axis, creating organic tactile depth.
* **`pan`**: Smooth horizontal scan across maps, timelines, or comparative columns.
* **`static`**: Rock-solid hold for 2–3 seconds to allow viewers to read complex infographics.

---

## 4. Narrative Arc Blueprints for Explainers

| Arc Pattern | Structure Sequence | Optimal Duration | Best Application |
| :--- | :--- | :---: | :--- |
| **`hook_payoff`** | Hook (≤3s) → Context → Build → Payoff → Wrap-up | 30s – 60s | Educational explainers, science breakdowns |
| **`pas`** | Problem → Agitate → Solve → Proof → Call to Action | 30s – 45s | B2B SaaS promos, product launches |
| **`timeline`** | Origin → Key Event 1 → Key Event 2 → Climax → Legacy | 45s – 90s | Historical events, founder stories, brand heritage |
| **`how_it_works`**| Hook → System Overview → Step 1 → Step 2 → Benefit | 30s – 60s | Technical tutorials, crypto protocols, engineering |

---

## 5. Production Multi-Beat Prompt Example (Seedance / Kling)

```text
Model: Seedance 2.0 / Kling 3.0 | Aspect: 16:9 | Duration: 10s

Editorial motion graphics style, mixed-media paper collage animation.
[0.0s – 3.0s]: Wide establishing shot of a flat-lay vintage world map on cream cardboard. A cut-out paper cargo ship glides along animated dashed red shipping lanes.
[3.0s – 6.5s]: Camera executes a smooth 2.5D parallax push-in. Floating paper bar charts rise from coastal ports, heights scaling upward with mechanical stop-motion clicks.
[6.5s – 10.0s]: Fast slide-in banner from left with bold black typography: "GLOBAL TRADE // 90% BY SEA". Text settles cleanly with zero camera drift.
Look: Tactile paper drop shadows, visible deckled edges, warm studio lighting from 45 degrees, high-contrast print aesthetic.
Audio: Tactile paper rustle, mechanical typewriter click on text settle, subtle vintage jazz double-bass groove.
```
