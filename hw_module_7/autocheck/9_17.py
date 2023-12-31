"""Підсписком (sublist) називають список, що є складовою більшого списку. Підсписок може містити один елемент, множину елементів або бути порожнім.

Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4] не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.

Порожній список є підсписком будь-якого списку.

Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]]."""


# def all_sub_lists(data):
#     sub_lists = [[]]
#     for i in range(len(data)):
#         for j in range(i + 1, len(data) + 1):
#             sub_list = data[i:j]
#             print(sub_list)
#             sub_lists.append(sub_list)
#     sub_lists.sort(key=len)
#     return sub_lists

def all_sub_lists(data):
    sub_lists = [[]]
    for i in range(1, len(data) + 1):
        for j in range(len(data) - i + 1):
            sub_lists.append(data[j:j + i])           
    
    return sub_lists

# def all_sub_lists(data):
#     if len(data) == 0:
#         return [[]]
#     extended_sub_lists = [([data[0]] + sub_list) for sub_list in all_sub_lists(data[1:])] + all_sub_lists(data[1:])
#     extended_sub_lists.sort(key=len)
#     return extended_sub_lists

    


# Приклад використання:
my_list = [1, 2, 3]
result = all_sub_lists(my_list)
print(result)
