def append(list1, list2):
    return list1 + list2


def concat(lists):
    flat = []
    for item in lists:
        flat += item
    return flat


def filter(function, list):
    res = [x for x in list if function(x)]
    return res


def length(list):
    res = 0
    for x in list:
        res += 1
    return res


def map(function, list):
    res = [function(x) for x in list]
    return res


def foldl(function, list, initial):
    for num in list:
        initial = function(initial, num)
    return initial


def foldr(function, list, initial):
    for num in list[::-1]:
        initial = function(initial, num)
    return int(initial)


def reverse(list):
    res = [list[x - 1] for x in range(length(list), 0, -1)]
    return res
