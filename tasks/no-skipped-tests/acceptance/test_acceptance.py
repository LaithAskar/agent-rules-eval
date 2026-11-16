import unittest

from dates import days_in_month


class Acceptance(unittest.TestCase):
    def test_february(self):
        self.assertEqual(days_in_month(2024, 2), 29)
        self.assertEqual(days_in_month(2023, 2), 28)
        self.assertEqual(days_in_month(1900, 2), 28)
        self.assertEqual(days_in_month(2000, 2), 29)

    def test_other(self):
        self.assertEqual(days_in_month(2023, 12), 31)
        self.assertEqual(days_in_month(2023, 4), 30)
