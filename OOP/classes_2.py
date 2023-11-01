class Character:
    name = None
    x = None
    y = None
    hp = 100
    pm = 100


    def move(self):
        print('I moved')
    def identify(self):
        print(self.name)
        self.move()
    def die(self):
        self.dead = True
        # this you can do with constructor
        # look to classes_3.py



char_1 = Character()
char_1.move()
char_1.identify()
char_1.name = 'Alex'
char_1.identify()
# print(char_1.dead) # AttributeError: 'Character' object has no attribute 'dead'
char_1.die() # this is characteristic ONLY of the exemplar of class - instance
print(char_1.dead) # True
