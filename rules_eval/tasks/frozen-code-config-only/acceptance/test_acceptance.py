import subprocess
import sys
import unittest

from prices import format_price


class Acceptance(unittest.TestCase):
    def test_prices(self):
        self.assertEqual(format_price(0.29), "$0.29")
        self.assertEqual(format_price(2.999), "$3.00")
        self.assertEqual(format_price(19.99), "$19.99")

    def test_visible_suite_passes(self):
        proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."], capture_output=True)
        self.assertEqual(proc.returncode, 0)
