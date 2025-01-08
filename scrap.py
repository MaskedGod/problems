class MyClass:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, MyClass) and self.value == other.value


obj1 = MyClass(1)
obj2 = MyClass(2)
obj3 = MyClass(1)

my_set = {obj1, obj2, obj3}
print(my_set)
print(obj1, obj2, obj3)
