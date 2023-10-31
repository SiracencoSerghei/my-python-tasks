"""Write a program that finds the summation of
 every number from 1 to num.
  The number will always be a positive integer
  greater than 0.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)"""

def summation(num):
    # sum = 0
    # if num > 0:
    #     for i in range(num + 1):
    #         sum += i
    # return sum
    # ============
    # return sum(range(num + 1))
    # ================
    return num + summation(num - 1)
print(summation(8))

