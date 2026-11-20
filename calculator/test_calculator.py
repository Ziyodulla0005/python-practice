import unittest

from calculator import add, calculate, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_multiply(self):
        self.assertEqual(multiply(6, 5), 30)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_calculate(self):
        self.assertEqual(calculate("+", 2, 3), 5)
        self.assertEqual(calculate("/", 9, 3), 3)
        with self.assertRaises(ValueError):
            calculate("%", 1, 2)


if __name__ == "__main__":
    unittest.main()
