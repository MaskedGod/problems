from time import sleep, time
from typing import Dict

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """

    def wrapper(*args):
        global execution_time
        start_timer = time()
        result = fn(*args)
        stop_timer = time()
        execution_time[fn.__name__] = stop_timer - start_timer
        return result

    return wrapper


@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b


print(func_add(10, 20))
print(execution_time["func_add"])
