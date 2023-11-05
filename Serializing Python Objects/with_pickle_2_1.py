import pickle

# with open("text.bin", "rb") as file:
#     des = pickle.load(file)
#     print(des)

    # Traceback(most recent call last):  File
    # "/home/sergio/Desktop/my python tasks/Serializing Python Objects/with_pickle_2_1.py", line
    # 10, in < module > des = pickle.load(file)
    # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    # AttributeError: Can't get attribute 'Character' on <module '
    # __main__ ' from ' / home / sergio / Desktop / my python tasks / Serializing
    # Python Objects / with_pickle_2_1.py '>


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def asd(self):
        pass

with open("text.bin", "rb") as file:
    des = pickle.load(file)
    print(des) # <__main__.Character object at 0x7fe6a2d23110>

print(des.name) # Jack


