# Polymorphism
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
        self.left_hand = None
        self.right_hand = None
        Character.count += 1
        print(Character.count)

    def pick_weapon(self, weapon):
        # duck typing without next string
        # if isinstance(weapon, Weapon):
        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            print("I'm full")

    def show_weapon(self):
        return self.right_hand

    def die(self):
        return self.right_hand

    def damage_left(self):
        return self.left_hand.kick_ass()

    def damage_right(self):
        return self.right_hand.kick_ass()


class Weapon:
    def __init__(self):
        self.damage = 10

    def kick_ass(self):
        return self.damage


class Knife(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 5

    def throw(self):
        return self.damage - 2

    def kick_ass(self):
        print("Chick-Chick")
        return self.damage


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 15

    def kick_ass(self):
        print("Slash-slash")
        return self.damage


class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20

    def kick_ass(self):
        print("Baa-am")
        return self.damage


class Gun(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 50

    def kick_ass(self):
        print("Pif-paf")
        return self.damage


# SOLID:
# Single responsibility

char = Character("Sergio")
# opening a chest
knife = Knife()
sword = Sword()
char.pick_weapon(knife)
print(char.left_hand)
print(char.damage_left())
char.pick_weapon(sword)
print(char.right_hand)
print(char.damage_right())
