# get input
# k = int(input())
# rooms = list(map(int,input().split()))
# print(rooms)

k = 5
rooms = [
    1,
    2,
    3,
    6,
    5,
    4,
    4,
    2,
    5,
    3,
    6,
    1,
    6,
    5,
    3,
    2,
    4,
    1,
    2,
    5,
    1,
    4,
    3,
    6,
    8,
    4,
    3,
    1,
    5,
    6,
    2,
]

# for num in rooms:
#     if rooms.count(num) < k:
#         print(num)


# k,rooms = int(input()),list(map(int, input().split()))

myset = set(rooms)

print(((sum(myset) * k) - (sum(rooms))) // (k - 1))
