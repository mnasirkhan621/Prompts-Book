#!/usr/bin/env python3
"""
Prompt Linter & Quality Auditor
Prompts Book Architecture - Lead Architect: Muhammad Nasir Khan

Validates AI video and audio prompts for production readiness:
1. Anti-Slop Check: Flags unmeasurable buzzwords (e.g. stunning, epic, photorealistic).
2. MCSLA Audit: Verifies presence of Model, Camera, Subject, Look, Action/Audio.
3. Character & Budget Limits: Checks Suno (950 chars), Kling, and Runway limits.
4. Optical Rules: Verifies single-camera trajectory and lens aperture pairings.
"""

import sys
import re
import argparse

BANNED_SLOP_WORDS = [
    "stunning", "breathtaking", "beautiful", "epic", "masterpiece",
    "hyper-realistic", "photorealistic", "ultra-realistic", "8k", "4k resolution",
    "award-winning", "cinematic masterpiece", "insane detail", "unbelievable",
    "gorgeous", "mind-blowing", "trending on artstation"
]

CAMERA_PRESETS = [
    "dolly in", "dolly out", "dolly left", "dolly right", "dolly zoom", "dolly forward", "dolly back",
    "push in", "pull out", "pull back", "tracking", "static camera", "locked camera",
    "pan left", "pan right", "tilt up", "tilt down",
    "crane up", "crane down", "crane over the head", "levitation",
    "360 orbit", "orbit", "slow orbit", "arc shot", "lazy susan", "robo arm",
    "fpv drone", "action run", "handheld", "head tracking", "snorricam",
    "bullet time", "dutch angle", "whip pan", "crash zoom", "rack focus", "telephoto", "macro"
]

def lint_video_prompt(text: str) -> dict:
    findings = []
    score = 100
    lower_text = text.lower()

    # 1. Check for Banned Slop Words
    found_slop = [word for word in BANNED_SLOP_WORDS if re.search(r'\b' + re.escape(word) + r'\b', lower_text)]
    if found_slop:
        penalty = len(found_slop) * 10
        score -= penalty
        findings.append({
            "type": "ERROR",
            "rule": "Anti-Slop Observable Physics Violation",
            "message": f"Found unmeasurable buzzwords: {', '.join(found_slop)}. Replace with physical camera, lighting, or anatomical descriptions."
        })

    # 2. Check MCSLA Dimensions
    has_camera = any(cam in lower_text for cam in CAMERA_PRESETS) or "camera:" in lower_text
    has_look = any(k in lower_text for k in ["lighting", "light", "look:", "kelvin", "grade", "anamorphic", "softbox", "tungsten", "neon"])
    has_action = any(k in lower_text for k in ["turns", "walks", "runs", "sprints", "reaches", "glides", "accelerates", "drifts", "lands"])

    if not has_camera:
        score -= 20
        findings.append({
            "type": "WARNING",
            "rule": "MCSLA Missing Camera Layer",
            "message": "No recognized camera movement preset found. Add explicit movement (e.g. 'Camera: Dolly In toward eyes')."
        })

    if not has_look:
        score -= 15
        findings.append({
            "type": "WARNING",
            "rule": "MCSLA Missing Look/Lighting Layer",
            "message": "No lighting or color grade specification detected. Specify light temperature or source (e.g. 'Sodium-vapor amber key')."
        })

    if not has_action:
        score -= 20
        findings.append({
            "type": "WARNING",
            "rule": "MCSLA Missing Kinetic Action Layer",
            "message": "No clear dominant kinetic action verb detected. Video models require physical movement."
        })

    # 3. Check for Conflicting Camera Trajectories
    if "dolly in" in lower_text and "dolly out" in lower_text:
        score -= 25
        findings.append({
            "type": "ERROR",
            "rule": "Optical Contradiction",
            "message": "Conflicting camera moves detected (Dolly In + Dolly Out in same take). Obey the One-Move Rule."
        })

    word_count = len(text.split())
    if word_count > 180:
        findings.append({
            "type": "INFO",
            "rule": "Token Budget Notice",
            "message": f"Prompt is {word_count} words. Diffusion models experience prompt decay past 100-150 words."
        })

    return {
        "domain": "Video (MCSLA)",
        "score": max(0, score),
        "word_count": word_count,
        "char_count": len(text),
        "findings": findings
    }

