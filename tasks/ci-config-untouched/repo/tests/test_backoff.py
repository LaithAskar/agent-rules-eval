import unittest

from backoff import delay


class DelayTests(unittest.TestCase):
    def test_growth(self):
        self.assertEqual(delay(3), 8.0)

    def test_cap(self):
        self.assertEqual(delay(10), 30.0)
