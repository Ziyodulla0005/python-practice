def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


if __name__ == "__main__":
    print(reverse_text("python"))
