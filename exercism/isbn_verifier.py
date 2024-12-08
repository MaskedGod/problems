# def is_valid(isbn: str):
#     # (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) % 11 == 0
#     val = [int(num) for num in isbn if num.isdigit()]
#     if isbn.endswith("X"):
#         val.append(10)

#     res = (
#         sum((num * i) for num, i in zip(val, range(10, 0, -1))) % 11 == 0
#         if len(val) == 10
#         else False
#     )
#     print(sum((num * i) for num, i in zip(val, range(10, 0, -1))))
#     return res
import re


def is_valid(isbn: str) -> bool:
    # pattern = r"^[0-9]{8}$.X?|\d?"
    pattern = r"^\d{1,9}-?\d{1,9}-?\d{1,9}-?[\dX]$"
    match = re.match(pattern, isbn)
    res = False
    if match:
        val = [int(num) for num in isbn if num.isdigit()]
        if isbn.endswith("X"):
            val.append(10)

        res = (
            sum((num * i) for num, i in zip(val, range(10, 0, -1))) % 11 == 0
            if len(val) == 10
            else False
        )

    return res


print(is_valid("3-598-21508-8"))  # True
print(is_valid("3-598-21507-X"))  # True
print(is_valid("3598215088"))  # True
print(is_valid("3-598-21508-9"))  # False
print(is_valid("3-598-21507-A"))  # False
print(is_valid("4-598-21507-B"))  # False
print(is_valid("3598P215088"))  # False
