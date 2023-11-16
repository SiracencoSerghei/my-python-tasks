class LaptopNameError(Exception): ...


class Laptop:
    def __init__(self, name: str) -> None:
        if len(name) < 2:
            raise LaptopNameError("Name must be grater then 1 symbols")
        self.name = name


try:
    lp1 = Laptop("H")
except LaptopNameError as e:
    print(e)
