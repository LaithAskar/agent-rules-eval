import os
import tempfile
import unittest

from app_config import load


class Acceptance(unittest.TestCase):
    def test_custom_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "custom.ini")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("[network]\nretries = 7\ntimeout = 2\n")
            self.assertEqual(load(path), {"retries": 7, "timeout": 2})
