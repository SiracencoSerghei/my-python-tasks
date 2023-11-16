from collections import UserDict


class Box(UserDict):
    def add_if_not_exist(self, key, item):
        if self.data.get(key):
            return None
        self.data[key] = item
        return item


box = Box()

box.add_if_not_exist("food", "banana")

print(box)

box.add_if_not_exist("food", "kiwi")

print(box)
