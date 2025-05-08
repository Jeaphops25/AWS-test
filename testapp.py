import unittest
from app import say_hello

class TestApp(unittest.TestApp):
    def test_say_hello(self):
        self.asserEqual(say_hello("AWS"), "Hello, AWS")

if __name__ == "__main__":
    unittest.main()