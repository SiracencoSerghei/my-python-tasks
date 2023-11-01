# Aggregation
class Character:
    hp = 100
    pm = 100
    count = 0

    def __init__(self, name, x=1, y=1):
        print("Init new instance, Total: ", end=" ")
        self.name = name
        self.x = x
        self.y = y
        self.left_hand = None
        self.right_hand = None
        Character.count += 1
        print(Character.count)

    def pick_weapon(self, weapon):
        if self.left_hand is None:
            self.left_hand = weapon
        elif self.right_hand is None:
            self.right_hand = weapon
        else:
            print("I'm full")

    def show_weapon(self):
        return self.left_hand, self.right_hand

    def die(self):
        return self.left_hand, self.right_hand


class Weapon:
    def __init__(self):
        self.type = 'sword'
        self.damage = 10


# SOLID:
# Single responsibility
#
char_1 = Character("Sergio")
char_2 = Character("Pietro")
# opening a chest
sword_1 = Weapon()
print(sword_1.type)
print(sword_1.damage)
char_1.pick_weapon(sword_1)
left_hand, right_hand = char_1.show_weapon()
print("left_hand: ", left_hand.type if left_hand else None)
print("right_hand: ", right_hand.type if right_hand else None)
left_hand, right_hand = char_1.die()
char_2.pick_weapon(sword_1)
print(char_2.left_hand.type if left_hand else None)
