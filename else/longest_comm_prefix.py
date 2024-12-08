# def longestCommonPrefix(strs: list[str]) -> str:
#     pref = strs[0]
#     for word in strs:
#         for letter in pref:
#             if letter not in word:
#                 pref = "".join(pref.split(letter))
#     return pref

# Approach 1: Horizontal scanning


def longestCommonPrefixn(strs: list[str]) -> str:
    """
    If strs[i].find(prefix) != 0, it means that the prefix is not a prefix of strs[i],
    so the code inside the loop reduces the prefix by one character
    from the end (prefix = prefix[0 : len(prefix) - 1]).
    This continues until either prefix is found at the start of strs[i]
    (where strs[i].find(prefix) == 0) or the prefix becomes an empty string.
    """
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0 : len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix


def longestCommonPrefix(strs: list[str]) -> str:
    if strs == None or len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["cir", "car"]))
