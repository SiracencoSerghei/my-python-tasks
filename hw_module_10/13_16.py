"""Як ми вже говорили, поліморфізм - це здатність програми вибирати різні реалізації при виклику операцій з однією і тією ж назвою.

Але поліморфізм - це також здатність об'єктів прикидатись чимось іншим. У наведеному вище прикладі Chupakabra прикидалася собакою та кішкою.

Для коду із завдання вам необхідно реалізувати клас CatDog, не використовуючи успадкування від класу Animal, але щоб екземпляр класу CatDog поводився як і, як екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat."""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


# Inherit from Cat, so CatDog behaves like a Cat
class CatDog(Cat):
    def __init__(self, nickname, weight):
        # Call the Cat constructor
        super().__init__(nickname, weight)


# Example usage:
cat_dog = CatDog("Fluffy", 5)
print(cat_dog.say())  # Outputs: Meow
print(cat_dog.nickname) # Outputs: Fluffy