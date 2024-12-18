"""Given a sorted array of distinct integers and a target value,
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""


def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        guess = (right + left) // 2
        if nums[guess] < target:
            left = guess + 1
        elif nums[guess] > target:
            right = guess - 1
        elif nums[guess] == target:
            return guess

    # If the target is not found, return the index where it would be inserted
    return left


print(searchInsert([1, 3, 5, 6], 5), "--2")
print(searchInsert([1, 3, 5, 6], 1), "--0")
print(searchInsert([1, 3, 5, 6], 2), "--1")
print(searchInsert([1, 3, 5, 6], 7), "--4")
