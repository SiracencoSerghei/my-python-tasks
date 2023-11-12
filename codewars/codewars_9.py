
"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""

# def get_count(sentence):
#     vouwels_list = ['a', 'e', 'i', 'o', 'u']
#     # vouwels_count = 0
#     # for char in sentence:
#     #     if char in vouwels_list:
#     #         vouwels_count += 1
#
#     vouwels_count = len([x for x in sentence if x in ['a', 'e', 'i', 'o', 'u']])
#     return vouwels_count
#
#
# print(get_count("hello world"))

# ==========================================

# """Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1)
#  e.g.: (Input --> Output)
#
# 1 -->  1
# 2 --> 3 + 5 = 8"""
#
# def row_sum_odd_numbers(n):
#     # odd_numbers = []
#     # start_number = n ** 2 - (n - 1)
#     # while n > 0:
#     #     odd_numbers.append(start_number)
#     #     start_number += 2
#     #     n -= 1
#     # sum_row = sum(odd_numbers)
#     # return sum_row
#     return n ** 3
# print(row_sum_odd_numbers(2))
# print(row_sum_odd_numbers(3))
# print(row_sum_odd_numbers(4))

# ========================================

# """Very simple, given an integer or a floating-point number, find its opposite.
#
# Examples:
#
# 1: -1
# 14: -14
# -34: 34"""
#
# def opposite(number):
# #     opposite_number = {}
# #     opposite_number[number] = - number
# #     return opposite_number[number]
#       return - number
# print(opposite(1))
# print(opposite(14))
# print(opposite(-34))
# print(opposite(25.6))
# print(opposite(0))
# print(opposite(1425.2222))
# print(opposite(-3.1458))
# print(opposite(-95858588225))

# ==========================================================


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

"""DESCRIPTION:
Complete the square sum function so that it squares each number passed into it and then 
sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1
2
+
2
2
+
2
2
=
9
1 
2
 +2 
2
 +2 
2
 =9.

"""

# def square_sum(numbers):
#     return sum([x**2 for x in numbers])
# print(square_sum([1, 2, 2]))
# =====================

"""Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per 
hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will 
drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5"""
# import math
#
# def litres(time):
#     liter_per_hour = 0.5
#     return math.floor(liter_per_hour * time)
#
# print(litres(3))
# print(litres(6.7))
# print(litres(11.8))

# ======================

"""Task:
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"""

# def odd_or_even(arr):
#     summ = sum(arr)
#     return 'even' if summ % 2 ==0 else 'odd'


# =========================

"""DESCRIPTION:
You are given the length and width of a 4-sided polygon. The polygon can either be a 
rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

Example(Input1, Input2 --> Output):

6, 10 --> 32
3, 3 --> 9
Note: for the purposes of this kata you will assume that it is a square if its length and 
width are equal, otherwise it is a rectangle.

"""

# def area_or_perimeter(l, w):
#     return l * w if l == w else 2 * (l + w)

# ===============================

"""Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)"""

def add_binary(a, b):
    # return  bin(a+b)[2:]
    # return format(a + b, 'b')
    return f"{a + b :b}"
print(add_binary(1, 1))
print(add_binary(5, 9))




