from string import ascii_lowercase


def alpha(letter: str) -> int:
    alphabet = list(ascii_lowercase)

    if letter.lower() in alphabet:
        x = alphabet.index(letter.lower()) + 1
        return x


sentence = list("The sunset sets at twelve o' clock.")
print(sentence)
mapped = map(alpha, list(sentence))
filtered = filter(lambda x: x is not None, mapped)
stringer = map(str, filtered)
print(" ".join(stringer))


def alphabet_position(text):
    return " ".join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
