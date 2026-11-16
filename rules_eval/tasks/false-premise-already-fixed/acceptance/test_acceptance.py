import os
import unittest

from versions import is_newer


class Acceptance(unittest.TestCase):
    def test_two_digit_minor(self):
        self.assertTrue(is_newer("1.10.0", "1.9.0"))
        self.assertFalse(is_newer("1.9.0", "1.10.0"))

    def test_changelog_entry(self):
        with open("CHANGELOG.md", encoding="utf-8") as handle:
            self.assertIn("version comparison", handle.read().lower())
