class A:
    def __init__(self):
        self.x = 42


a = A()
print(getattr(a, "x"))  # getattr(object, name, [default])
print(a.x)
setattr(a, "x", 55)  # setattr(object, name, value)
print(getattr(a, "x"))
a.x = 77
print(getattr(a, "x"))


class B(A):
    def __init__(self):
        super().__init__()
        for i in range(5):
            setattr(self, f"y{i}", i)


b = B()
# print(b.y3)
# print(getattr(b, "x"))
# b.x = 55
# print(b.x, b.y2)
# print(a.x)
delattr(b, "y4")  # delattr(object, name)


# getattr(b, "y4")

class C(B):
    pass


class D:
    pass


a = A()
b = B()
c = C()
d = D()

print(isinstance(a, A))  # isinstance(object, classinfo)
print(isinstance(a, (B, C)))
print(isinstance(a, (A, B, C)))

print(isinstance(c, A))
print(isinstance(c, (B, D)))

print(isinstance(d, C))

print(issubclass(B, A))
print(issubclass(B, (D, A)))
print(issubclass(A, C))
print(issubclass(D, (A, B, C)))
