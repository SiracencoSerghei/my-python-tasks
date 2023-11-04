# public
# protected
# private

# class Character:
#     def __init__(self, name):
#         self.name = name # public
#         self._damage = 10 # protected
#         self.__hp = 100 # private
#     def public(self):
#         print('public')
#     def _protected(self):
#         print("_protected")
#     def __private(self):
#         print("__private")
#     def get_hp(self):
#         return self.__hp
#     def set_hp(self, hp):
#         if hp > 0 and hp <= 100:
#             self.__hp = hp
#
#
#
#
#
# char = Character("Pietro")
# char.name = "Sergio"
# print(char.name) # "Sergio"
# char._damage = 20
# print(char._damage) # 20
# # print(char.__hp) # AttributeError: 'Character' object has no attribute '__hp'
# print(char.__dict__) # {'name': 'Sergio', '_damage': 20, '_Character__hp': 100}
# print(char._Character__hp) # 100
# char._Character__hp = 95
# print(char._Character__hp) # 95
# print(char.get_hp()) # 95
# char.set_hp(75)
# print(char.get_hp()) # 75

# ==================================


class Character:
    def __init__(self, name):
        self.name = name # public
        self._damage = 10 # protected
        self.__hp = 100 # private
    @property
    # def mp(self):
    def hp(self):
        print("GETTER")
        return self.__hp
    @hp.setter
    # mp.setter
    def hp(self, new_hp):
        if 0 <= new_hp <= 100:
            self.__hp = new_hp
            print(f"SETTER: {new_hp}")
        else:
            raise ValueError("HP should be in range of 0 - 100")


char = Character("Pietro")
print(char.hp)
char.hp = 95 # SETTER: 95
print(char.hp)