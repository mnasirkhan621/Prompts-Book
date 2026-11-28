#!/usr/bin/env python3
"""
Unit Tests for Prompts Book Linter
Architect: Muhammad Nasir Khan
"""

import unittest
from prompt_linter import lint_video_prompt, lint_audio_prompt

class TestPromptLinter(unittest.TestCase):

    def test_valid_video_prompt(self):
        prompt = (
            "A detective in a dark trench coat sprints through a wet alleyway. "
            "Camera: Action Run low behind him matching speed. "
            "Look: Sodium-vapor 2200K key light, cold rain reflections on asphalt. "
            "Audio: Heavy footsteps and rain patter."
        )
        report = lint_video_prompt(prompt)
        self.assertGreaterEqual(report["score"], 80)
        self.assertEqual(len([f for f in report["findings"] if f["type"] == "ERROR"]), 0)

    def test_valid_veo3_prompt(self):
        prompt = (
            "Medium close-up, slow push in on a 35mm lens. "
            "A ceramicist turns a clay bowl on a wheel as morning window light casts warm 3200K shadows. "
            "Audio: Wheel hum and wet clay sliding cleanly."
        )
        report = lint_video_prompt(prompt)
        self.assertEqual(report["score"], 100)
        self.assertEqual(report["findings"], [])

    def test_valid_ltx25_and_suno_v6_prompts(self):
        ltx_prompt = (
            "Wide shot with tracking movement on 28mm anamorphic lens: a courier walks along wet concrete "
            "under cold 6000K neon light as rain drifts through the frame. "
            "Audio: steady rain patter and footsteps."
        )
        v_report = lint_video_prompt(ltx_prompt)
        self.assertEqual(v_report["score"], 100)

        suno_style = "Gravelly baritone male vocal. Dark synthwave, pulsing analog bass, LinnDrum, BPM: 120, Key: A Minor"
        suno_lyrics = "[Intro - Analog drone]\n\n[Verse 1 - Cold steady pulse]\nShadow on the glass\n[Chorus - Full synth lift]\nSignal cutting through\n[End]"
        a_report = lint_audio_prompt(suno_style, suno_lyrics)
        self.assertEqual(a_report["score"], 100)

    def test_banned_slop_words_detection(self):
        prompt = "An epic and stunning cinematic masterpiece with photorealistic 8k detail."
        report = lint_video_prompt(prompt)
        errors = [f for f in report["findings"] if f["type"] == "ERROR"]
        self.assertTrue(any("Anti-Slop" in e["rule"] for e in errors))

    def test_suno_character_limit_audit(self):
        short_prompt = "1980s synthwave, analog synths, punchy LinnDrum, BPM: 120, Key: D Minor"
        report = lint_audio_prompt(short_prompt)
        self.assertLessEqual(report["char_count"], 950)
        self.assertGreaterEqual(report["score"], 80)

        long_prompt = "synthwave " * 200
        over_report = lint_audio_prompt(long_prompt)
        errors = [f for f in over_report["findings"] if f["type"] == "ERROR"]
        self.assertTrue(any("Character Limit" in e["rule"] for e in errors))

if __name__ == "__main__":
    unittest.main()
