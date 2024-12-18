"""Implement the keyword encoding and decoding for the Latin alphabet. The keyword cipher uses a keyword to rearrange the letters in the alphabet. You should add the provided keyword at the beginning of the alphabet. A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet. The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

Encryption:

The keyword is "Crypto"

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Example:

>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"

>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"""

from string import ascii_uppercase


class Cipher:

    _alph = list(ascii_uppercase)

    def __init__(self, keyword):
        self.keyword = keyword
        self._cipher = self.cipher

    @property
    def cipher(self):
        key_list = list(self.keyword.upper())
        redacted_alphabet = [
            char for char in self._alph if char not in key_list
        ]
        return key_list + redacted_alphabet

    def encode(self, data):
        encoded = ""
        for char in data:
            if char.upper() in self._alph:
                indx = self._alph.index(char.upper())
                encoded += (
                    self._cipher[indx].lower()
                    if char.islower()
                    else self._cipher[indx]
                )
            else:
                encoded += char

        return encoded

    def decode(self, data):
        encoded = ""
        for char in data:
            if char.upper() in self._alph:
                indx = self.cipher.index(char.upper())
                encoded += (
                    self._alph[indx].lower()
                    if char.islower()
                    else self._alph[indx]
                )
            else:
                encoded += char

        return encoded


cipher = Cipher("crypto")
# print(cipher._cipher)
print(cipher.encode("Hello world"))  # "Btggj vjmgp"
print(cipher.decode("Fjedhc dn atidsn"))  # "Kojima is genius"
