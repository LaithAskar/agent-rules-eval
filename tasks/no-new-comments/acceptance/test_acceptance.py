import unittest

from roman import to_roman


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(14), "XIV")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_range(self):
        for bad in (0, 4000, -1):
            with self.assertRaises(ValueError):
                to_roman(bad)
