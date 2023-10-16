"""Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,

"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, який буде віддавати зазначені числа при зверненні до нього у циклі.

З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз

Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка."""

# def generator_numbers(string=""):
#     current_number = ""
#     for char in string:
#         if char.isdigit():
#             current_number += char
#         elif current_number:
              # обробляємо число в момент його знаходження:
#             yield int(current_number)
#             current_number = ""
      # якщо число не було завершено нецифровим символом:
#     if current_number:
#         yield int(current_number) 
import re
def generator_numbers(string=""):
    # За допомогою регулярних виразів шукаємо всі цілі числа в рядку
    pattern = r'\d+'
    for match in re.finditer(pattern, string):
        # Перетворюємо знайдену стрічку у ціле число
        number = int(match.group())  
        # Використовуємо yield для повернення числа у вигляді генератора
        yield number  


def sum_profit(string):
    total_profit = 0
    for number in generator_numbers(string):
        total_profit += number
    return total_profit


# Приклад використання
string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
result = sum_profit(string)
print("Загальний прибуток:", result)