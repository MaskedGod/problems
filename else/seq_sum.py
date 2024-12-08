from typing import List, Tuple, Union

from altair import sequence


def seq_sum(sequence: Union[List, Tuple]) -> int:
    sum = 0

    for i in sequence:
        if isinstance(i, int):
            sum += i
        else:
            sum += seq_sum(i)

    return sum


sequence = [1, 2, 3, [4, 5, (6, 7)]]
sequence2 = [1, (2, 3), [4, [5, 6], (7, 8)], 9]
print(seq_sum(sequence))  # 28
print(seq_sum(sequence2))  # 45
