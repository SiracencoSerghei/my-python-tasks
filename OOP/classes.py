
class Character:
    name = None
    x = None
    y = None
    hp = 100
    pm = 100
    def move():
        print('I moved')



char_1 = Character()
char_2 = Character()
print(char_1)
print(char_2)
print(char_1.hp)
print(char_2.name)
char_1.name = "Edelweiss"
char_2.name = "Gabriel"
print(char_1.name)
print(char_2.name)
Character.hp = 300
print(char_1.hp)
Character.name = "AZE"
print(char_1.name)
print(char_2.name)
char_3 = Character()
print(char_3.name)
# if override first - not changed
print(char_2.name)


