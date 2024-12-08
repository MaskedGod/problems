"""Create generic union and intersect functions to work with sets. The functions must accept an arbitrary number of arguments of different types: list, tuple, and set. Each function must return the value of the set type"""


def union(*args) -> set:
    result = []
    for arg in args:
        for char in arg:
            result.append(char)

    return set(result)


def intersect(*args) -> set:
    result = list(args[0])

    for arg in args:
        for char in result[:]:
            if char not in arg:
                result.remove(char)

    return set(result)


print(union(("S", "A", "M"), ["S", "P", "A", "C"]))  # {'S', 'P', 'A', 'M', 'C'}

print(intersect(("S", "A", "C"), ("P", "C", "S"), ("G", "H", "S", "C")))  # {'S', 'C'}
print(intersect(("S", "A", "C"), ("P", "C"), ("G", "H")))
