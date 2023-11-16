class Laptop:
    def __init__(self) -> None:
        self.color = "Black"

    def get_color(self) -> str:
        return self.color


class Bird:
    def __init__(self) -> None:
        self.color = "Brown"

    def get_color(self) -> str:
        return self.color


lp = Laptop()
bird = Bird()

for i in (lp, bird):
    print(i.get_color())
