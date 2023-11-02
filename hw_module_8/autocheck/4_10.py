"""Щоб виграти головний приз лотереї, необхідний збіг
кількох номерів на лотерейному квитку з числами,
що випали випадковим чином і в певному діапазоні під
час чергового тиражу. Наприклад, необхідно вгадати шість
чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Напишіть функцію, яка випадково підбиратиме набір чисел
 для лотерейного квитка. Серед цих чисел не має бути дублікатів.

Формат функції get_numbers_ticket(min, max, quantity), де параметри:

min - мінімальне значення діапазону, не може бути менше 1
max - максимальне значення діапазону, не може бути більше 1000
quantity - кількість чисел у наборі (має бути min < quantity < max)
Функція повинна повернути перелік випадкових чисел за зростанням.
Якщо порушено умови обмежень на параметри функції, тоді повернути
 пустий список."""

from random import randrange, sample

def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка обмежень на параметри
    if min_value < 1 or max_value > 1000 or not min_value <= quantity <= max_value:
        return []

    # Генеруємо список унікальних чисел у заданому діапазоні
    # numbers = []
    # while len(numbers) < quantity:
    #     num = randrange(min_value, max_value + 1)
    #     if num not in numbers:
    #         numbers.append(num)
    numbers = sample(range(min_value, max_value + 1), quantity)
    # Сортуємо числа за зростанням
    numbers.sort()

    return numbers

# Приклад використання:
min_value = 1
max_value = 49
quantity = 6
result = get_numbers_ticket(min_value, max_value, quantity)
print(result)
