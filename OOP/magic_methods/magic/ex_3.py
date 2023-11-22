# Методи __repr__ и __str__
class Car:
    name = 'GoIT'

    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.name}: {self.mark}.{self.model}'

    def __repr__(self):
        return f"Car({self.year}, '{self.mark}', '{self.model}', '{self.color}')"


car = Car(2022, 'Toyota', 'Camry', 'Black')
print(car)  # print(str(car))
print(repr(car))
