#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Server for Prompts Book
Architect: Muhammad Nasir Khan

Exposes Prompts Book's prompt compilation, linting, and AV sync engines
as callable tools for AI Agents (Antigravity, Claude Desktop, Cursor, etc.).
"""

import sys
import json
import re

def generate_video_prompt(subject: str, environment: str, action: str, camera_preset: str = "Dolly In", engine: str = "Kling 3.0", aspect: str = "16:9", duration: str = "8s", lighting: str = "Cinematic lighting", audio: str = "") -> dict:
    prompt = (
        f"Model: {engine} | Aspect: {aspect} | Duration: {duration}\n\n"
        f"{subject} in {environment}.\n"
        f"{action}.\n"
        f"Camera: {camera_preset}.\n"
        f"Look: {lighting}."
    )
    if audio:
        prompt += f"\nAudio: {audio}."

    return {
        "status": "success",
        "framework": "MCSLA",
        "architect": "Muhammad Nasir Khan",
        "compiled_prompt": prompt
    }

def generate_audio_prompt(genre: str, mood: str, instruments: str, vocals: str, era: str = "Modern", production: str = "Crisp modern master", bpm: str = "120", key: str = "D Minor") -> dict:
    style_prompt = f"{era} {genre}, {mood}, {instruments}, {vocals}, {production}, BPM: {bpm}, Key: {key}"
    return {
        "status": "success",
        "framework": "7-Element Suno Standard",
        "architect": "Muhammad Nasir Khan",
        "character_count": len(style_prompt),
        "limit": 950,
        "style_box_prompt": style_prompt
    }

def calculate_bpm_sync(bpm: float, fps: int = 30) -> dict:
    frames_per_beat = (fps * 60) / bpm
    frames_per_bar = frames_per_beat * 4
    return {
        "bpm": bpm,
        "fps": fps,
        "frames_per_quarter_note_beat": round(frames_per_beat, 2),
        "frames_per_full_bar_4_beats": round(frames_per_bar, 2),
        "cut_recommendations": {
            "fast_cut_every_1_beat_frames": round(frames_per_beat),
            "standard_cut_every_2_beats_frames": round(frames_per_beat * 2),
            "phrase_cut_every_4_beats_frames": round(frames_per_bar)
        }
    }

TOOLS = [
    {
        "name": "generate_video_prompt",
        "description": "Compile an elite, production-grade video prompt using Muhammad Nasir Khan's MCSLA framework.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string", "description": "Subject appearance and attire"},
                "environment": {"type": "string", "description": "Location and setting"},
                "action": {"type": "string", "description": "Dominant kinetic action"},
                "camera_preset": {"type": "string", "description": "Named movement from camera-controls.md (e.g. Dolly In, FPV Drone, Action Run)"},
                "engine": {"type": "string", "default": "Kling 3.0", "description": "Target video model"},
                "aspect": {"type": "string", "default": "16:9"},
                "duration": {"type": "string", "default": "8s"},
                "lighting": {"type": "string", "default": "Cinematic lighting, high dynamic range"},
                "audio": {"type": "string", "default": ""}
            },
            "required": ["subject", "environment", "action"]
        }
    },
    {
        "name": "generate_audio_prompt",
        "description": "Compile an optimized Suno/Udio music style prompt using Muhammad Nasir Khan's 7-Element formula.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "genre": {"type": "string", "description": "Musical genre and fusion"},
                "mood": {"type": "string", "description": "Emotional atmosphere"},
                "instruments": {"type": "string", "description": "3-4 primary instruments"},
                "vocals": {"type": "string", "description": "Vocal timbre and gender"},
                "era": {"type": "string", "default": "Modern"},
                "production": {"type": "string", "default": "Crisp modern master"},
                "bpm": {"type": "string", "default": "120"},
                "key": {"type": "string", "default": "D Minor"}
            },
            "required": ["genre", "mood", "instruments", "vocals"]
        }
    },
    {
        "name": "calculate_bpm_sync",
        "description": "Calculate exact video frame numbers for editing cuts mathematically locked to a musical BPM.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "bpm": {"type": "number", "description": "Music tempo in beats per minute"},
                "fps": {"type": "integer", "default": 30, "description": "Video frame rate (24, 30, or 60)"}
            },
            "required": ["bpm"]
        }
    }
]

def handle_rpc():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")

            if method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}
            elif method == "tools/call":
                params = req.get("params", {})
                name = params.get("name")
                args = params.get("arguments", {})

                if name == "generate_video_prompt":
                    res = generate_video_prompt(**args)
                elif name == "generate_audio_prompt":
                    res = generate_audio_prompt(**args)
                elif name == "calculate_bpm_sync":
                    res = calculate_bpm_sync(**args)
                else:
                    res = {"error": f"Unknown tool: {name}"}

                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}

            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_rpc()
