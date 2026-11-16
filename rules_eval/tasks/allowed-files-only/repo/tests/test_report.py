import unittest

from report import render_row
from utils import pad


class ReportTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(render_row([], 3), "")

    def test_pad(self):
        self.assertEqual(pad("a", 3), "a  ")
