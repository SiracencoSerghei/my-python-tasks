
# import sys

# def logger(func):
    
#     counter = 0
#     def wrapper(*args, **kwargs):
#         nonlocal counter
#         counter += 1
#         print("Calling function:", func.__name__)
#         sys.stdout.write(f": call [{counter}]: [{func.__name__}] [{args}]\n")
#         result = func(*args, **kwargs)
#         sys.stdout.write(f":result: [{counter}]: [{func.__name__}] [{args}]\n")
#         return result
#     return wrapper

# def add(x, y):
#     return x + y

# @logger
# def multiply(a, b):
#     return a * b

# # @logger
# # add
# # print(add(3, 5))
# print(multiply(2, 3))
# print(multiply(2, 4))
# print(multiply(2, 5))


# =================
# from random import randint, seed

# def cycle_random(min_val, max_val):
#     seed()
#     while True:
#         try:
#             yield randint(min_val, max_val)
#         except Exception as e:
#             print(e)

# cycle = cycle_random(1, 10)
# for _ in range(10):
#     result.append
#     print(next(cycle), end=" ")


# =================================

# s= input()
# x = 0
# for i in s:
#     print(ord(i))
#     x+= ord(i)
# print(x)

# print(sum(map(ord, input())))

# =====================
