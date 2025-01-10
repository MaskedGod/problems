"""You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order."""

# not working
# def wordSubsets(words1, words2):
#     words2_len = len(words2)
#     res = {k: [] for k in range(words2_len + 1)}

#     for word in words1:
#         counter = 0
#         for sub in words2:
#             if sub in word:
#                 counter += 1
#         res[counter].append(word)
#     print(res)
#     return res[words2_len]


# def wordSubsets(words1, words2):

#     def count_frequencies(word):
#         freq = [0] * 26
#         for char in word:
#             freq[ord(char) - ord("a")] += 1
#         return freq

#     max_freq = [0] * 26
#     for word in words2:
#         word_freq = count_frequencies(word)
#         for i in range(26):
#             max_freq[i] = max(max_freq[i], word_freq[i])

#     result = []
#     for word in words1:
#         word_freq = count_frequencies(word)
#         if all(word_freq[i] >= max_freq[i] for i in range(26)):
#             result.append(word)

#     return result

from collections import Counter


def wordSubsets(words1, words2):
    res = []

    max_freq_words2 = Counter()

    for word in words2:
        word_freq = Counter(word)
        for char in word_freq:
            max_freq_words2[char] = max(max_freq_words2[char], word_freq[char])

    for word in words1:
        word_freq = Counter(word)
        is_universal = True
        for char in max_freq_words2:
            if word_freq[char] < max_freq_words2[char]:
                is_universal = False
                break
        if is_universal:
            res.append(word)

    return res


print(
    wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"])
)  # ["facebook","google","leetcode"]
print(
    wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"])
)  # ["apple","google","leetcode"]
print(
    wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"])
)  # ["google","leetcode"]
