from collections import UserString, UserList, UserDict
from random import randint
class A:
    field = None
    def method(self):
        pass

print(A().__dict__) # {}
print(A.__dict__) # {'__module__': '__main__', 'field': None, 'method': <function A.method at 0x7f0aba2d8540>,
                  # '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__'
                  # of 'A' objects>, '__doc__': None}

# class list(list):
#     def append(self):
#         print('No elements for you')
#     def sey_hello(self):
#         print(f'Hello from {self}')
#
#
# a = list('azerty')
# print(a)
# a.append()
# a.sey_hello()

# class MyList(UserList):
#     def append(self):
#         print('No elements for you')
#     def sey_hello(self):
#         print(f'Hello from {self.data}')
#     def update_with_random(self):
#         self.data[0] = randint(0, 10)
#         return self.data[0]
#
# a = MyList('azerty')
# print(a)
# a.append()
# a.sey_hello()
# print(a.update_with_random())

# class MyList(UserDict):
#     def append(self):
#         print('No elements for you')
#     def sey_hello(self):
#         print(f'Hello from {self.data}')
#     def update_with_random(self):
#         self.data[0] = randint(0, 10)
#         return self.data[0]
#
# a = MyList({'azerty': 5})
# print(a)
# a.append()
# a.sey_hello()
# print(a.update_with_random())
# a.sey_hello()

class MyList(UserString):
    def append(self):
        print('No elements for you')
    def sey_hello(self):
        print(f'Hello from {self.data}')
    def update_with_random(self):
        self.data = self.data.replace("a", "B")
        return self.data

a = MyList('azerty')
print(a)
a.append()
a.sey_hello()
print(a.update_with_random())