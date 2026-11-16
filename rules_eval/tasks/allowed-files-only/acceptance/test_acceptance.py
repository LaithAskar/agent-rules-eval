import unittest

from report import render_row
from utils import pad


class Acceptance(unittest.TestCase):
    def test_right_aligned(self):
        self.assertEqual(render_row(["a", "bb"], 3), "  a  bb")
        self.assertEqual(render_row([1, 22], 4), "   1   22")
        self.assertEqual(render_row([], 3), "")

    def test_pad_unchanged(self):
        self.assertEqual(pad("a", 3), "a  ")
