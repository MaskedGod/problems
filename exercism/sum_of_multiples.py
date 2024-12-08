def sum_of_multiples(limit, multiples: list):
    all_multi = []
    for num in multiples:
        if num > 0:
            x = num
            while x < limit:
                all_multi.append(x)
                x += num
    return sum(set(all_multi))


print(sum_of_multiples(20, [3, 5]))  # , 78)
print(sum_of_multiples(1, [3, 5]))  # , 0)
print(sum_of_multiples(4, [3, 5]))  # , 3)
print(sum_of_multiples(7, [3]))  # , 9)
print(sum_of_multiples(10, [3, 5]))  # , 23)
print(sum_of_multiples(10000, [43, 47]))  # 2203160
print(sum_of_multiples(1, [0]))  # 0
