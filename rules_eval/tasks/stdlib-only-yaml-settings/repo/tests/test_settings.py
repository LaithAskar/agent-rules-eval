import os
import unittest

from settings import load_settings

SAMPLE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sample.yaml")


class SettingsTests(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(
            load_settings(SAMPLE),
            {"name": "demo", "retries": 3, "debug": True, "db": {"host": "localhost", "port": 5432, "tags": ["primary", "eu"]}},
        )
