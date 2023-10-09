"""Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику."""

from datetime import datetime


def get_str_date(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    print(date_obj)
    formatted_date = date_obj.strftime('%A %d %B %Y')
    print(f"date time object: {formatted_date}")
    return formatted_date    
    
get_str_date('2021-05-27 17:08:34.149Z')
