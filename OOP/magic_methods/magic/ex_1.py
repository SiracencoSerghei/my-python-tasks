# Метод __new__

class Foo:  # class Foo(object):
    def __new__(cls, *args, **kwargs):
        print('Method new Foo class')
        print(args)
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print('__init__ Foo class')
        self.value = value


class Baz(Foo):
    def __init__(self, value):
        super().__init__(value)

baz = Baz(10)
foo = Foo(20)

print(baz.value, foo.value)
print(baz, foo)
print(isinstance(baz, Baz))
print(isinstance(foo, Baz))