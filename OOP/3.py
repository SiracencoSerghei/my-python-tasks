
class A:
    def __init__(self):
        self._x = 100
    def get_x(self):
        return self._x
    def set_x(self, value):
        if value < 0:
            return
        self._x = value


a = A()
print(a.get_x())
a.set_x(300)
print(a.get_x())
a.set_x(-20)
print(a.get_x())
a._x = 500
print(a.get_x())
