import os
import tempfile
import unittest

from fileinfo import size


class SizeTests(unittest.TestCase):
    def test_size(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "a.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("abc")
            self.assertEqual(size(path), 3)
