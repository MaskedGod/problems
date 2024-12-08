def romanToInt(s: str) -> int:
    alph = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    res = 0
    # Iterate through each character in the input string
    for i in range(len(s)):
        # Check if the current character is less than the next character
        if i + 1 < len(s) and alph[s[i]] < alph[s[i + 1]]:
            # If so, subtract its value (indicates a subtractive combination)
            res -= alph[s[i]]
        else:
            # Otherwise, add its value to the result
            res += alph[s[i]]

    return res


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("XI"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
