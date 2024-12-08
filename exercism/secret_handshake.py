def commands(binary_str: str) -> list:
    """
    00001 = wink
    00010 = double blink
    00100 = close your eyes
    01000 = jump
    10000 = Reverse the order of the operations in the secret handshake.
    """
    res = []
    octo = int(binary_str, 2)
    if int(binary_str, 2) < 1 and int(binary_str, 2) > 31:
        return res

    for i, char in enumerate(binary_str[::-1]):
        if i == 0 and int(char):
            res.append("wink")
        elif i == 1 and int(char):
            res.append("double blink")
        elif i == 2 and int(char):
            res.append("close your eyes")
        elif i == 3 and int(char):
            res.append("jump")
        elif i == 4 and int(char):
            res = res[::-1]
    return res


print(commands("00001"))  # ["wink"]
print(commands("00010"))  # ["double blink"]
print(commands("00100"))  # ["close your eyes"]
print(commands("01000"))  # ["jump"]
print(commands("00011"))  # ['wink', 'double blink']
print(commands("10011"))  # ['double blink', 'wink']
print(commands("11000"))  # ['jump']
print(commands("10000"))  # []
print(commands("01111"))  # ['wink', 'double blink', 'close your eyes', 'jump']
print(commands("11111"))  # ['jump', 'close your eyes', 'double blink', 'wink']
print(commands("00000"))  # []
