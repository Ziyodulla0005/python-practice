import re


def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")


def slugify(text):
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-")


def truncate(text, limit, suffix="..."):
    if len(text) <= limit:
        return text
    return text[: limit - len(suffix)] + suffix


if __name__ == "__main__":
    print(reverse_text("python"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(capitalize_words("hello brave new world"))
    print(count_vowels("programming"))
    print(slugify("Hello, World! Welcome"))
    print(truncate("A very long sentence", 12))
