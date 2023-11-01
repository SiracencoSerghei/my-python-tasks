class Record:
    def __init__(self, name):
        self.name = name

class Name:
    def __init__(self, value):
        self.value = value
record = Record(Name("Sergio"))
print(record.name.value)


class A:
    def hello(self):
        print("hello A")


class B:
    def hello(self):
        print("hello B")


class C:
    def hello(self):
        print("hello C")


class D(A, B, C):
    pass


class H(A):
    def hello(self):
        print("hello H")


class J(A):
    pass


class F(H, C):
    pass


class S(J, C):
    pass


d = D()
d.hello()  # A
f = F()
f.hello()  # H
s = S()
s.hello()  # A
