import unittest

from app_config import load


class LoadTests(unittest.TestCase):
    def test_default_file(self):
        self.assertEqual(load()["retries"], 3)
