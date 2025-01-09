"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# O(N)


def isPalindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    clean = "".join(filter(lambda char: char.isalnum(), s.lower()))
    left = 0
    right = len(clean) - 1

    # if not clean:
    #     return False

    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome(".,"))
