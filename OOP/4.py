

class A:
    def __init__(self):
        self.x = 100
    def get_x(self):
        print("Getter called")
        return self._x
    def set_x(self, value):
        print("Setter called")
        if value < 0:
            return
        self._x = value
    x = property(get_x, set_x)


a = A()
a.x = 300
print(a.x)
a.x = -20
print(a.x)
