from string import ascii_lowercase

alph = ascii_lowercase[::-1]


def encode(plain_text):
    encoded = []
    i = 0
    for char in plain_text.lower():
        if char.isalpha():
            i += 1
            new_char_index = ascii_lowercase.index(char)
            encoded.append(alph[new_char_index])
        elif char.isnumeric():
            i += 1
            encoded.append(char)
        else:
            continue
        if i % 5 == 0:
            encoded.append(" ")

    return "".join(encoded).rstrip()


def decode(ciphered_text):
    decoded = []
    for char in ciphered_text.replace(" ", ""):
        if char.isalpha():
            new_char_index = alph.index(char)
            decoded.append(ascii_lowercase[new_char_index])
        elif char.isnumeric():
            decoded.append(char)

    return "".join(decoded)


# print(encode("abc"), "zyx")
# print(encode("test"), "gvhg")
# print(encode("x123 yes"), "c123b vh")
# print(encode("mindblowingly"), "nrmwy oldrm tob")

print(encode("Testing,1 2 3, testing."), "--gvhgr mt123 gvhgr mt")
print(encode("Truth is fiction."), "--gifgs rhurx grlm")
print(
    encode("The quick brown fox jumps over the lazy dog."),
    "--gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt",
)


# print(decode("gvhg"), "test")
# print(
#     decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"),
#     "thequickbrownfoxjumpsoverthelazydog",
# )
