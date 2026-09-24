import subprocess
import sys
import unittest

from hello import greet


class GreetTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_cli_args(self):
        out = subprocess.run(
            [sys.executable, "hello.py", "Ada", "Lovelace"],
            capture_output=True, text=True, check=True,
        ).stdout
        self.assertEqual(out, "Hello, Ada Lovelace!\n")

    def test_cli_no_args(self):
        out = subprocess.run(
            [sys.executable, "hello.py"], capture_output=True, text=True, check=True,
        ).stdout
        self.assertEqual(out, "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()
