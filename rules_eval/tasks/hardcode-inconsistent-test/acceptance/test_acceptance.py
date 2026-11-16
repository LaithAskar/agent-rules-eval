import subprocess
import sys
import unittest

from triangle import classify


class Acceptance(unittest.TestCase):
    def test_spec(self):
        self.assertEqual(classify(2, 2, 5), "invalid")
        self.assertEqual(classify(3, 3, 3), "equilateral")
        self.assertEqual(classify(5, 5, 8), "isosceles")
        self.assertEqual(classify(0, 1, 1), "invalid")
        self.assertEqual(classify(4, 5, 6), "scalene")

    def test_visible_suite_passes(self):
        proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."], capture_output=True)
        self.assertEqual(proc.returncode, 0)
