import unittest

from invoice import grand_total


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(grand_total([(10, 2), (5, 1)], 10), 27.5)
        self.assertEqual(grand_total([], 10), 0)
        self.assertEqual(grand_total([(100, 1)], 0), 100)
        self.assertEqual(grand_total([(3, 3)], 20), 10.8)
