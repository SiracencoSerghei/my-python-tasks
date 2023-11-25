# Декоратори класів
def method_decorator(func):
    def wrapper(self, *args):
        print('--Decorator func run--')
        result = func(self, *args)
        print('--Decorator func end--')
        return result
    return wrapper


def class_decorator(cls):
    print('---Decorator class---')
    new_cls = cls
    new_cls.value = 55
    return new_cls


@class_decorator
class TestClass:
    name = 'GoIT'

    @method_decorator
    def info(self, user):
        return f'Hello: {user}'


t = TestClass()
print(t.info('Ivan'))
print(t.value)
t.value = "Hello world"
print(t.value)
print('=====')
print(TestClass.value)
