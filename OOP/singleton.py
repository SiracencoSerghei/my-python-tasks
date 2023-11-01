class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


class A(Singleton):
    pass


a = A()
print(a)  # <__main__.A object at 0x7fb60e322490>
b = A()
print(b)  # <__main__.A object at 0x7fb60e322490>
