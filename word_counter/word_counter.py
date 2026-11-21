from collections import Counter


def count_words(text):
    return len(text.split())


def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def word_frequencies(text):
    words = text.lower().split()
    return Counter(words)


def most_common_words(text, limit=3):
    return word_frequencies(text).most_common(limit)


if __name__ == "__main__":
    print(count_words("the quick brown fox"))
