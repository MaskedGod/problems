SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


# def is_superlist(l1, l2):
#     if len(l1) > len(l2):
#         return l2 in l1

#     return False


def is_sublist(l1, l2):
    if len(l1) < len(l2):
        for i in range(len(l2) - len(l1) + 1):
            sli = l2[i : i + len(l1)]
            if l2[i : i + len(l1)] == l1:
                return True

    return False


def sublist(list_one, list_two):

    res = UNEQUAL
    if list_one == list_two:
        res = EQUAL
    elif is_sublist(list_one, list_two):
        res = SUBLIST
    elif is_sublist(list_two, list_one):
        res = SUPERLIST

    return res


print(sublist([], []), EQUAL)
print(sublist([], [1, 2, 3]), SUBLIST)
print(sublist([1, 2, 3], []), SUPERLIST)
print(sublist([1, 2, 3], [1, 2, 3]), EQUAL)
print(sublist([1, 2, 3], [2, 3, 4]), UNEQUAL)

print(sublist([1, 2], [0, 1, 2, 3, 4, 5]), SUBLIST)
print(sublist([0, 1, 2, 3, 4, 5], [0, 1, 2]), SUPERLIST)
print(sublist([1, 3], [1, 2, 3]), UNEQUAL)
print(sublist([1, 2, 3], [1, 3]), UNEQUAL)
print(sublist([1, 0, 1], [10, 1]), UNEQUAL)
print(sublist(["a c"], ["a", "c"]), UNEQUAL)
print(sublist(list(range(3, 200, 3)), list(range(15, 200, 15))), UNEQUAL)
