"""Рекурсия хорошо подходит к задаче flattening. Это процесс выравнивания списков, который заключается в избавлении вложенной структуры. Например список вида [1, 2, [3, 4, [5, 6]], 7] должен быть преобразован в плоский (flat) список [1, 2, 3, 4, 5, 6, 7]

Напишите функцию flatten, которая принимает на вход список, рекурсивно будет выравнивать этот список и возвращать плоскую версию списка.

Для выполнения задачи можно следовать следующему алгоритму:

Если входной список пуст, то:
  возвращаем пустой список
Если первый элемент списка является списком, то:
  Получаем первый список, рекурсивно вызвав функцию с первым элементом списка
  Получаем второй список, рекурсивно вызвав функцию с остальным списком без первого элемента
  Возвращаем конкатенацию двух списков
Если первый элемент списка не является списком, то:
  Получаем первый список с первого элемента списка
  Получаем второй список, рекурсивно вызвав функцию с остальным списком без первого элемента
  Возвращаем конкатенацию двух списков"""
  
def flatten(data):
    if not data:
        return []
    elif isinstance(data[0], list):
        first = flatten(data[0])
        rest = flatten(data[1:])
        return first + rest
    else:
        first = data[0:1]
        rest = flatten(data[1:])
        return first + rest
    
nested_list = [1, 2, [3, 4, [5, 6]], 7]
flat_list = flatten(nested_list)
print(flat_list)