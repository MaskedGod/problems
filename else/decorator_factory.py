from typing import Callable


def decorator_apply(lambda_func) -> Callable[..., Callable[..., int]]:
    """
    A function that applies a lambda function to the arguments of
    the decorated function and then passes the result to the decorated function.
    """

    def decorator(fn) -> Callable[..., int]:
        """Decorates a function by modifying its arguments using the specified lambda function."""

        def wrapper(*args) -> int:
            """Applying the lambda function to the arguments, before passing them to the original function."""
            new_id = lambda_func(*args)
            return fn(new_id)

        return wrapper

    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    """
    Returns the given integer, modified by the lambda function in the decorator"""
    return num


print(return_user_id(3))
print(return_user_id(43))