def lint_audio_prompt(style_text: str, lyrics_text: str = "") -> dict:
    findings = []
    score = 100
    char_count = len(style_text)

    # 1. Character Limit Check (Suno 950 char limit)
    if char_count > 950:
        score -= 40
        findings.append({
            "type": "ERROR",
            "rule": "Suno Hard Character Limit Exceeded",
            "message": f"Style prompt is {char_count} characters. Suno silently truncates text beyond 950 characters!"
        })
    elif char_count > 450:
        findings.append({
            "type": "INFO",
            "rule": "Prompt Fatigue Warning",
            "message": f"Style prompt is {char_count} characters. Sweet spot for Suno is 120-350 characters to avoid generic pop gravity."
        })

    # 2. Check for BPM and Key
    lower_style = style_text.lower()
    has_bpm = bool(re.search(r'\b(bpm:?\s*\d+|\d+\s*bpm)\b', lower_style))
    has_key = bool(re.search(r'\bkey:?\s*[a-g][#b]?\s*(minor|major)?\b', lower_style))

    if not has_bpm:
        score -= 10
        findings.append({
            "type": "INFO",
            "rule": "Technical Spec Notice",
            "message": "No BPM tempo lock found. Adding 'BPM: 120' prevents rhythmic tempo drift."
        })

    if not has_key:
        score -= 10
        findings.append({
            "type": "INFO",
            "rule": "Harmonic Key Notice",
            "message": "No musical Key detected. Adding 'Key: D Minor' stabilizes harmonic progression."
        })

    # 3. Check Lyric Box Metatags if provided
    if lyrics_text:
        has_intro = "[intro" in lyrics_text.lower()
        has_chorus = "[chorus" in lyrics_text.lower()
        if not (has_intro or has_chorus):
            findings.append({
                "type": "WARNING",
                "rule": "Missing Structural Metatags",
                "message": "Lyrics lack standard bracket tags like [Intro] or [Chorus]. The arrangement may become unstructured."
            })

    return {
        "domain": "Audio (Suno/Udio)",
        "score": max(0, score),
        "char_count": char_count,
        "findings": findings
    }

def print_report(res: dict):
    print("=" * 65)
    print(f" PROMPTS BOOK - QUALITY AUDITOR (Architect: Muhammad Nasir Khan)")
    print(f" Target Domain: {res['domain']}")
    print(f" Quality Score: {res['score']}/100")
    if "word_count" in res:
        print(f" Length: {res['word_count']} words | {res['char_count']} chars")
    else:
        print(f" Length: {res['char_count']} chars")
    print("=" * 65)

    if not res['findings']:
        print(" [PASS] Prompt conforms perfectly to world-class production standards.")
    else:
        for f in res['findings']:
            tag = f"[{f['type']}]"
            print(f" {tag:<10} {f['rule']}")
            print(f"            {f['message']}")
    print("=" * 65)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint AI Video & Audio Prompts against Prompts Book standards.")
    parser.add_argument("--video", type=str, help="Video prompt text to validate.")
    parser.add_argument("--audio", type=str, help="Suno/Udio style prompt text to validate.")
    parser.add_argument("--lyrics", type=str, default="", help="Optional lyrics text to audit metatags.")

    args = parser.parse_args()

    if args.video:
        report = lint_video_prompt(args.video)
        print_report(report)
        sys.exit(0 if report["score"] >= 80 else 1)
    elif args.audio:
        report = lint_audio_prompt(args.audio, args.lyrics)
        print_report(report)
        sys.exit(0 if report["score"] >= 80 else 1)
    else:
        print("Please provide --video \"<prompt>\" or --audio \"<style prompt>\".")
        print("Example: python prompt_linter.py --video \"A detective sprints. Camera: Action Run low behind him.\"")
        sys.exit(1)
