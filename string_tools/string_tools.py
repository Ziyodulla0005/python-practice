def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")


if __name__ == "__main__":
    print(reverse_text("python"))
