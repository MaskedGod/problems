def mergeAlternately(word1: str, word2: str) -> str:
    """You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string."""
    # 0(n)
    res = []

    if len(word1) >= len(word2):
        long, short = word1, word2
    else:
        long, short = word2, word1

    for i in range(len(short)):
        res.append(word1[i])
        res.append(word2[i])

    res.append(long[len(short) :])

    return "".join(res)


print(mergeAlternately("abc", "pqr"), "--apbqcr")
print(mergeAlternately("ap", "pqrs"), "--apbqrs")
print(mergeAlternately("abcd", "pq"), "--apbqcd")


# omg what? optimal solution u say?
def mergeAlternately2(word1: str, word2: str) -> str:
    # O(N)
    A, B = len(word1), len(word2)
    a, b = 0, 0
    s = []

    word = 1
    while a < A and b < B:
        if word == 1:
            s.append(word1[a])
            a += 1
            word = 2
        else:
            s.append(word2[b])
            b += 1
            word = 1

    while a < A:
        s.append(word1[a])
        a += 1

    while b < B:
        s.append(word2[b])
        b += 1

    return "".join(s)
