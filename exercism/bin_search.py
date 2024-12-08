def find(search_list, value):
    max_val = len(search_list) - 1
    low_val = 0

    while low_val <= max_val:
        guess = (max_val + low_val) // 2

        if search_list[guess] < value:
            low_val = guess + 1
        elif search_list[guess] > value:
            max_val = guess - 1
        else:
            return guess
    raise ValueError("value not in array")


print(find([1, 3, 4, 6, 8, 9, 11], 6))  # 3
print(find([1, 3, 4, 6, 8, 9, 11], 8))  # 4
print(find([1, 3, 4, 6, 8, 9, 11], 1))  # 0
print(find([1, 3, 4, 6, 8, 9, 11], 12))  # raise
