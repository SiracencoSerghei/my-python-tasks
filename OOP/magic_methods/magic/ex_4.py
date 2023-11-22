# Методи __getitem__ i __setitem__
from collections import UserList


class PositiveNumbers(UserList):
    def __init__(self, data=[]):
        super().__init__()
        self.data = [el for el in list(filter(lambda x: x > 0, data))]

    def __getitem__(self, item):
        if item is None:
            return self.data
        return self.data[item]

    def __setitem__(self, key, value):
        if value > 0 and key < len(self.data):
            self.data[key] = value

    def append(self, item) -> None:
        if item > 0:
            super().append(item)


nums = PositiveNumbers([2, 3, -4, 5, 6])
print(nums)
print(nums[None])
print(nums[0])
nums[0] = -3
print(nums)
nums.append(-5)
print(nums)
