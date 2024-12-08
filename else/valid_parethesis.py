"""string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

"""
Stack
Space complexity:
The time complexity of the solution is O(n), where n is the length of the input string. This is because we traverse the string once and perform 
constant time operations for each character.
The space complexity of the solution is O(n), where n is the length of the input string. This is because the worst-case scenario 
is when all opening brackets are present in the string and the stack will have to store them all."""


def isValid(s: str) -> bool:
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = []
    if not s:  # s empty
        return True
    elif len(s) % 2 != 0:  # s have odd number of brackets
        return False

    for bracket in s:
        if (
            bracket in brackets.keys()
        ):  # for every opening bracket ((, {, [), push it onto the stack
            stack.append(bracket)
        else:
            if (
                stack and brackets[stack[-1]] == bracket
            ):  # For every closing bracket (), }, ]), check if the stack is not empty and pop the top element
                stack.pop()
            else:
                return False

    # if (
    #     stack
    # ):  # if stack is empty, it means all open brackets found their closing bracket <3
    #     return True
    # return False
    return not stack


print(isValid("()"))
print(isValid("({}"))
print(isValid("(]"))
print(isValid("()[]{}"))
print(isValid("([])"))
print(isValid("([}}])"))
