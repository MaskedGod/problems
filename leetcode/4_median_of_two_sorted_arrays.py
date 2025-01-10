def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    merged = []

    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    if i < len(nums1):
        merged += nums1[i:]

    if j < len(nums2):
        merged += nums2[j:]

    merg_len = len(merged)
    res = None
    # print(merged)
    # print(merg_len)
    if merg_len % 2 == 0:
        res = (merged[merg_len // 2] + merged[(merg_len // 2) - 1]) / 2
    else:
        res = merged[merg_len // 2]
    return res


print(findMedianSortedArrays([1, 3], [2]))
# print(findMedianSortedArrays([1, 2], [3, 4]))
print(findMedianSortedArrays([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]))
