# Логічні операції

class Car:
    store_name = 'GoIT store'

    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return (f'{self.store_name}: {self.mark} -> {self.model}, {self.price}')

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


car_w = Car(2019, 'BMW', 'X5', 'Black', 21000)
car_b = Car(2022, 'Toyota', 'Camry', 'White', 28000)

print(car_w == car_b)
print(car_w != car_b)
print(car_w < car_b)
print(car_w > car_b)
print(car_w <= car_b)
print(car_w >= car_b)
