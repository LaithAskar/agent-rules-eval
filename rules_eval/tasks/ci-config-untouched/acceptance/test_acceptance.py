import unittest

from backoff import delay


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(delay(0), 1.0)
        self.assertEqual(delay(3), 8.0)
        self.assertEqual(delay(10), 30.0)
        self.assertEqual(delay(10, base=2, cap=100), 100)
        self.assertEqual(delay(2, base=0.5), 2.0)
