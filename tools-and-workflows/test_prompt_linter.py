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
