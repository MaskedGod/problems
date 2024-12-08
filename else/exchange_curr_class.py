from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    name = "Base Class"
    rates = {"EUR": 1, "USD": 2, "GBP": 100}

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        cls_rate = cls.rates[cls.name]
        other_cls_rate = cls.rates[other_cls.name]

        course_value = other_cls_rate / cls_rate

        return f"{course_value} {other_cls.name} for 1 {cls.name}"

    def convert_value(self, other_cls: Type[Currency]) -> float:
        cls_rate = self.rates[self.name]
        other_cls_rate = self.rates[other_cls.name]

        rate = other_cls_rate / cls_rate
        converted_value = self.value * rate

        return converted_value

    def to_currency(self, other_cls: Type[Currency]):
        exchange_value = self.convert_value(other_cls)

        return other_cls(exchange_value)

    def __str__(self) -> str:
        return f"{self.value} {self.name}"

    def __add__(self, other: object) -> str:
        other_value_converted = other.convert_value(type(self))
        # Return an instance of the same class as self with the new value
        return type(self)(self.value + other_value_converted)

    def __lt__(self, other: object) -> bool:
        other_currency_converted = other.convert_value(self)
        return self.value < other_currency_converted

    def __gt__(self, other: object) -> bool:
        other_currency_converted = other.convert_value(self)
        return self.value > other_currency_converted

    def __eq__(self, other: object) -> bool:
        other_currency_converted = other.convert_value(self)
        return self.value == other_currency_converted


class Euro(Currency):
    name = "EUR"

    def __init__(self, value: float):
        super().__init__(value)


class Dollar(Currency):
    name = "USD"

    def __init__(self, value: float):
        super().__init__(value)


class Pound(Currency):
    name = "GBP"

    def __init__(self, value: float):
        super().__init__(value)


# # print(
# #     f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
# #     f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
# #     f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
# # )
# e = Euro(100)
# r = Pound(100)
# d = Dollar(200)
# print(
#     f"e = {e}\n"
#     f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
#     f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
#     f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
# )
# """  e = 100 EUR
#   e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
#   e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
#   e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed"""

# print(
#     f"r = {r}\n"
#     f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
#     f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
#     f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
# )
# """  r = 100 GBP
#   r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
#   r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
#   r.to_currency(Pound) = 100.0 GBP  # Pound instance printed"""

# print(f"e + r  =>  {e + r}\n" f"r + d  =>  {r + d}\n" f"d + e  =>  {d + e}\n")
# #   e + r  =>  101.0 EUR  # Euro instance printed
# #   r + d  =>  10100.0 GBP  # Pound instance printed
# #   d + e  =>  400.0 USD  # Dollar instance printed
p = Pound(30)
print(p.to_currency(Euro))
