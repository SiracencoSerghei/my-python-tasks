
import pickle

# a = (1,2,3)
# ==============
# print(a) # (1, 2, 3)
# b = pickle.dumps(a)
# print(b) #b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00K\x01K\x02K\x03\x87\x94.'
# c = pickle.loads(b)
# print(a == c) # True
# print(type(c)) # <class 'tuple'>
# print(c) # (1, 2, 3)
# =============================
# a = (1,2,3)
# with open("text.bin", "wb") as file:
#     pickle.dump(a, file)
# with open("text.bin", "rb") as file:
#     b = pickle.load(file)
#     print(b)

# =====================

class Character:
    def __init__(self, name):
        self.name = name

char = Character("Jack")
# ser = pickle.dumps(char)
# print(ser)
# des = pickle.loads(ser)
# print(des) # <__main__.Character object at 0x7f7bb3f23090>
# print(des.name) # Jack
# print(type(des)) # <class '__main__.Character'>

with open("text.bin", "wb") as file:
    pickle.dump(char, file)