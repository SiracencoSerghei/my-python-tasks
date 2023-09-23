"""Напишіть функцію formatted_numbers, яка повертає список відформатованих рядків, щоб під час виведення наступного коду:

for el in formatted_numbers():
    print(el)
    всі стовпці мають ширину 10 символів
у заголовків таблиці вирівнювання по центру
перший стовпець десяткових чисел — вирівнювання по лівому краю
другий стовпець шістнадцяткових чисел — вирівнювання по центру
третій стовпець двійкових чисел — вирівнювання з правого краю
вертикальний символ | не входить у ширину стовпця
Функція formatted_numbers виводить таблицю чисел від 0 до 15 у десятковому, шістнадцятковому та бінарному форматі."""


def formatted_numbers(number_to_range):
    formatted_list = []

    # Форматування заголовка таблиці
    header = f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"
    formatted_list.append(header)

    # Генеруємо рядки для чисел від 0 до 15
    for i in range(number_to_range):
        decimal = f"{i:<10}"  # Десятковий формат
        hex_value = f"{hex(i)[2:]:^10}"  # Шістнадцятковий формат
        binary = f"{bin(i)[2:]:>10}"  # Бінарний формат без префіксу '0b'

        row = f"|{decimal}|{hex_value}|{binary}|"
        formatted_list.append(row)
    formatted_list.append('|'*34)
    return formatted_list

# Виведення відформатованих даних
for el in formatted_numbers(16):
    print(el)