class Character:
    # name = None
    # x = None
    # y = None
    hp = 100
    pm = 100
    count = 0
    # def __init__(self):
    #     print("Init new instance")
    #     self.name = None
    #     self.x = None
    #     self.y = None
    #     Character.count += 1
    def __init__(self, name, x, y):
        print("Init new instance, Total: ", end=" ")
        self.name = name
        self.x = x
        self.y = y
        Character.count += 1

    def move(self):
        print('I moved')

    def identify(self):
        print(self.name)
        self.move()


# char_1 = Character()
# print(Character.count)
char_1 = Character("Sergio", 0, 0)
print(Character.count)
print(char_1.name)
print(char_1.x)
print(char_1.y)

char_2 = Character("Pietro", 1, 1)
print(Character.count)
print(char_2.name)
print(char_2.x)
print(char_2.y)

