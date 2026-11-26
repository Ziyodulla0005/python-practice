import unittest

from string_tools import capitalize_words, is_palindrome, reverse_text


class StringToolsTests(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertFalse(is_palindrome("python"))

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")


if __name__ == "__main__":
    unittest.main()
