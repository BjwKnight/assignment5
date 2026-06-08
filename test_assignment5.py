import unittest
from assignment5 import fahrenheit_to_celsius, fibonacci


class TestAssignment5(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(68), 20)

    def test_fahrenheit_type_error(self):
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("warm")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_value_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci(3.5)

if __name__ == "__main__":
    unittest.main()