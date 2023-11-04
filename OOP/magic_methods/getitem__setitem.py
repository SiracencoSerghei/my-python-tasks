
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


char_pos = Position(1, 2)
print(char_pos.position_list) # [1, 2]
print(char_pos.position_dict) # {'x': 1, 'y': 2}
char_pos[0] = 5
print("x", char_pos[0]) # val_x 5
print(char_pos.position_list) # [5, 2]
print(char_pos.position_dict) # {'x': 5, 'y': 2}
char_pos[1] = 10
print("y", char_pos[1]) # y 10
print(char_pos.position_list) # [5, 10]
print(char_pos.position_dict) # {'x': 5, 'y': 10}
char_pos["x"] = 50
print("x", char_pos.x) # x 50
print(char_pos.position_list) # [50, 10]
print(char_pos.position_dict) # {'x': 50, 'y': 10}
char_pos["y"] = 100
print("y", char_pos.y) # y 100
print(char_pos.position_list) # [50, 100]
print(char_pos.position_dict) # {'x': 50, 'y': 100}

# # ================
# char_pos.x = 150
# # =============
# print("x", char_pos.x) # x 150
# # ================
# char_pos.y = 250
# # =============
# print("y", char_pos.y) # x 250
# print(char_pos.position_list) # [50, 100]
# print(char_pos.position_dict) # {'x': 50, 'y': 100}


# у чому ризниця char_pos.x = 150 і char_pos["x"] = 150
#  в __setitem__ чому при char_pos.x = 150 код не працює,
#  алє тут char_pos.x = 150 print("x", char_pos.x) # x 150 працює.... може мені
#  треба викорістовувати __setattr__ ???