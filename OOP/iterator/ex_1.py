"""
Протокол ітератора в Python реалізований методом __iter__. Цей метод має повертати ітератор.
Ітератором може бути будь-який об'єкт, який має метод __next__, який при кожному виклику повертає значення.
Щоб створити ітератор, достатньо реалізувати метод __next__.
"""

from random import randint


class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)


my_random_list = RandIterator(0, 200, 10)

for random_range in my_random_list:
    print(random_range, end=' ')


a = [1, 3, 4]
print(type(a))
b = list()