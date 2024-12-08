def is_paired(input_string: str) -> bool:
    if not input_string:
        return True
    bracket_pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in input_string:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:

            if stack and stack[-1] == bracket_pairs[char]:
                print(stack)
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(is_paired(""), True)
print(is_paired("[["), False)
print(is_paired("}{"), False)
print(is_paired("{]"), False)
print(is_paired("{ }"), True)
print(is_paired("{[])"), False)
print(is_paired("([{}({}[])])"), True)
print(is_paired("{what is (42)}?"), True)
