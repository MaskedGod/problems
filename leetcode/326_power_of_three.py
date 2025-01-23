"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
"""


def is_power_of_three(n: int) -> bool:
    # return n > 0 and 3**19 % n == 0
    if n <= 0:
        return False
    # Check if the number is divisible by 3 until it's no longer divisible
    while n % 3 == 0:
        n /= 3  # Use normal division
    return n == 1  # If n becomes 1, it was a power of three


print(is_power_of_three(27))
print(is_power_of_three(9))  # true
print(is_power_of_three(0))
print(is_power_of_three(-1))
