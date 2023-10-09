"""Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

Підказки:

Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
datetime приймає аргументи типу int, використовуйте перетворення типів.
ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157."""

from datetime import datetime


def get_days_from_today(date):
    # year, month, day = date.split("-")    # щоб перетворити рядок з датою на цілі числа для створення об'єкта datetime => разпаковка:
    year, month, day = map(int, date.split('-'))
    print(year, month, day)
    # ігноруємо години, хвилини та секунди для нашей дати, важливі повні дні.
    current_date = datetime.now().date()
    print(type(current_date))
    print(current_date)
    # ігноруємо години, хвилини та секунди для нашей дати, важливі повні дні.
    target_date = datetime(year=year, month=month, day=day).date()
    print(type(target_date))
    print(target_date)
    # ігноруємо години, хвилини та секунди для нашей дати, важливі повні дні. виведемо різницю в днях:
    difference = (current_date - target_date).days
    print(difference)
    return difference

    
    
get_days_from_today('2020-10-09')