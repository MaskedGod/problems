from time import sleep, time


def log(fn):

    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        exec_time = round(end_time - start_time, 2)

        arg_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
        arg_values = [
            f"{name}={value}" for name, value in zip(arg_names, args)
        ]

        kwarg_values = [f"{key}={value}" for key, value in kwargs.items()]
        print(arg_names)
        print(arg_values)
        print(kwarg_values)
        with open("log.txt", "a") as file:
            log_message = (
                f"{fn.__name__}; "
                f"args: {', '.join(arg_values)}; "
                f"kwargs: {', '.join(kwarg_values)}; "
                f"execution time: {exec_time} sec.\n"
            )
            file.write(log_message)

        return result

    return wrapper


# foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
@log
def foo(a, b, c):
    sleep(0.12)
    return a + b + c


# print(foo.__code__.co_varnames)
print(foo(1, 2, c=3))
