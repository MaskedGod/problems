def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    for chars in candidates:
        if word.lower() == chars.lower():
            candidates.remove(chars)
    res = []
    word_ls = sorted(word.lower())
    for chars in candidates:
        chars_ls = sorted(chars.lower())
        if len(word_ls) == len(chars_ls):
            # if all(char in chars_ls for char in word_ls):
            if all(
                chars_ls.count(char) == word_ls.count(char)
                for char in chars_ls
            ):
                res.append(chars)
    return res


print(find_anagrams("diaper", ["hello", "world", "zombies", "pants"]))  # []
print(
    find_anagrams("solemn", ["lemons", "cherry", "melons"])
)  # ["lemons", "melons"]
print(find_anagrams("nose", ["Eons", "ONES"]))  # ["Eons", "ONES"]
print(find_anagrams("tapper", ["patter"]))  # []
print(find_anagrams("Banana", ["BANANA"]))  # []
