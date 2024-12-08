def findClosestNumber(nums: list[int]) -> int:
    """Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value."""
    # O(2n) -> O(n)
    closest = nums[0]

    for i in nums:
        if abs(i) < abs(closest):
            closest = i

    if closest < 0 and abs(closest) in nums:
        return abs(closest)

    return closest


print(findClosestNumber([-4, -2, 1, 4, 8]), "-- 1")
print(findClosestNumber([29, -8, 7, 9]), "-- 7")
print(findClosestNumber([2, -1, 1]), "-- 1")
