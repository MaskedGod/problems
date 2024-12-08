# | Function  | Time Complexity    | Space Complexity |
# |-----------|--------------------|------------------|
# | `strStr1` | \(O(n + m)\)        | \(O(1)\)         |
# | `strStr2` | \(O(n * k)\)    | \(O(k)\)         |
# def strStr(haystack: str, needle: str) -> int:
#     return haystack.find(needle)


# sliding window or what it's called
def strStr(haystack: str, needle: str) -> int:
    k = len(needle)
    for i in range(len(haystack)):
        if needle in haystack[i : i + k]:
            return i
    return -1


print(strStr("sadbutsad", "sad"), "-0")
print(strStr("leetcode", "leeto"), "-1")
