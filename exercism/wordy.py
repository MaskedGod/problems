# if len(parsed) == 1 and numbers == 1:
#     return "".join(parsed)
# elif len(parsed) == 0:
#     raise ValueError("syntax error")
# elif not known_operator:
#     raise ValueError("unknown operation")
# if not known_operator and numbers > 0:
#     raise ValueError("unknown operation")
# if len(operators) > len(numbers) or len(operators) == len(numbers):
#     raise ValueError("syntax error")


def answer(question: str) -> int:
    """
    Parse and evaluate simple math word problems returning the answer as an integer.
    """
    ops = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied": lambda x, y: x * y,
        "divided": lambda x, y: x // y,
    }
    if not question.startswith("What is") and question.endswith("?"):
        raise ValueError("syntax error")

    parsed = question.replace("What is", "").replace("by ", "").replace("?", "").split()
    known_operator = any(char in ops.keys() for char in parsed)
    operators = [char for char in parsed if char in ops]
    numbers = [int(char) for char in parsed if char.lstrip("-").isdigit()]
    print(parsed)
    print(operators)
    print(numbers)

    if not known_operator and len(parsed) == 1:
        return numbers[0]
    elif not known_operator and len(parsed) == 0:
        raise ValueError("syntax error")
    elif len(operators) == len(numbers):
        raise ValueError("syntax error")
    elif len(operators) + 1 != len(numbers):
        raise ValueError("syntax error")
    elif (
        parsed[0].isalpha()
        and known_operator
        or parsed[-1].isalpha()
        and known_operator
    ):
        raise ValueError("syntax error")
    elif not known_operator and len(numbers) >= 1:
        raise ValueError("unknown operation")

    def calculate_expression(parsed):
        if len(parsed) == 1:
            return int(*parsed)

        operation = ops.get(parsed[1])
        num1 = int(parsed[0])
        num2 = int(parsed[2])

        result = operation(num1, num2)

        return calculate_expression([str(result)] + parsed[3:])

    return calculate_expression(parsed)


print(answer("What is 5?"))  # 5
print(answer("What is 52 cubed?"))  # unknown
# print(answer("What is?"))  # syntax
# print(answer("What is plus 1 2?"))  # syntax
# print(answer("What is 5 plus 13?"))  # 18
print(answer("What is 7 minus 5?"))  # 2
# print(answer("What is 6 multiplied by 4?"))  # 24
# print(answer("What is 25 divided by 5?"))  # 5
# print(answer("What is 5 plus 13 plus 6?"))  # 24
# print(answer("What is 3 plus 2 multiplied by 3?"))  # 15
# print(answer("What is -1 plus -10?"))  # -11
