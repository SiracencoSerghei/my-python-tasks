"""
Напишіть функцію, яка приймає на вхід три
цілих числа: день, місяць та рік. Функція має повертати порядковий
номер заданого дня у вказаному році.
​
Результат функції: номер року та порядковий номер дня у цьому
році - обидва у цілісному форматі.
"""

from datetime import datetime, date

def date_test(day: int, month: int, year: int):
    d = date(year, month, day).toordinal()
    diff = d - date(year, 1, 1).toordinal() + 1
    return year, diff

print(date_test(31, 12, 2023))
print(date_test(1, 1, 2023))
print(date_test(2, 11, 2023))