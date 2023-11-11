#
#
# list_contacts = [
#     {"name": "Serghei", "email": "siracencoserghei@gmail.com"},
# {"name": "Petro", "email": "siracencopetro@gmail.com"}
# ]
# def get_emails(list_contacts):
#     lst = []
#     for el in map(get_email,list_contacts):
#         lst.append(el)
#     return lst
#
#
# def get_email(contact):
#     return contact['email']
#
# print(get_emails(list_contacts))

# ==============================

# list = []
# def generator(n):
#     for i in range(1, n + 1):
#         yield i
#         print(i)
#
# result = generator(5)
# for i in result:
#     list.append(i)
#
# print(list)

# ======================
# import random
#
# list = []
# def generator(n):
#     for i in range(n):
#         number = random.randint(n, 10)
#
#         yield number
#         print(number)
#
# result = generator(5)
# for i in result:
#     list.append(i)
#
# print(list)

# ==========================

# list = []
# def generator(a, b):
#     while a<=b:
#         yield a
#         print(a)
#         a+=1
#
# result = generator(5, 12)
# for i in result:
#     list.append(i)
#
# print(list)

# ======

# def gen_list(list_1, list_2):
#     for val in list_1:
#         if val in list_2:
#             yield  eval
#
# result = gen_list([1, 1, 2, 2], [1, 1, 2, 3])
# lis = []
# for j in result:
#     lis.append(j)
# print(lis)

# ================

# def gen_list(list_1, list_2):
#     filter1 = filter(lambda x: x in list_2, list_1)
#     for val in filter1:
#         yield val
#
# result = gen_list([1, 1, 2, 2], [1, 1, 2, 3])
# lis = []
# for j in result:
#     lis.append(j)
# print(lis)

# =========================

# def gen_list(list_1, list_2):
#     combined_set = set(list_1)
#     combined_set.update(list_2)
#     result =  list(combined_set)
#     for i in result:
#         yield i
# result = gen_list([1, 1, 2, 2], [1, 1, 2, 3])
# lis = []
# for j in result:
#     lis.append(j)
# print(lis)

# ============
# list = []
# def generator(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             yield i
#             print(i)
#
# result = generator(15)
# for i in result:
#     list.append(i)
#
# print(list)
# =====================
#
# list = []
# def generator(n):
#     add_filter = filter(lambda x: x % 2 == 0, n)
#     for i in add_filter:
#         yield i
#         print(i)
#
# result = generator([1, 2, 4, 5, 10, 11, 13])
# for i in result:
#     list.append(i)
#
# print(list)
# =========================

# def gen(string):
#     list_lt = ['a', 'e', 'o','i']
#     for letter in string.lower():
#         if letter in list_lt:
#             yield  letter
#
# for item in gen('hello world'):
#     print(item)
#
# ==========================

# def gen(string):
#     word_list = string.split(" ")
#     for i in word_list:
#         if len(i) > 4:
#             yield i
#
# for i in gen("hello wonderful world and me"):
#     print(i)

# ============

# def gen(string):
#     word_list = string.split(" ")
#     word_list = filter(lambda x : len(x) > 4, word_list)
#     for i in word_list:
#         yield i
#
# for i in gen("hello my  wonderful world and me"):
#     print(i)
# =====================

# import datetime
# import time
# def timer_gen(n):
#     time = datetime.datetime.now()
#     for i in range(1, n+1):
#         yield datetime.datetime.now()
#
# for i in timer_gen(5):
#     time.sleep(1)
#     print(i)

# ==============================
#
# def decor(func):
#     def wrapper(*args,**kwargs):
#         result = [i for i in func(*args,**kwargs)]
#         return result
#     return wrapper
#
# @decor
# def gen(x, y):
#     filter_num = filter(lambda a: a % 3 == 0 and a % 5 ==0, range(x, y+1))
#     for i in filter_num:
#         yield i
#
#
# print(gen(1, 45))

# =============================

# def decor(func):
#     def wrapper(x, y):
#         result = func(x, y)
#         for i in result:
#             if i % 3 == 0 and i % 5 ==0:
#                 print("FizzeBuzze")
#             elif i % 3 == 0:
#                 print("Fizze")
#             elif i % 5 ==0:
#                 print("Buzze")
#             else:
#                 print(i)
#     return wrapper
#
# @decor
# def gen(x, y):
#     for i in range(x, y + 1):
#         yield i
#
#
# print(gen(1, 45))

# ============================

# def decor(func):
#     def wrapper(*args, **kwargs):
#         print(*args)
#         new_lst = []
#         for i in func(*args, **kwargs):
#             new_lst.append(i)
#         print(new_lst)
#     return  wrapper
#
# @decor
# def power(list_el):
#     for i in list_el:
#         num_pow = i ** 2
#         yield num_pow
#
# power([1, 5, 8, 96])

# =======================================

