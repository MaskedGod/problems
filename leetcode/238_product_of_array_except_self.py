def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    n = len(nums)
    # Step 1: Initialize the result array with 1s
    answer = [1] * n
    print(answer)
    # Step 2: Calculate prefix products
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]
    print(answer)
    # Step 3: Calculate suffix products and multiply with the prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        print(suffix_product)
        suffix_product *= nums[i]  # Update the suffix product

    return answer


print(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
print(productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
