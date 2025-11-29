def is_pangram(sentence):
    import string
    from collections import Counter

    count = Counter(sentence.lower())
    if all(letter in count for letter in string.ascii_lowercase):
        return True
    return False