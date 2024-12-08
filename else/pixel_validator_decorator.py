from typing import Callable


def validate(fn) -> Callable[..., str]:
    """Validates arguments for a pixel creation function"""

    def wrapper(*args, **kwargs) -> str:
        validation_list = [*args] + [v for v in kwargs.values()]
        if all(0 <= i <= 256 for i in validation_list):
            result = fn(*args, **kwargs)
        else:
            result = "Function call is not valid!"
        return result

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    """
    Creates a pixel at specified coordinates

    Parameters:
        x (int): horizontal coordinate
        y (int): vertical coordinate
        z (int): height coordinate
    """
    return "Pixel created!"


values = [0, 123, 234]
print(all(0 <= val <= 256 for val in values))
c = [105, 34, 10]
print(all(0 <= val <= 256 for val in c))
print(set_pixel(0, 127, z=259))
