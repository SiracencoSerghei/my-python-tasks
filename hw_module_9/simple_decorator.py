def simple_decorator(func):
    def simple_wrapper(*args, **kwargs):
        print("Before func")
        result = func(*args, **kwargs)
        print(result)
        print("After func")
        return result

    return simple_wrapper


@simple_decorator
def mult(x, y):
    return x * y


result1 = mult(5, 5)
print(result1)


import functools
def f(a,b,c,d):
    print("{} {} {} {}".format(a,b,c,d))
f_new = functools.partial(f, b='you', c='beautiful', d='world')
print(f_new('Hello '))
print(f_new('Bye, '))
