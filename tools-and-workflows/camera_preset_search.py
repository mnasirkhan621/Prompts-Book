#!/usr/bin/env python3
"""
Camera Preset Search CLI
Prompts Book Architecture - Architect: Muhammad Nasir Khan

Searches the 40+ camera movement catalog by mood, motion type, or genre.
"""

import sys

CAMERA_DATABASE = [
    {"name": "Dolly In", "type": "Linear", "best_for": "Intimacy, revelation, closing tension", "syntax": "Camera Dolly In toward his face over 6 seconds"},
    {"name": "Dolly Out", "type": "Linear", "best_for": "Isolation, widening context, departure", "syntax": "Camera Dolly Out revealing the desolate plain"},
    {"name": "Dolly Zoom (Vertigo)", "type": "Optical", "best_for": "Shock, panic, realization, psychological vertigo", "syntax": "Dolly Zoom In — subject size stays fixed as room distorts"},
    {"name": "FPV Drone", "type": "Kinetic", "best_for": "High-speed chase, extreme kinetic energy, sports", "syntax": "FPV Drone weaving through forest 2 meters behind bike"},
    {"name": "Action Run", "type": "Kinetic", "best_for": "Foot pursuit, combat sprint, urgent escape", "syntax": "Action Run — low tracking camera 1.5m behind sprint"},
    {"name": "360 Orbit", "type": "Rotational", "best_for": "Hero reveal, standoff, emotional isolation", "syntax": "360 Orbit around samurai drawing katana"},
    {"name": "Snorricam", "type": "Specialty", "best_for": "Panic attack, intoxication, psychological breakdown", "syntax": "Snorricam locked on face as background spins frantically"},
    {"name": "Crane Up", "type": "Vertical", "best_for": "Epic scale, transition from intimate to grand", "syntax": "Crane Up from boots in mud to vast valley"},
    {"name": "Dutch Angle", "type": "Pitch", "best_for": "Unease, tension, moral instability", "syntax": "Dutch Angle tilted 25 degrees on dim hallway"},
    {"name": "Whip Pan", "type": "Specialty", "best_for": "Dynamic high-tempo cut, sudden reaction", "syntax": "Whip Pan right from gunshot to broken window"}
]

def search_presets(query: str):
    q = query.lower()
    matches = [c for c in CAMERA_DATABASE if q in c["name"].lower() or q in c["best_for"].lower() or q in c["type"].lower()]

    print("=" * 65)
    print(f" CAMERA PRESET SEARCH — Query: '{query}'")
    print(f" Architect: Muhammad Nasir Khan")
    print("=" * 65)

    if not matches:
        print(" No matching camera preset found. Try 'chase', 'shock', 'intimate', 'linear'.")
    else:
        for m in matches:
            print(f" ▶ {m['name']} ({m['type']})")
            print(f"   Best For: {m['best_for']}")
            print(f"   Syntax:   \"{m['syntax']}\"")
            print("-" * 65)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_presets(" ".join(sys.argv[1:]))
    else:
        print("Usage: python camera_preset_search.py <keyword>")
        print("Example: python camera_preset_search.py chase")
