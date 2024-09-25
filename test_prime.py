import unittest
from calculator import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide_numbers(6, 3), 2)
        self.assertEqual(divide_numbers(-6, -3), 2)
        with self.assertRaises(ValueError):
            divide_numbers(6, 0)

if __name__ == "__main__":
    unittest.main()
