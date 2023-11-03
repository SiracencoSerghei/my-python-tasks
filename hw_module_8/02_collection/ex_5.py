"""
Реалізувати функцію, яка повертає n чисел, що найчастіше зустрічаються і n найменш часто зустрічаються, з файлу
"""

from collections import Counter


def num_counter(n):
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    counter = Counter([int(number) for number in data.split(',')])
    ordered = counter.most_common()
    return [item for item, _ in ordered[:n]], [item for item, _ in ordered[-n:]]

result = num_counter(5)
max_num, min_num = result
print(max_num)
print(min_num)