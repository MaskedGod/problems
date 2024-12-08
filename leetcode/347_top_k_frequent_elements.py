from collections import defaultdict
import heapq

# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     """
#     Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#     O(nlogn)
#     O(n)
#     """
#     hash_mappy = {}

#     for num in nums:
#         if num not in hash_mappy:
#             hash_mappy[num] = 1
#         else:
#             hash_mappy[num] += 1
#     hash_mappy = dict(
#         sorted(hash_mappy.items(), key=lambda item: item[1], reverse=True)
#     )
#     res = [x for x in hash_mappy.keys()]

#     return res[:k]


def topKFrequent_heap(nums: list[int], k: int) -> list[int]:
    """
    O(nlogk)
    """
    # Step 1: Frequency map
    # Similar to the previous approach, we use defaultdict to count the frequency of each number
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # Step 2: Use a heap to keep track of top k elements
    # In Python, heapq is a min-heap, so it stores the smallest element at the root
    # We'll store (-frequency, num) to sort by the largest frequency
    heap = []

    for num, freq in freq_map.items():
        # Push the tuple (-freq, num) onto the heap, so we can sort by frequency (higher first)
        heapq.heappush(heap, (freq, num))  # Insert the element (freq, num)

        # If the size of the heap exceeds k, we remove the smallest frequency element
        if len(heap) > k:
            heapq.heappop(heap)  # Removes the smallest element (min frequency)

    # Step 3: Extract the numbers from the heap (which now contains the top k elements)
    return [num for freq, num in heap]


def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Busket Sort
    O(n)

    """
    # Step 1: Frequency map using defaultdict
    # defaultdict(int) creates a dictionary where each key has a default value of 0 (like an integer counter)
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1  # Increment the count of each number in nums

    # Step 2: Create buckets where index represents frequency
    # We create an array of empty lists where the index corresponds to a frequency
    # E.g., bucket[1] contains numbers that appear once, bucket[2] contains numbers that appear twice, etc.
    bucket = [[] for _ in range(len(nums) + 1)]

    # Step 3: Fill the buckets with numbers based on their frequency
    for num, freq in freq_map.items():
        # Append the number to the bucket corresponding to its frequency
        bucket[freq].append(num)

    # Step 4: Collect the top k frequent elements
    result = []
    # Traverse the bucket array from the highest index (most frequent) to the lowest
    for i in range(len(bucket) - 1, 0, -1):  # Start from the highest frequency
        for num in bucket[i]:  # For each number in this bucket
            result.append(num)  # Add it to the result list
            if len(result) == k:  # Stop once we've added k elements
                return result


print(topKFrequent([1, 1, 1, 2, 2, 3], 2), "--[1,2]")
print(topKFrequent([1], 1), "--[1]")
print(topKFrequent([5, 5, 6, 5, 3, 2, 2], 1), "--[5]")
