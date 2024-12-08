class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """

    def __get__(self, obj, objtype=None):
        return getattr(obj, "_price")

    def __set__(self, obj, value):
        if 0 <= value <= 100:
            setattr(obj, "_price", value)
        else:
            raise ValueError("Price must be between 0 and 100.")


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if hasattr(obj, self.private_name):
            raise ValueError(f"{self.public_name.capitalize()} can not be changed.")
        setattr(obj, self.private_name, value)


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price) -> None:
        self.author = author
        self.name = name
        self.price = price


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
b.price = 100
