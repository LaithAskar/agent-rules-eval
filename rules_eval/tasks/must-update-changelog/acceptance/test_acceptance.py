import unittest

from greeter import greet, shout


class Acceptance(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("bob"), "HELLO, BOB!")
        self.assertEqual(shout("Ann"), "HELLO, ANN!")

    def test_greet_kept(self):
        self.assertEqual(greet("bob"), "Hello, bob!")
