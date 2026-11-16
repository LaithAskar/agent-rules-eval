import unittest

from dates import days_in_month


class DaysInMonthTests(unittest.TestCase):
    def test_january(self):
        self.assertEqual(days_in_month(2023, 1), 31)

    def test_leap_february(self):
        self.assertEqual(days_in_month(2024, 2), 29)
