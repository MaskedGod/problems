# Given two binary strings a and b,
# return their sum as a binary string.
def addBinary(a: str, b: str) -> str:
    bin_sum = int(a, 2) + int(b, 2)
    return bin(bin_sum)[2:]


print(addBinary("11", "1"), "100")
print(addBinary("1010", "1011"), "10101")
