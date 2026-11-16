import os
import tempfile
import unittest

from fileinfo import line_count


class Acceptance(unittest.TestCase):
    def count(self, content):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "a.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(content)
            return line_count(path)

    def test_counts(self):
        self.assertEqual(self.count("a\nb\nc\n"), 3)
        self.assertEqual(self.count("a\nb\nc"), 3)
        self.assertEqual(self.count(""), 0)
