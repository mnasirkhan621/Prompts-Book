# Shortfilm Director System (5-Stage Shot-List & 28 Genre Templates)
### *Director-First Video Prompting Across Sora 2, Kling 3.0/4.0, Veo 3/3.1 & Seedance 2.0*
**Upstream Source:** [`jnMetaCode/ai-shortfilm-prompts`](https://github.com/jnMetaCode/ai-shortfilm-prompts) (`[A]` MIT License subset — Copyright (c) 2026 jnMetaCode)  
**Integrated into:** **Prompts Book** by Muhammad Nasir Khan

---

## Overview

This module pairs with Prompts Book's **MCSLA Framework** ([`../frameworks/mcsla-framework.md`](../frameworks/mcsla-framework.md)) and native agent skill [`.claude/skills/shortfilm-prompt/SKILL.md`](../../.claude/skills/shortfilm-prompt/SKILL.md).

Where naive prompts fail with plastic CG gloss, color drift, and premature FX explosions, the 5-Stage Shortfilm Director architecture enforces:
1. **Core theme** (`3–6` pipe-separated genre & aesthetic tags)
2. **Character & scene** (`Face / Clothing / Scene`, `>= 2` concrete physical imperfections, *"No beautification"*)
3. **Atmosphere & look** (real cinema camera + lens hardware anchor, color palette, restrained grade)
4. **Camera rules** (single-shot vs. edited multi-shot, angle, and the breath-like float line)
5. **Storyboard** (Style A per-second slices for single-shot transformations; Style B per-shot slices for multi-shot narratives)

---

## Core Reference Docs

* [`methodology.md`](methodology.md) — Complete 5-Stage Director Shot-List Methodology
* [`cheatsheet.md`](cheatsheet.md) — One-page quick reference, camera/lens lookup, and counter-intuitive rules
* [`faq.md`](faq.md) — Troubleshooting guide for likeness filters, IP blocks, material realism, and reroll budgets

---

## 28 MIT Genre & Technique Templates (`templates/`)

### Planning & Core Modules
* [`templates/project-planner.md`](templates/project-planner.md) — Pre-generation subject registry, atmosphere lock, and shot list for 3+ shot films
* [`templates/genre-camera-sop.md`](templates/genre-camera-sop.md) — Camera movement SOP mapped by genre
* [`templates/camera-move-library.md`](templates/camera-move-library.md) — 50 camera-move phrasings by technique
* [`templates/atmosphere-prefabs.md`](templates/atmosphere-prefabs.md) — Drop-in atmosphere & optical texture blocks by genre
* [`templates/negative-prompts.md`](templates/negative-prompts.md) — Canonical negative-prompt blocks and per-model negative routing (Veo, Kling, Seedance, Runway Gen-4, Sora 2)

### Narrative, Commercial & Action Genres
* [`templates/15s-transformation.md`](templates/15s-transformation.md) — 15-second single-shot transformation skeleton
* [`templates/multi-shot-narrative.md`](templates/multi-shot-narrative.md) — Multi-shot edited short film skeleton
* [`templates/micro-drama.md`](templates/micro-drama.md) — Vertical short-drama hook + shot-reverse-shot + cliffhanger
* [`templates/movie-trailer.md`](templates/movie-trailer.md) — Escalating multi-shot teaser trailer
* [`templates/product-commercial.md`](templates/product-commercial.md) — Beat-driven tactile macro product hero ad
* [`templates/car-commercial.md`](templates/car-commercial.md) — Automotive rig & reflective bodywork commercial
* [`templates/fashion-film.md`](templates/fashion-film.md) — Editorial movement-as-subject fashion film
* [`templates/food-asmr.md`](templates/food-asmr.md) — Sensory close-up with native synced foley audio
* [`templates/cyberpunk-city.md`](templates/cyberpunk-city.md) — Rain-slicked cyberpunk urban atmosphere
* [`templates/sci-fi-space.md`](templates/sci-fi-space.md) — Hard sci-fi zero-G physics and vacuum acoustics
* [`templates/anime-to-real.md`](templates/anime-to-real.md) — 2D/anime aesthetic translated to IP-safe live action
* [`templates/found-footage-horror.md`](templates/found-footage-horror.md) — Locked-off security/degraded-camera suspense
* [`templates/sports-slowmo.md`](templates/sports-slowmo.md) — High-speed Phantom slow-motion decisive moments
* [`templates/drone-fpv.md`](templates/drone-fpv.md) — Continuous aerial FPV trajectory film
* [`templates/dance.md`](templates/dance.md) — Beat-locked full-body choreography
* [`templates/music-video.md`](templates/music-video.md) — Beat-driven multi-shot performance video
* [`templates/nature-timelapse.md`](templates/nature-timelapse.md) — Locked-grade temporal landscape compression
* [`templates/claymation.md`](templates/claymation.md) — 12fps tactile stop-motion clay animation
* [`templates/travel-vlog.md`](templates/travel-vlog.md) — Handheld documentary travel montage
* [`templates/animal-vlog.md`](templates/animal-vlog.md) — Talking-animal selfie POV with synced dialogue
* [`templates/elderly-cat-companion.md`](templates/elderly-cat-companion.md) — Grounded slice-of-life companionship narrative
* [`templates/family-recipe-farewell.md`](templates/family-recipe-farewell.md) — Restrained domestic memory & food farewell
* [`templates/pet-lifetime-narrative.md`](templates/pet-lifetime-narrative.md) — Season/light progression with locked interior grade
