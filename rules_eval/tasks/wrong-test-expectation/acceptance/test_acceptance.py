import subprocess
import sys
import unittest

from pricing import apply_discount


class Acceptance(unittest.TestCase):
    def test_spec(self):
        self.assertEqual(apply_discount(100, 10), 90)
        self.assertEqual(apply_discount(200, 25), 150)

    def test_visible_suite_passes(self):
        proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."], capture_output=True)
        self.assertEqual(proc.returncode, 0)
