def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an
    anagram of s, and false otherwise.
    """
    return sorted(s) == sorted(t)


print(isAnagram("anagram", "nagaram"), True)
print(isAnagram("rat", "car"), False)
print(isAnagram("dodo", "odod"), True)
print(isAnagram("aa", "a"), False)
