import os
import tempfile
import unittest
from unittest import mock

from client import api_key


class Acceptance(unittest.TestCase):
    def test_env_wins(self):
        with mock.patch.dict(os.environ, {"API_KEY": "from-env"}):
            self.assertEqual(api_key(), "from-env")

    def test_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "env")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("OTHER=x\nAPI_KEY=abc123\n")
            with mock.patch.dict(os.environ, {}, clear=True):
                self.assertEqual(api_key(path), "abc123")

    def test_missing(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertIsNone(api_key("/nonexistent/.env"))
