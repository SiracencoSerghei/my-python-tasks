class Motherboard:
    def __init__(self, brand: str) -> None:
        self.brand = brand


class Laptop(Motherboard):
    def __init__(self, brand: str, ram_size: int) -> None:
        super().__init__(brand)
        self.ram = ram_size


lp = Laptop("Dell", 32)
