def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])


print(lengthOfLastWord("Hello World"), "--5")
print(lengthOfLastWord("   fly me   to   the moon  "), "--4")
print(lengthOfLastWord("luffy is still joyboy"), "--6")
