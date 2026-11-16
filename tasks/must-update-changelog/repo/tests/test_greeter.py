import unittest

from greeter import greet


class GreetTests(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("bob"), "Hello, bob!")
