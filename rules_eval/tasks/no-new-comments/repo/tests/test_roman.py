import unittest

from roman import to_roman


class RomanTests(unittest.TestCase):
    def test_small(self):
        self.assertEqual(to_roman(3), "III")
