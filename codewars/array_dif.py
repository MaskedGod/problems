def array_diff(a, b):
    return [item for item in a if item not in b]


print(array_diff([6, -3], [5, 3, 3]))
