
# ======================

# def simple_generator():
#     yield "Test"
#     yield "hello"
    
    
# for item in simple_generator():
#     print(item)
    
# ========================

# def simple_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1

# five_to_ten_generator = simple_generator(5, 10)

# print(next(five_to_ten_generator)) # 5
# print(next(five_to_ten_generator)) # 6
# next(five_to_ten_generator) # 7
# next(five_to_ten_generator) # 8
# next(five_to_ten_generator) # 9
# print(next(five_to_ten_generator)) # 10
# print(next(five_to_ten_generator)) # ERROR - StopIteration


# =================================

# def my_range(limit):
#     val = 0
    
#     while val < limit:
#         yield val
#         val += 1

# my_gen = my_range(10)

# # for num in my_gen:
# #     print(num)
    
# while True:
#     try:
#         r = next(my_gen)
#         print(r)
#     except StopIteration as e:
#         break
    
# ===============================



# def pow_normal(x):
#     return x ** 2

# print(pow_normal(3))

# pow_lambda = lambda x: x ** 2
# print(pow_lambda)

# ==================

# names = ['dan', 'jane', 'steve', 'mike']

# def normalize(name):
#     return name.title()


# new_name = []

# for name in names:
#     new_name.append(normalize(name))
# print(new_name)

# new_map = map(normalize, names)
# print(new_map)
# print(list(new_map))


# ====================



# names = ['dan', 'jane', 'steve', 'mike']

# def normalize(name):
#     return name.title()


# new_name = []

# new_map = map(normalize, names)
# print(new_map)
# print(list(new_map))


# new_name_map = map(str.title, names)
# print(list(new_name_map))

# lambda_name_map = map(lambda name: name.title(), names)
# print(lambda_name_map)

# news_map = [name.title() for name in names]
# print(news_map)


# ================================


# payment = [100, -3, 400, 35, -100]

# def is_negative_number(number):
#     if number < 0:
#         return True
#     else:
#         return False
# is_negatives = list(filter(is_negative_number, payment))
# print(is_negatives)

# is_positives = list(filter(lambda num: num > 0, payment))
# print(is_positives)


# ===========================

# nums = [i for i in range(1, 10)]
# print(nums)

# sq = map(lambda x: x ** 2, nums)
# result = filter(lambda value: not bool(value % 2), sq)

# print(list(result))


# ===========================


# nums = [i for i in range(1, 10)]
# print(nums)

# sq = map(lambda x: x ** 2, nums)
# result = filter(lambda value: not bool(value % 2), sq)

# print(list(result))
# # ==========
# res = list(filter(lambda value: bool(value % 2), map(lambda x: x ** 2, [i for i in range(1, 10)])))
# print(res)
# # ===========

# result = list(map(lambda x: x ** 2, filter(lambda value: not bool(value % 2), [i for i in range(1, 10)])))
# print(result)

# ===============================================


from functools import reduce

# reduce(func, sequence, initial)

def add(x, y):
    return x + y

numbers = [1, 3, 5]
print(reduce(add, numbers, 11)) # 20 11+1+3+5

def mult(x, y):
    return x * y

numbers = [1, 3, 5]
print(reduce(mult, numbers, 2)) # 30 2*1*3*5

