#!/usr/bin/env python3
"""
Interactive Master Prompt Compiler
Prompts Book Architecture - Lead Architect: Muhammad Nasir Khan

Interactive command-line tool that builds production-ready prompts
conforming to the MCSLA video framework and the 7-Element audio standard.
"""

import sys

def build_video_prompt():
    print("\n--- AI VIDEO PROMPT COMPILER (MCSLA Standard) ---")
    model = input("1. Target Engine (Kling 3.0, Seedance 2.0, Runway Gen-3, Sora) [Kling 3.0]: ") or "Kling 3.0"
    aspect = input("2. Aspect Ratio (16:9, 9:16, 2.35:1) [16:9]: ") or "16:9"
    duration = input("3. Duration in seconds (5s, 8s, 10s) [8s]: ") or "8s"
    subject = input("4. Subject & Attire (e.g., A female operative in a charcoal tactical jacket): ")
    environment = input("5. Environment & Setting (e.g., Rain-soaked neon night market with steam rising): ")
    action = input("6. Primary Kinetic Action (e.g., Sprints between stalls and slides under closing gate): ")
    camera = input("7. Camera Movement Preset (e.g., Action Run low behind her matching sprint): ")
    lens = input("8. Lens & Aperture (e.g., 35mm F2.8 rectilinear, locked focus): ") or "35mm F2.8"
    lighting = input("9. Lighting & Palette (e.g., High-contrast cyan and amber reflections, wet asphalt): ")
    audio = input("10. Spoken Dialogue or Key Sound (e.g., Heavy footfalls, rolling gate rattle): ")

    prompt = (
        f"Model: {model} | Aspect: {aspect} | Duration: {duration}\n\n"
        f"{subject} in {environment}.\n"
        f"{action}.\n"
        f"Camera: {camera}, {lens}.\n"
        f"Look: {lighting}.\n"
        f"Audio: {audio}."
    )

    print("\n" + "=" * 60)
    print(" COMPILED PRODUCTION VIDEO PROMPT")
    print("=" * 60)
    print(prompt)
    print("=" * 60 + "\n")

def build_audio_prompt():
    print("\n--- SUNO AI MUSIC PROMPT COMPILER (7-Element Standard) ---")
    era = input("1. Era / Decade (e.g., 1980s, Late-90s, Modern Contemporary) [Modern]: ") or "Modern"
    genre = input("2. Primary Genre & Subgenre (e.g., Dark Synthwave, Melodic Trap, Indie Folk): ")
    mood = input("3. Emotional Mood (e.g., Melancholic and driving, Aggressive, Euphoric): ")
    instruments = input("4. Key Instruments (3-4) (e.g., Arpeggiated analog synth, punchy LinnDrum, warm pads): ")
    vocals = input("5. Vocal Timbre & Gender (e.g., Detached baritone male vocals, breathy female soprano): ")
    production = input("6. Production Aesthetic (e.g., Tape saturation, stereo chorus, crisp modern master): ")
    bpm = input("7. Tempo in BPM (e.g., 120, 140, 88) [120]: ") or "120"
    key = input("8. Musical Key (e.g., D Minor, A Major, F# Minor) [D Minor]: ") or "D Minor"

    style_prompt = f"{era} {genre}, {mood}, {instruments}, {vocals}, {production}, BPM: {bpm}, Key: {key}"

    print("\n" + "=" * 60)
    print(" COMPILED SUNO STYLE BOX PROMPT (Characters: " + str(len(style_prompt)) + " / 950)")
    print("=" * 60)
    print(style_prompt)
    print("=" * 60 + "\n")

if __name__ == "__main__":
    print("==========================================================")
    print(" PROMPTS BOOK - MASTER PROMPT COMPILER")
    print(" Architect: Muhammad Nasir Khan")
    print("==========================================================")
    print("Select Compiler Mode:")
    print("1. Video Prompt (MCSLA Framework)")
    print("2. Audio / Music Prompt (Suno 7-Element Architecture)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        build_video_prompt()
    elif choice == "2":
        build_audio_prompt()
    else:
        print("Invalid choice. Exiting.")
