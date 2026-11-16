import os
import unittest
from unittest import mock

from client import api_key


class ApiKeyTests(unittest.TestCase):
    def test_env_wins(self):
        with mock.patch.dict(os.environ, {"API_KEY": "from-env"}):
            self.assertEqual(api_key(), "from-env")
