# Composition + Aggregation
class Character:
    hp = 100
    pm = 100
    count = 0

    def __init__(self, name, x=1, y=1):
        print("Init new instance, Total: ", end=" ")
        self.name = name
        self.x = x
        self.y = y
        # Composition
        self.left_hand = Weapon()
        self.right_hand = None
        Character.count += 1
        print(Character.count)

    def pick_weapon(self, weapon):
        if self.right_hand is None:
            self.right_hand = weapon
        else:
            print("I'm full")

    def show_weapon(self):
        return self.right_hand

    def die(self):
        return self.right_hand


class Weapon:
    def __init__(self):
        self.damage = 10

    def kick_ass(self):
        return self.damage


class Knife(Weapon):
    def __init__(self):
        self.damage = 5

    def throw(self):
        return self.damage - 2


class Sword(Weapon):
    def __init__(self):
        self.damage = 15


class Axe(Weapon):
    def __init__(self):
        self.damage = 20


# SOLID:
# Single responsibility

char_1 = Character("Sergio")
char_2 = Character("Pietro")
# opening a chest
knife = Knife()
sword = Sword()
axe = Axe()
print(knife.damage)
print(knife.kick_ass())
print(knife.throw())

#
