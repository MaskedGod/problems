"""A singleton is a class that only allows a single instance of itself to be created and gives access to that created instance. Implement singleton logic inside your custom class using a method to initialize a class instance.

Example:

>>> p = Sun.inst()
>>> f = Sun.inst()
>>> p is f
True
"""


class Sun:
    _instance = None

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Sun, cls).__new__(cls)
        return cls._instance

    @classmethod
    def inst(cls):
        return cls._instance


p = Sun.inst()
f = Sun.inst()

print(p is f)
