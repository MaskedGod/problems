from string import ascii_lowercase, ascii_uppercase

# def rotate(text, key):
#     cyphered = []
#     for letter in text.lower():
#         let = (ascii_lowercase.index(letter) + key) % 26
#         cyphered.append(ascii_lowercase[let])
#     return "".join(cyphered)


# def rotate(text, key):
#     cyphered = [
#         ascii_lowercase[(ascii_lowercase.index(letter) + key) % 26] for letter in text
#     ]
#     return "".join(cyphered)


def rotate(text: str, key):
    cyphered = []
    for char in text:
        if char.isalpha():
            new_letter = (ascii_lowercase.index(char.lower()) + key) % 26
            if char.islower():
                cyphered.append(ascii_lowercase[new_letter])
            else:
                cyphered.append(ascii_uppercase[new_letter])
        else:
            cyphered.append(char)
    return "".join(cyphered)


print(rotate("abcdefghijklmnopqrstuvwxyz", 13))  # nopqrstuvwxyzabcdefghijklm
print(rotate("omg", 5))  # trl
print(rotate("OMG", 5))  # TRL
