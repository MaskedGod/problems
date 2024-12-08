# def twoSum(nums: list[int], target: int) -> list[int]:
#     """
#     Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#     You may assume that each input would have exactly one solution, and you may not use the same element twice.
#     You can return the answer in any order.
#     Time Complexity: O(n²) because you are checking every possible pair.
#     Space Complexity: O(1) because no extra space is used apart from a few variables.
#     """
#     res = []

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 res = [i, j]
#                 return res
#     return res

# def twoSum(nums: list[int], target: int) -> list[int]:
#     """
#     Time Complexity: O(n log n) because of sorting, followed by O(n) for the two-pointer scan.
#     Space Complexity: O(1) if sorting is done in place.
#     """
#     # Sort the array and keep track of the original indices
#     nums = sorted(enumerate(nums), key=lambda x: x[1])  # [(index, value), ...]

#     low = 0
#     high = len(nums) - 1

#     # Two-pointer approach
#     while low < high:
#         sum = nums[low][1] + nums[high][1]

#         if sum == target:
#             return [nums[low][0], nums[high][0]]  # Return original indices

#         # If the sum is less than the target, move low pointer to the right
#         elif sum < target:
#             low += 1

#         # If the sum is greater than the target, move high pointer to the left
#         else:
#             high -= 1

#     return []  # In case no solution is found


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(n) because you only iterate through the array once.
    Space Complexity: O(n) because the hash map stores elements and their indices
    """
    nums_hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in nums_hash_map:
            return [nums_hash_map[complement], i]

        nums_hash_map[num] = i

    return []


print(twoSum([2, 7, 11, 15], 9), "--[0, 1]")
print(twoSum([-1, -2, -3, -4, -5], -8), "--[2, 4]")
print(twoSum([3, 2, 4], 6), "--[1, 2]")
print(twoSum([3, 3], 6), "--[0, 1]")
