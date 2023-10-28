# def back_point(number):
#     print(number)
#     if number > 0:
#         back_point(number-1)
    
# print(back_point(5))

# def back_point(number):
#     if number % 2 == 0:
#         print(number)
        
#     if number > 0:
#         back_point(number-1)
    
# print(back_point(5))

# def sum_num(num):
#     if num > 0:
#         total = num + sum_num(num - 1)
#         print(total)
#         return total
#     return 0

# print(sum_num(4))
    
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(4))

# def stepen(number, pow):
#     print(number, pow)
#     if pow == 0:
#         return 1
#     elif pow < 0:
#         return "Negative power is not supported"
#     else:
#         result = number *stepen(number, pow-1)
#         print(result)
#         return result
    
# print(stepen(3, 2))

# def stepen(number, pow):
#     print(number, pow)
#     if pow == 0:
#         return 1
#     if pow < 0:
#         return "Negative power is not supported"
#     for _ in range(1, pow):
#         print(number, pow)
#         number = number * number
#     return number
    
# print(stepen(3, 2))

# def list_arround(list_in, length_list=None):
#     if length_list is None:
#         length_list = len(list_in)
#     if length_list == 0:
#         return []
#     el = [list_in[length_list - 1]]
#     el.extend(list_arround(list_in, length_list - 1))
#     return el

# print(list_arround([1, 2, 3, 4, 5]))

# def spisok(lst):
#     if len(lst) > 0:
#         spk_new = lst[-1]
#         lenght = len(lst)
#         spk_new += spisok(lst[:lenght-1])
#         return spk_new
#     return lst
# list1 = "robot"
# print(spisok(list1))
# list1 = ""
# print(spisok(list1))
# list1 = "1"
# print(spisok(list1))

# ==========================================

# import sys
# def files(path_1, path_2):
#     with open(path_2, 'r') as file_2:
#         text_file_2 = file_2.read()
        
#     with open(path_1, 'w') as file_1:
#         text_file_1 = file_1.write(text_file_2)
        
#     return True
# print(files(sys.argv[1], sys.argv[2]))

# python3 les2.py exits.txt text.txt


# import sys
# def files(path_1, path_2):
#     with open(path_2, 'r') as file_2:
#         text_file_2 = file_2.readlines()
#         final_file_2 = text_file_2[::-1]
        
#     with open(path_1, 'w') as file_1:
#         file_1.writelines(final_file_2)
#     return True
# print(files(sys.argv[1], sys.argv[2]))

# python3 les2.py exits.txt text.txt



# ========================================

# def list_num(n):
#     new_list = []
#     for el in range(1, n+1):
#         if el%3==0 and el%5==0:
#             new_list.append(el)
#     return new_list

# print(list_num(35))

# def word_list_count(word_list):
#     result = []
#     for word in word_list:
#         word_list = list(word)
#         char_set = set(word_list)
#         # print(char_set)
        
#         for char in char_set:
            
#             if word.count(char) > 3:
#                 result.append(char)
#     return result
            
            
# print(word_list_count(["hello", "world", "Sergio", "abracadabra"]))

# def unic_word(string):
#     words = list()
#     for word in string.split():
#         word = word.replace("!", "")
#         word = word.lower()
#         if word in words:
#             continue
#         words.append(word)
#     return len(words), words
# print(unic_word("Hello world! Hello people!"))



# a = ["A", "B", "C", "D"]
# b = ["G", "F", "E"]

# z = [{a: b} for a, b in zip(a, b)]
# z.extend([{x: None} for x in a[len(b):]])

# print(z)

