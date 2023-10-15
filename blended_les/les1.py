# def sum_even_num(num):
#     sum = 0
#     if num > 0:
#         if num % 2 == 0:
#             sum += num
#         return sum + sum_even_num(num - 1)
#     else:
#         return sum

# print(sum_even_num(10))
# =============================
# import sys
# def calc(num1, num2, operand):
    
#     if (operand=="+"):
#         result = num1 + num2
#     elif (operand == "*"):
#         result= num1 * num2
#     elif (operand =="/") :
#         result = num1 / num2
#     elif (operand =="-" ):
#         result = num1-num2
    
#     return result

# try:
#     print(calc(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]))
# except (ValueError, IndexError):
#     print("Invalid input!")
    
# ==================================
# def uniq_elem(elem_list):
#     res_list = []
#     for el in elem_list:
#         count_el = elem_list.count(el)
#         if count_el > 1:
#             continue
#         else:
#             res_list.append(el)
#     print(res_list)
    
# uniq_elem([1,1,2,3, 4, 5,5])

# ===============================

# [1,2,3,4,5] => [5,1,2,3,4]

# def num_reserve(list_num):
#     reserved_list = []
#     reserved_list.append(list_num[-1])
#     for el in list_num[0:9]:
#         reserved_list.append(el)
#     return reserved_list    
# print(num_reserve([1,2,3,4,5]))

# def num_reserve(list_num, shift):

#     return list_num[shift:]+list_num[:shift] 
# print(num_reserve([1,2,3,4,5],-1))

# ---------------------------------

# import re
# def find_digits(text):
#     digits = re.findall(r'[0-9]', text)
#     return digits

# print(find_digits('hello123'))

# ================================
