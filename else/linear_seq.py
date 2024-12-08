from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    result = []

    for i in sequence:
        if isinstance(i, (int, str, float)):
            result.append(i)
        else:
            result += linear_seq(i)

    return result


sequence = [1, 2, 3, [4, 5, (6, 7)]]
sequence_2 = [1, (2, 3), [4, [5, 6], (7, 8)], 9]

print(linear_seq(sequence))
print(linear_seq(sequence_2))
