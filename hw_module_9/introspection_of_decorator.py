"""In Python, introspection is the ability to obtain information about
the structure and properties of objects during program execution.
Introspection allows you to recognize the attributes, methods and
other characteristics of objects, as well as check their types.

Decorator introspection is a way to obtain information about the decorator
 that is applied to a function or method. In Python, a decorator is a
 function that takes another function and extends its functionality
 without changing its code. Decorators are widely used to implement
 aspect-oriented programming, logging, authentication and other tasks.

In order to introspect a decorator, you can use various attributes and
functions, such as .__name__, .__doc__, inspect, etc.
For example, to get the name of a decorator, you can use
the .__name__ attribute:"""

# import functools
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#     return wrapper
#
# @my_decorator
# def my_function():
#     print("Hello, world!")
#
# my_function()
#
# print(my_function.__name__)

"""Here my_decorator is a decorator and its name can be obtained via 
my_decorator.__name__. However, usually the need for decorator 
introspection is not that great, and usually introspection is applied 
to the function that has been decorated in order to obtain information 
about it."""
# .....................................

""" @functools.wraps(func) is a decorator provided by the functools
 module, and it is typically used inside custom decorators to preserve 
 metadata (such as function name, documentation, and other attributes) 
 of the original function that was decorated. 
 Without using @functools.wraps(func), the metadata of the original 
 function may be lost and replaced by the attributes of the decorating 
 function, which can lead to undesirable consequences when introspecting 
 and debugging the code."""

# ex_1 without @functools

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#     return wrapper
#
# @my_decorator
# def my_function():
#     """This is the original function."""
#     print("Hello, world!")
#
# print(my_function.__name__)  #  "wrapper"
# print(my_function.__doc__)   #  None

#  ex_2 with @functools

import functoolsw


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def my_function():
    """This is the original function."""
    print("Hello, world!")


my_function()

print(my_function.__name__)  # "my_function"
print(my_function.__doc__)  # "This is the original function."
