"""Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року."""

from datetime import date


def get_days_in_month(month, year):
    a = date(year, month, 1)
    print(a)
    if month == 12:
        next_year = year + 1
        next_month =1
    else:
        next_year = year
        next_month = month + 1
    
    
    next_a = date(next_year, next_month, 1)
    print(next_a)
    days = (next_a - a).days
    print(days)
    return days
    
get_days_in_month(2,2024)
get_days_in_month(12,2024)
