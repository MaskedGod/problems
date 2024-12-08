def longestConsecutive(nums: list[int]) -> int:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
    """
    if not nums:
        return 0
    
    num_set = set(nums)  # Step 1: Store all numbers in a hash set
    longest_sequence = 0
    
    # Step 2: Iterate over each number in the array
    for num in num_set:
        # Step 3: Only start counting sequence if num is the start (num-1 isn't in the set)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Step 4: Expand the sequence by looking for consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # Step 5: Track the longest sequence found
            longest_sequence = max(longest_sequence, current_streak)

    return longest_sequence


print(longestConsecutive([100, 4, 200, 1, 3, 2]), "--4")
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), "--9")
print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]), "--7")
