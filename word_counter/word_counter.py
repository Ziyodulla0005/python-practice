def count_words(text):
    return len(text.split())


def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


if __name__ == "__main__":
    print(count_words("the quick brown fox"))
