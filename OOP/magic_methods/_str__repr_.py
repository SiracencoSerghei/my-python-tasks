class Position:
    def __init__(self, x, y):
        print("i am initialize instance")
        self.x = x
        self.y = y

    def __str__(self):
        print("i am __str__ ")
        original_str = super().__str__()
        return f"{original_str}__str__"

    def __repr__(self):
        print("I am __repr__")
        original_repr = super().__repr__()
        return f"{original_repr}__repr__"


char_pos = Position(1, 2) # i am initialize instance
# print(str(char_pos))  # <__main__.Position object at 0x7fcc5eb22390>
print(str(char_pos))  # <__main__.Position object at 0x7f698e722790>a



