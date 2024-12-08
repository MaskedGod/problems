def romanToInt(s: str) -> int:
    pass


print(romanToInt("III"), "--3")
print(romanToInt("LVIII"), "--58")
print(romanToInt("MCMXCIV"), "--1994")


def romanToInt1(s: str) -> int:
    alph = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and alph[s[i]] < alph[s[i + 1]]:
            res -= alph[s[i]]
        else:
            res += alph[s[i]]

    return res


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        summ = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i + 1]]:
                summ += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1

        return summ
        # Time: O(n)
        # Space: O(1)
