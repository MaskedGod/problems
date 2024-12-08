def longestCommonPrefix(strs: list[str]) -> str:
    """Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    O(n*m)
    O(1)
    """
    prefix = strs[0]

    for s in strs[1:]:
        # Compare characters in prefix and the current string
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        # Update prefix to the common part found
        prefix = prefix[:i]

        # Early exit if the prefix becomes empty
        if not prefix:
            return ""

    return prefix


print(longestCommonPrefix(["ab", "a"]), "--a")
print(longestCommonPrefix(["flower", "flow", "flight"]), "--fl")
print(longestCommonPrefix(["dog", "racecar", "car"]), "--")


def longestCommonPrefix2(strs: list[str]) -> str:
    prefix = min(strs, key=len)

    for i in strs:
        while len(prefix) > 0:
            if i.startswith(prefix):
                break
            else:
                prefix = prefix[:-1]
    return prefix


def longestCommonPrefix3(strs: list[str]) -> str:
    min_length = float("inf")

    for s in strs:
        if len(s) < min_length:
            min_length = len(s)

    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1

    return strs[0][:i]
