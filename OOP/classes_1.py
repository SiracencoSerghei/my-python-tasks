class Character:
    name = None
    x = None
    y = None
    hp = 100
    pm = 100

    #     def move():
    #         print('I moved')
    # #         Error:
    # # Method must have a first parameter, usually called 'self'
    def move(arg):
        print(arg)
        print('I moved')



char_1 = Character()
char_2 = Character()
char_1.move()
# <__main__.Character object at 0x7fbd46506350>
# I moved
print(char_1)
# <__main__.Character object at 0x7fbd46506350>

#  => self is reference to the object itself
