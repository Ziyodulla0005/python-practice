import unittest

from string_tools import (
    capitalize_words,
    count_vowels,
    is_palindrome,
    reverse_text,
    slugify,
    truncate,
)


class StringToolsTests(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertFalse(is_palindrome("python"))

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello"), 2)

    def test_slugify(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_truncate(self):
        self.assertEqual(truncate("abcdefghij", 8), "abcde...")
        self.assertEqual(truncate("abc", 8), "abc")


if __name__ == "__main__":
    unittest.main()
