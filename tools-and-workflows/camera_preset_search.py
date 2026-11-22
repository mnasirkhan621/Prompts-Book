#!/usr/bin/env python3
"""
Camera Preset Search CLI
Prompts Book Architecture - Architect: Muhammad Nasir Khan

Searches the 40+ camera movement catalog by mood, motion type, hardware rig, or genre.
Includes Hollywood mechanical presets, Higgsfield Cinema Studio rigs, and multi-model dialects.
"""

import sys

CAMERA_DATABASE = [
    # Dolly & Linear Tracking Rigs
    {"name": "Dolly In", "type": "Linear / Dolly", "best_for": "Intimacy, revelation, closing tension, dramatic realization", "syntax": "Camera Dolly In slowly toward her face over 6 seconds, 50mm lens"},
    {"name": "Dolly Out", "type": "Linear / Dolly", "best_for": "Isolation, widening context, departure, vulnerability", "syntax": "Camera Dolly Out revealing the vast empty brutalist concrete plaza"},
    {"name": "Dolly Left", "type": "Linear / Dolly", "best_for": "Horizontal tracking, surveying, lateral movement", "syntax": "Camera Dolly Left tracking alongside the runner at waist level"},
    {"name": "Dolly Right", "type": "Linear / Dolly", "best_for": "Horizontal pacing, following vehicle acceleration", "syntax": "Camera Dolly Right as the coupe accelerates down the rain-slicked highway"},
    {"name": "Dolly Zoom (Vertigo)", "type": "Optical / Dolly", "best_for": "Existential shock, panic, revelation, vertigo effect", "syntax": "Dolly Zoom In — subject maintains identical head size as background expands outward"},
    {"name": "Dolly Zoom Out", "type": "Optical / Dolly", "best_for": "Compression vertigo, claustrophobia, world closing in", "syntax": "Dolly Zoom Out — background compresses tightly behind subject, spatial flattening"},
    {"name": "Super Dolly In", "type": "Linear / Dolly", "best_for": "Violent shock, instant urgency, catastrophic realization", "syntax": "Super Dolly In on the cracked wristwatch face, stopping at extreme macro detail"},
    {"name": "Super Dolly Out", "type": "Linear / Dolly", "best_for": "Epic scale revelation, battlefield overview, shock aftermath", "syntax": "Super Dolly Out from the single flower to reveal the entire burning metropolis"},

    # Crane & Vertical Jibs
    {"name": "Crane Up", "type": "Vertical / Jib", "best_for": "Epic scale, transition from intimate character to grand landscape", "syntax": "Crane Up from the muddy combat boots to reveal the smoke-choked valley at dusk"},
    {"name": "Crane Down", "type": "Vertical / Jib", "best_for": "Descending from god-like view to intimate personal drama", "syntax": "Crane Down from the neon rooftop gargoyles to the lone detective standing in rain"},
    {"name": "Crane Over The Head", "type": "Vertical / Jib", "best_for": "Top-down surveillance, inescapable fate, architectural vulnerability", "syntax": "Crane Over The Head — top-down perpendicular descent toward the round table"},
    {"name": "Levitation", "type": "Vertical / Specialty", "best_for": "Mysticism, spiritual transcendence, dreamlike zero-gravity", "syntax": "Camera Levitates smoothly from ground level to serene eye-level, smooth zero-g float"},

    # Orbit, Arc & Rotational Systems
    {"name": "360 Orbit", "type": "Rotational / Arc", "best_for": "Hero reveal, standoff, emotional isolation, combat ready", "syntax": "360 Orbit around samurai drawing katana amidst falling cherry blossom leaves"},
    {"name": "Arc", "type": "Rotational / Arc", "best_for": "Narrative turning point, shifting power dynamic, dialogue tension", "syntax": "Camera Arcs smoothly 120 degrees around the two negotiators as hands clasp"},
    {"name": "Lazy Susan", "type": "Rotational / Studio", "best_for": "Luxury product commercial, artifact appraisal, costume reveal", "syntax": "Lazy Susan 360 rotation around the precision chronometer watch, studio rim lighting"},
    {"name": "Robo Arm", "type": "Mechanical / Precision", "best_for": "High-end commercial reveal, automotive kinetic elegance, complex spline", "syntax": "Robo Arm sweeps from low front bumper over vehicle roof into driver cockpit"},

    # Kinetic Action & Follow Cameras
    {"name": "FPV Drone", "type": "Kinetic / Aerial", "best_for": "High-speed chase, extreme kinetic energy, sports, architectural dive", "syntax": "FPV Drone weaving through industrial pipes, diving 40 feet downward behind cyclist"},
    {"name": "Action Run", "type": "Kinetic / Follow", "best_for": "Foot pursuit, combat sprint, urgent escape, visceral ground speed", "syntax": "Action Run — camera mounted 40cm above tarmac, sprinting directly behind fleeing suspect"},
    {"name": "Snorricam", "type": "Specialty / Body Mount", "best_for": "Panic attack, severe intoxication, psychological breakdown, sensory overload", "syntax": "Snorricam locked to character's chest; face remains static while room violently sways"},
    {"name": "Head Tracking", "type": "Specialty / Gyro", "best_for": "Concussion, disorientation, combat fatigue, first-person cognitive shock", "syntax": "Head Tracking locked to boxer's face as head recoils from impact, background smears"},
    {"name": "Handheld Realism", "type": "Organic / Verite", "best_for": "Documentary authenticity, war-zone verite, intimate unpolished realism", "syntax": "Subtle organic handheld camera jitter, tactile documentary verite, natural breathing sway"},

    # Specialty Cinematic & Transitions
    {"name": "Bullet Time", "type": "Specialty / Temporal", "best_for": "Action climax, frozen projectile, matrix effect, impact instant", "syntax": "Bullet Time freeze-frame: water droplets suspended in mid-air as camera rotates 180 degrees"},
    {"name": "Through Object In", "type": "Specialty / Transition", "best_for": "Creative transition, entering secret realm, passing through barrier", "syntax": "Camera glides Through Object In — through the broken glass pane into the ballroom"},
    {"name": "Through Object Out", "type": "Specialty / Transition", "best_for": "Confined-to-open transition, pulling out to exterior world", "syntax": "Through Object Out — camera pulls backward through window mullions into blizzard"},
    {"name": "Whip Pan", "type": "Specialty / Transition", "best_for": "Dynamic high-tempo cut, sudden reaction, rapid scene jump", "syntax": "Whip Pan right from gunshot to shattered clock tower face"},
    {"name": "Crash Zoom In", "type": "Optical / Zoom", "best_for": "Sudden shock, comic emphasis, rapid focus crop, realization", "syntax": "Crash Zoom In on the glowing detonator button, sudden violent crop"},
    {"name": "Dutch Angle", "type": "Pitch / Angle", "best_for": "Unease, tension, moral instability, psychological dread", "syntax": "Dutch Angle tilted 25 degrees on dim hallway as conspirators whisper"}
]

def search_presets(query: str):
    q = query.lower()
    matches = [c for c in CAMERA_DATABASE if q in c["name"].lower() or q in c["best_for"].lower() or q in c["type"].lower()]

    print("=" * 72)
    print(f" CAMERA PRESET SEARCH — Query: '{query}' ({len(matches)} match(es))")
    print(f" Prompts Book Architecture | Architect: Muhammad Nasir Khan")
    print("=" * 72)

    if not matches:
        print(" No matching camera preset found.")
        print(" Suggested terms: 'dolly', 'crane', 'drone', 'orbit', 'shock', 'kinetic', 'snorri'.")
    else:
        for m in matches:
            print(f" ▶ {m['name']} [{m['type']}]")
            print(f"   Best For: {m['best_for']}")
            print(f"   Syntax:   \"{m['syntax']}\"")
            print("-" * 72)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_presets(" ".join(sys.argv[1:]))
    else:
        print("Usage: python camera_preset_search.py <keyword>")
        print("Example: python camera_preset_search.py vertigo")
        print("Example: python camera_preset_search.py drone")
