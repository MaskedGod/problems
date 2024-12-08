def append(list1, list2):
    if not list1:
        return list2

    head = list1[0]
    tail = list1[1:]

    return [head] + append(tail, list2)


# dumbest thing ever

# print((append([1, 2], [3, 4])))  # , [1, 2, 3, 4]))


def concat(lists):
    if not lists:
        return []

    head = lists[0]
    tail = lists[1:]

    return head + concat(tail)


# print(concat([[1, 2], [3], [], [4, 5, 6]]))  # [1, 2, 3, 4, 5, 6]


def filter(function, list):
    pass


def length(list):
    if not list:
        return 0

    tail = list[1:]

    return 1 + length(tail)


# print(length([1, 2, 3, 4, 5])) #5


def mapper(function, list):
    # Base case: when the list is empty, return an empty list
    if not list:
        return []

    # Recursively process the first element (head) and tail
    head = list[0]
    tail = list[1:]

    # Apply the function to the head and append the result to the recursive call on the tail
    return [function(head)] + mapper(function, tail)


# Explanation of 3 iterations:
# 1st iteration: head = 1, tail = [3, 5, 7], result = [2] + mapper([3, 5, 7])
# 2nd iteration: head = 3, tail = [5, 7], result = [4] + mapper([5, 7])
# 3rd iteration: head = 5, tail = [7], result = [6] + mapper([7])


# print(mapper(lambda x: x + 1, [1, 3, 5, 7]))


def foldl(function, list, initial):
    # Base case: when the list is empty, return the initial accumulator value
    if not list:
        return initial

    # Recursively apply the function with the head of the list and the accumulator
    head = list[0]
    tail = list[1:]

    # Pass the result as the new accumulator (left fold)
    return foldl(function, tail, function(head, initial))


# Explanation of 3 iterations:
# 1st iteration: head = 1, tail = [2, 3, 4], initial = 5, result = foldl([2, 3, 4], function(1, 5)) => foldl([2, 3, 4], 6)
# 2nd iteration: head = 2, tail = [3, 4], initial = 6, result = foldl([3, 4], function(2, 6)) => foldl([3, 4], 8)
# 3rd iteration: head = 3, tail = [4], initial = 8, result = foldl([4], function(3, 8)) => foldl([4], 11)

# print(foldl(lambda ini, el: el + ini, [1, 2, 3, 4], 5))


def foldr(function, list, initial):
    # Base case: when the list is empty, return the initial accumulator value
    if not list:
        return initial

    # Recursively process the tail and apply the function on the way back
    head = list[0]
    tail = list[1:]

    # Apply the function to the result of the recursive call and the head (right fold)
    return function(foldr(function, tail, initial), head)


# Explanation of 3 iterations:
# 1st iteration: head = 1, tail = [2, 3, 4], result = function(foldr([2, 3, 4], 24), 1)
# 2nd iteration: head = 2, tail = [3, 4], result = function(foldr([3, 4], 24), 2)
# 3rd iteration: head = 3, tail = [4], result = function(foldr([4], 24), 3)

# print(foldr(lambda ini, el: el / ini, [1, 2, 3, 4], 24))


def reverse(list):
    # Base case: when the list is empty, return an empty list
    if not list:
        return []

    # Recursively process the tail, then append the head at the end
    head = list[0]
    tail = list[1:]

    # Append the head to the result of reversing the tail
    return reverse(tail) + [head]


# Explanation of 3 iterations:
# 1st iteration: head = 1, tail = [2, 3, 4, 5], result = reverse([2, 3, 4, 5]) + [1]
# 2nd iteration: head = 2, tail = [3, 4, 5], result = reverse([3, 4, 5]) + [2]
# 3rd iteration: head = 3, tail = [4, 5], result = reverse([4, 5]) + [3]

# print(reverse([1, 2, 3, 4, 5]))
