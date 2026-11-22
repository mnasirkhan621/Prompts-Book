# Master Camera Movement & Control Catalog

This encyclopedia details the recognized camera presets, movements, and execution syntax for high-end AI video generators. Using exact industry terminology forces the underlying models to generate authentic cinematography.

---

## 1. Dolly & Linear Tracking

Linear movement along a single spatial axis:

| Movement | Description | Best Dramatic Use | Exact Prompt Syntax |
| :--- | :--- | :--- | :--- |
| **Dolly In** | Smooth forward travel toward the subject | Focus, building intimacy, dramatic revelation | `Camera Dolly In toward his eyes over 6 seconds` |
| **Dolly Out** | Smooth backward pull away from subject | Isolation, expanding context, conclusion | `Camera Dolly Out revealing the desolate landscape` |
| **Dolly Left / Right** | Lateral linear tracking across a plane | Following horizontal movement, scene scanning | `Camera Dolly Left tracking alongside the running courier` |
| **Dolly Zoom In** | Dolly forward while zooming out (Vertigo effect) | Psychological shock, panic, reality unraveling | `Dolly Zoom In — subject size remains fixed as the room warps` |
| **Dolly Zoom Out** | Dolly backward while zooming in | Overwhelm, claustrophobia, impending doom | `Dolly Zoom Out — background expands and looms over the figure` |
| **Super Dolly In** | Accelerated rapid rush toward subject | Sudden violent discovery, urgent focus | `Super Dolly In directly to the crack on the spaceship hull` |

---

## 2. Vertical & Crane Movements

Elevation changes along the Y-axis:

| Movement | Description | Best Dramatic Use | Exact Prompt Syntax |
| :--- | :--- | :--- | :--- |
| **Crane Up** | Vertical rise from ground level upward | Establishing scope, rising triumphant, grandeur | `Crane Up from boots in mud to the vast army on the ridge` |
| **Crane Down** | Vertical descent from high overhead | Personalizing, descending into intimacy | `Crane Down through warehouse rafters to the lone worker` |
| **Crane Over The Head** | Vertical climb directly above the subject | Vulnerability, defeat, geometric choreography | `Crane Over The Head — top-down view of the labyrinth` |
| **Levitation** | Weightless, dreamlike upward float | Mystical, transcendence, surreal moments | `Camera Levitates smoothly from ground to eye level` |

---

## 3. Orbit & Rotational Movements

Circular travel around a focal point:

| Movement | Description | Best Dramatic Use | Exact Prompt Syntax |
| :--- | :--- | :--- | :--- |
| **360 Orbit** | Full circular rotation around centered subject | Hero moments, disorientation, standoff | `360 Orbit around the samurai drawing his blade` |
| **Arc Shot** | Semi-circular partial sweep (90°–180°) | Emotional turning points, conversational pivot | `Camera Arcs slowly 180 degrees around the two negotiators` |
| **Lazy Susan** | Slow turntable rotation, centered object | Product luxury showcase, artifact examination | `Lazy Susan rotation around the mechanical chronograph watch` |
| **Robo Arm** | Complex multi-axis mechanical arc | Precision commercial reveals, high-tech styling | `Robo Arm sweeps along the car body from front grill to taillight` |

---

## 4. Follow & Kinetic Action

Dynamic tracking of active subjects:

| Movement | Description | Best Dramatic Use | Exact Prompt Syntax |
| :--- | :--- | :--- | :--- |
| **FPV Drone** | Agile, high-speed weaving trajectory | Chase sequences, extreme sports, aerial energy | `FPV Drone chases the motocross rider through dense forest` |
| **Action Run** | Low-angle camera sprinting behind/beside subject | Foot chases, combat pursuit, urgent escape | `Action Run — low tracking camera locked 1 meter behind her sprint` |
| **Handheld** | Natural operator breathing and organic micro-shake | Documentary realism, warzone chaos, intimate drama | `Handheld camera jostling with the protesting crowd` |
| **Head Tracking** | Camera locked rigidly to subject's head position | Disorientation, concussive impact, delirium | `Head Tracking locked onto boxer's head as he staggers` |
| **Snorricam** | Rig mounted directly to actor's chest facing them | Psychological breakdown, paranoia, panic attack | `Snorricam locked on his face as the background spins frantically` |

---

## 5. Specialty & Optical Effects

| Movement | Description | Best Dramatic Use | Exact Prompt Syntax |
| :--- | :--- | :--- | :--- |
| **Bullet Time** | Subject frozen in slow-motion, camera sweeps around | Climax impact, explosive physics | `Bullet Time orbit around the martial artist mid-air kick` |
| **Dutch Angle** | Camera tilted diagonally off-axis (15°–45°) | Tension, moral instability, dread, delirium | `Dutch Angle canted 25 degrees as the detective enters the trap` |
| **Whip Pan** | Rapid lateral motion blur transition | High-tempo scene transitions, sudden reaction | `Whip Pan right from the gunshot to the shattered mirror` |
| **Through Object In** | Camera passes through a narrow aperture or obstacle | Revealing hidden rooms, immersive transitions | `Camera glides Through Object In — through the keyhole into darkness` |
| **Crash Zoom In** | Instantaneous high-speed optical zoom | Sudden realization, punchline, comedic or dramatic shock | `Crash Zoom In on the ticking bomb timer` |

---

## The One-Move Rule for Maximum Stability

For any single 5–10 second shot, specify **ONE primary camera trajectory**. Stacking contradictory or excessive moves (e.g., *"dolly in while orbiting, craning down, and tilting up"*) results in severe spatial warping and generation failure.

* **Incorrect:** `Camera dollies in while panning left and tilting down and crash zooming.`
* **Correct:** `Camera: Slow Dolly In from medium to close-up along the central axis over 6 seconds.`
