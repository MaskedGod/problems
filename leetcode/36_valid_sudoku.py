"""Row and Column Validation Together:

In one pass over the board (using indices i and j), check both the ith row and jth column simultaneously. Use two separate sets for the row and column.
For example, if you're on row i, check all the characters in that row using row_set, and simultaneously, use column_set to check the characters in the jth column.
Sub-box Validation:

Use a nested loop to iterate over each 3x3 sub-box (as you've done).
For each sub-box, reset the sub_box_set and ensure each sub-box contains unique digits without repetition."""


def isValidSudoku(board: list[list[str]]) -> bool:
    """
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    O(N squared) or O(1) hz
    """
    for row in board:
        row_set = set()
        for char in row:
            if char.isdigit() and char in row_set:
                return False
            elif char.isdigit():
                row_set.add(char)

        row_set.clear()

    for i in range(len(board)):
        column_set = set()
        for j in range(len(board)):
            char = board[j][i]
            if char.isdigit() and char in column_set:
                return False
            elif char.isdigit():
                column_set.add(char)
        column_set.clear()

    for box_row in range(
        0, 9, 3
    ):  # Traverse starting points of each 3x3 sub-box row-wise (0, 3, 6)
        sub_box_set = set()
        for box_col in range(
            0, 9, 3
        ):  # Traverse starting points of each 3x3 sub-box column-wise (0, 3, 6)
            # For each sub-box, traverse its 3x3 cells
            for i in range(3):
                for j in range(3):
                    char = board[box_row + i][
                        box_col + j
                    ]  # Access the cell within the sub-box
                    if char.isdigit() and char in sub_box_set:
                        return False
                    elif char.isdigit():
                        sub_box_set.add(char)
            print(sub_box_set)
            sub_box_set.clear()

    return True


print(
    isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    ),
    "true",
)
print(
    isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    ),
    "false",
)
print(
    isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", "1", ".", "7", "9"],
        ]
    ),
    "false",
)
