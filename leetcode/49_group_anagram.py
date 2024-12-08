def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams
    together. You can return the answer in any order.
    Time Complexity: Sorting each word takes O(k log k), where k is the length of the word, and doing this for all n words gives O(n * k log k). The space complexity is O(nk) for storing the groups
    """
    # hash_map = {set(k): v for (k, v) in zip(strs, strs)}
    hash_map = {}

    for el in strs:
        sorted_el = "".join(sorted(el))
        if sorted_el not in hash_map.keys():
            hash_map[sorted_el] = [el]
        else:
            hash_map[sorted_el] += [el]

    return [val for val in hash_map.values()]


print(
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
    '\n[["bat"],["nat","tan"],["ate","eat","tea"]]',
)
print(groupAnagrams([""]), '\n[[""]]')
print(groupAnagrams(["a"]), '\n[["a"]]')
