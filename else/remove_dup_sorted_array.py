"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

"""Time complexity: O(n^2), because of the repeated calls to count(i), index(i), and pop() in the worst case.
Space complexity: O(1), because no additional space is used aside from the input list, and the list is modified in place."""
# def removeDuplicates(nums: list[int]) -> int:
#     for i in nums:
#         # Assign the current number to 'sub' for comparison
#         sub = i

#         while (
#             sub == i and nums.count(i) > 1
#         ):  # While the current number matches 'sub' and it appears more than once in the list

#             nums.pop(
#                 nums.index(i)
#             )  # Remove the first occurrence of the current number from the list

#     return len(nums), nums

"""Time complexity: O(n), where n is the length of the input list.
Space complexity: O(n), since we are creating a dictionary and a new list to store the unique elements."""


def removeDuplicates(nums: list[int]) -> int:
    nums[:] = list(dict.fromkeys(nums))
    return len(nums), nums


print(removeDuplicates([1, 1, 2]), "--2, [1, 2]")
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), "--5, [0, 1, 2, 3, 4]")
print(removeDuplicates([-1, 0, 0, 0, 0, 3, 3]), "--3, [-1,0,3]")
