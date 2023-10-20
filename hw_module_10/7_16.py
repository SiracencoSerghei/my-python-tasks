"""Для минулого завдання додамо клас Owner — власника собаки. У класу є три атрибути: 
ім'я — name, вік — age та адреса — address. Також необхідно реалізувати метод info, 
який повертає словник з ключами 'name', 'age' і 'address', та значення яких дорівнюють 
відповідним властивостям екземпляра класу.

Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner. Додати до
класу Dog метод who_is_owner, який повертає результат виклику методу info екземпляра
класу Owner, тобто це словник з ключами name, age та address власника."""

class Animal:
    """class Animal"""
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        """method say for animal"""
        pass

    def change_weight(self, weight):
        """method change weight"""
        self.weight = weight


class Owner:
    """class owner"""
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def info(self):
        """method info owner"""
        return {
            "Name":self.name,
            "Age":self.age,
            "Address":self.address
        }

class Dog(Animal):
    """class dog"""
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        """dog method return owner info"""
        return self.owner.info()
# Створення екземпляру класу Owner
owner = Owner("Sergio", 35, "Spoorweglaan 30")

# Створення екземпляру класу Dog з власником
dog = Dog("Barbos", 23, "labrador", owner)

print(f"Ім'я собаки: {dog.nickname}")
print(f"Вага собаки: {dog.weight} кг")
print(f"Порода собаки: {dog.breed}")
print(f"Собака каже: {dog.say()}")
print(f"Власник собаки: {dog.who_is_owner()}")
