def flatten(iterable):
    flat = []
    for item in iterable:
        # print(item)
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)

    flat = [item for item in flat if item is not None]

    return flat


print(flatten([1, [2, 3, None, 4], [None], 5]))  # [1,2,3,4,5]
print(flatten([0, 1, 2]))  # [0, 1, 2]
print(flatten([1, 2, None]))  # [1, 2]
print(
    flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8])
)  # [1, 2, 3, 4, 5, 6, 7, 8]
