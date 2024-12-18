# def plusOne(digits: list[int]) -> list[int]:
#     add_one = str(
#         int("".join(str(num) for num in digits)) + 1
#     )  # make list into a str and then into int to add 1 and then into str :D
#     return [int(num) for num in add_one]

# def plusOne(digits: list[int]) -> list[int]:
#     # Helper function to perform the addition recursively
#     def addOne(index: int) -> list[int]:
#         # Base case: if the index is less than 0, it means we need to add a new digit
#         if index < 0:
#             return [1]  # Return [1] as we have a carry over

#         # Increment the current digit
#         digits[index] += 1

#         # Check if the incremented digit is less than 10
#         if digits[index] < 10:
#             return digits  # No carry, return the modified array

#         # If the digit is 10, set it to 0 and continue carrying over
#         digits[index] = 0
#         return addOne(index - 1)  # Recursively call for the next digit to the left

#     # Start the recursive process from the last digit
#     return addOne(len(digits) - 1)


def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1

        # If the current digit is less than 10, return the updated array
        if digits[i] < 10:
            return digits
        # If the current digit equals 10, set it to 0 and carry over to the next digit
        else:
            digits[i] = 0

    # If all digits were 9, insert 1 at the beginning to represent the carry
    digits.insert(0, 1)

    return digits


print(plusOne([1, 2, 3]), "[1, 2, 4]")
print(plusOne([4, 3, 2, 1]), "[4, 3, 2, 2]")
print(plusOne([9, 9]), "[1,0,0]")
print(plusOne([9]), "[1,0]")
print(plusOne([]), "[1]")
