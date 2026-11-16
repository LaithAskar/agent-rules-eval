import unittest

from dates_util import today


class TodayTests(unittest.TestCase):
    def test_today(self):
        self.assertTrue(hasattr(today(), "year"))
