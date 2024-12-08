# def isSubsequence(s: str, t: str) -> bool:
#     #  Time complexity: O(m + n).
#     # Space complexity: O(m).
#     s: list = list(s)[::-1]
#     for char in t:
#         if not s:
#             return True
#         if s[-1] == char:
#             s.pop()

#     return not s


def isSubsequence(s: str, t: str) -> bool:
    # Time complexity: O(m*n)
    # Space complexity: O(m)
    s = list(s)
    for char in t:
        if not s:
            return True
        if s[0] == char:
            s.pop(0)

    return not s


print(isSubsequence("abc", "ahbgdc"), True)
print(isSubsequence("axc", "ahbgdc"), False)
print(isSubsequence("acb", "ahbgdc"), False)


# # using set to lower complexity to O(n) from O(n*m)
# return all(char in set(t) for char in s)


def isSubsequence2(self, s: str, t: str) -> bool:
    # algomap sol
    S = len(s)
    T = len(t)
    if s == "":
        return True
    if S > T:
        return False

    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S - 1:
                return True
            j += 1

    return False
    # Time: O(T)
    # Space: O(1)
