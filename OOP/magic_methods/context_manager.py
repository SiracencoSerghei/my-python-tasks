class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position_dict = {"x": self.x, "y": self.y}
        self.position_list = [self.x, self.y]

    def __str__(self):
        original_str = super().__str__()
        return original_str

    def __repr__(self):
        original_repr = super().__repr__()
        return original_repr

    def __getitem__(self, item):
        if isinstance(item, str) and item in self.position_dict:
            return self.position_dict[item]
        elif isinstance(item, int) and 0 <= item < len(self.position_list):
            return self.position_list[item]
        else:
            raise KeyError("Key could be 'x' or 'y' for strings and 0 or 1 for integers.")

    def __setitem__(self, key, value):
        if isinstance(key, str) and key in self.position_dict:
            self.position_dict[key] = value
            if key == "x":
                self.x = value
                self.position_list[0] = self.position_dict[key]
            elif key == "y":
                self.y = value
                self.position_list[1] = self.position_dict[key]
            else:
                raise KeyError("Key could be 'x' or 'y' for strings.")
        elif isinstance(key, int):
            if key == 0:
                self.x = value
                self.position_list[0] = value
                self.position_dict["x"] = self.position_list[0]
            elif key == 1:
                self.y = value
                self.position_list[1] = value
                self.position_dict["y"] = self.position_list[1]
            else:
                raise KeyError("Key could be 0 or 1 for integers.")
        else:
            raise KeyError("Key could be 'x' or 'y' for strings and 0 or 1 for integers.")

    def __call__(self, a):
        print(f"This object has been called with arg {a}")
        print(f'{self.position_list}')

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Finishing context manager')
        if exc_type is not None:
            print(f"There was exception: {exc_type} : {exc_val} \n{exc_tb}")
        else:
            print("No problem")

char_position = Position(10, 30)
print(char_position)
# with char_position as cp:
#     print("hello")
#     # TypeError: 'Position' object does not support the context manager protocol

with char_position as cp:
    # raise ValueError("azerty")
    print("hello")
    print(cp.x)
    # print(cp.Z)
