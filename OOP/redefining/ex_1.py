"""
Напишіть клас Adder, який має метод add, який генерує виключення NotImplemented.
Потім визначте два підкласи, які реалізують метод додавання:

а) ListAdder з методом додавання, який повертає конкатенацію двох своїх аргументів списку

б) DictAdder з методом додавання, який повертає новий словник з елементами як у два його словникові аргументи
(Підійде будь-яке визначення додавання)
"""


class Adder:
    def __add__(self, other):
        raise NotImplemented


class ListAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value  # return [*self.value, *other.value]

class DictAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return {**self.value, **other.value}


la1 = ListAdder([1, 2])
la2 = ListAdder([3, 4])
print(la1 + la2)

da1 = DictAdder({'Volodymyr': 15, 'Olga': 25})
da2 = DictAdder({'Roman': 3, 'Oxana': 11})
print(da1 + da2)

# {'Volodymyr': 15, 'Olga': 25, 'Roman': 3, 'Oxana': 11}