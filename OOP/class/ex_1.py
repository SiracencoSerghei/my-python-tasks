class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None
        # Setter
        self.name = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError('Тварина має мати імя')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError('Не вірний вік для тварини')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError('Не вірна вага для тварини')


a = Animal('Boris', 12, 1500)
print(a.name, a.age, a.weight)


a = Animal('Boris', -2, 1500)
print(a.name, a.age, a.weight)
a.age = -15
print(a.name, a.age, a.weight)