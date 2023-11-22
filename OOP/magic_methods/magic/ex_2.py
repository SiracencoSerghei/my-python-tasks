# Singleton
class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)  # cls - екземпляр класу
        return cls.instance

    def __init__(self, value):
        self.value = value


foo = Singleton(10)
baz = Singleton(20)
bar = Singleton(30)

print(foo.value, baz.value, bar.value)
print(foo, baz, bar)
# 0x7fe6002c8f10
# 0x7fe6002c8f10
# 0x7fe6002c8f10
