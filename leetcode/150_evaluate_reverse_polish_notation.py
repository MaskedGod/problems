"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

"""Might be used with "operator" library, but im using eval() cuz we don't care about safety BUT eval will use float division (/) by default, which might not give you the desired results for integer division."""


# def evalRPN(tokens: list[str]) -> int:
#     stack = []

#     for token in tokens:

#         try:
#             num = int(token)
#             stack.append(num)
#         except:
#             op_1 = stack.pop()
#             op_2 = stack.pop()

#             if token == "+":
#                 res = op_2 + op_1
#             elif token == "-":
#                 res = op_2 - op_1
#             elif token == "*":
#                 res = op_2 * op_1
#             elif token == "/":
#                 res = int(op_2 / op_1)

#             stack.append(res)

#     return stack.pop()


def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:

        if token not in "+-/*":
            stack.append(int(token))
        else:
            op_1 = stack.pop()
            op_2 = stack.pop()

            if token == "+":
                stack.append(op_2 + op_1)
            elif token == "-":
                stack.append(op_2 - op_1)
            elif token == "*":
                stack.append(op_2 * op_1)
            else:
                stack.append(int(op_2 / op_1))

    return stack.pop()


# print(evalRPN(["3", "4", "+"]))
# print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
