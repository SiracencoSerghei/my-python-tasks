
"""multiplying a given number by eight if it is an even number
and by nine otherwise."""

# def simple_multiplication(number) :
#     return number * 8 if number % 2 == 0 else number * 9

# ================================================

"""Create a function with two arguments that will return an array of the first n 
multiples of x.

Assume both the given number and the number of times to count will be positive numbers 
greater than 0.

Return the results as an array or list ( depending on language ).

Examples
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]"""


# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     return [i * x for i in range(1, n + 1)]
#
# print(count_by(1,10)) #should return [1,2,3,4,5,6,7,8,9,10]
# print(count_by(2,5)) #should return [2,4,6,8,10]
# ======================================================

"""Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty."""

# def find_smallest_int(arr):
#     return min(arr)
#
# print(find_smallest_int([34, 15, 88, 2]))
# print(find_smallest_int([34, -345, -1, 100]))

# ==================================================

"""Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), 
value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7"""

# def basic_op(operator, value1, value2):
# #     def sum(x, y):
# #         return x + y
# #     def substract(x, y):
# #         return x - y
# #     def mult(x, y):
# #         return x * y
# #     def divide(x, y):
# #         if y != 0:
# #             return x / y
# #         return "can't divide by zero"
# #     # action = {
# #     #     '+': sum,
# #     #     '-': substract,
# #     #     '*': mult,
# #     #     '/': divide
# #     # }
# #     action = {
# #         '+': lambda x, y: x + y,
# #         '-': lambda x, y: x - y,
# #         '*': lambda x, y: x * y,
# #         '/': divide
# #     }
# #
# #     return action[operator](value1, value2)
#     return eval(f"{value1} {operator} {value2}")
# #
# print(basic_op('+', 4, 7))
# print(basic_op('-', 15, 18))
# print(basic_op('*', 5, 5))
# print(basic_op('/', 49, 7))
# #

# ==========================================

"""Given a set of numbers, return the additive inverse of each. Each positive becomes 
negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list."""

# def invert(lst):
#     return [x * (- 1) for x in lst]
# print(invert([1,2,3,4,5]))
# print(invert([1,-2,3,-4,5]))
# print(invert([]))

# ================

"""Create a function that takes an integer as an argument and returns 
"Even" for even numbers or "Odd" for odd numbers."""
# def even_or_odd(number):
#     return "Even" if number % 2 == 0 else "Odd"
#
# print(even_or_odd(1))
# print(even_or_odd(2))

# =============================================


