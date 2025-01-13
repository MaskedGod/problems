"""Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise."""


def canConstruct(s: str, k: int) -> bool:
    if len(s) < k:
        return False


print(canConstruct("annabelle", 2))
"""
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
"""
print(canConstruct("leetcode", 3))
"""
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
"""
print(canConstruct("true", 4))
"""
Output: true
Explanation: The only possible solution is to put each character in a separate string.
"""
