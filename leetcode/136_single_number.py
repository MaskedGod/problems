"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from collections import Counter

# def singleNumber(nums: list[int]) -> int:
#     total = 0

#     for num in nums:
#         total ^= num

#     return total


def singleNumber(nums: list[int]) -> int:
    freq = Counter(nums)
    res = None
    for k, v in freq.items():
        if v == 1:
            res = k
    return res


print(singleNumber([2, 2, 1]))
print(singleNumber([1, 0, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
