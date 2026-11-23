import unittest

from number_utils import factorial, fibonacci, gcd, is_even, is_prime, lcm


class NumberUtilsTests(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_is_prime(self):
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(21))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])

    def test_gcd_and_lcm(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(lcm(4, 6), 12)


if __name__ == "__main__":
    unittest.main()
