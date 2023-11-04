class Position:
    def __init__(self, x, y):
        print("i am initialize instance")
        self.x = x
        self.y = y
        self.position = [self.x, self.y]

    def __str__(self):
        print("i am __str__ ")
        original_str = super().__str__()
        return original_str

    def __repr__(self):
        print("I am __repr__")
        original_repr = super().__repr__()
        return original_repr
    def __getitem__(self, item):
        return  self.position[item]

char_pos = 