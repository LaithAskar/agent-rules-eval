import os
import tempfile
import unittest

from settings import load_settings


def load_text(text):
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "settings.yaml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        return load_settings(path)


class Acceptance(unittest.TestCase):
    def test_scalars(self):
        text = "name: demo\nratio: 0.5\nneg: -4\nflag: false\nnothing: null\nquoted: \"a # not a comment\"\nsingle: 'x: y'\n"
        self.assertEqual(load_text(text), {"name": "demo", "ratio": 0.5, "neg": -4, "flag": False, "nothing": None, "quoted": "a # not a comment", "single": "x: y"})

    def test_comments_and_blank_lines(self):
        text = "# top\n\nname: demo  # trailing\n\n  \nretries: 3\n"
        self.assertEqual(load_text(text), {"name": "demo", "retries": 3})

    def test_deep_nesting_and_lists(self):
        text = "a:\n  b:\n    c:\n      - 1\n      - two\n      - 3.5\n    d: x\n  e: true\nf:\n  - a\n  - b\n"
        self.assertEqual(load_text(text), {"a": {"b": {"c": [1, "two", 3.5], "d": "x"}, "e": True}, "f": ["a", "b"]})

    def test_url_value(self):
        self.assertEqual(load_text("url: http://example.com:8080/x\n"), {"url": "http://example.com:8080/x"})
