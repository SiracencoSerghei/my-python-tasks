# Написати функцію, яка визначає який день тижня у певної дати у вигляді "день-місяць-рік".

from datetime import datetime

days_name = {
    0: "понеділок",
    1: "вівторок",
    2: "середа",
    3: "четвер",
    4: "п'ятниця",
    5: "субота",
    6: "неділя",
}


def day_of_the_week(date: str):
    d, m, y = date.split('-')
    date = datetime(day=int(d), month=int(m), year=int(y))
    d_name = days_name.get(date.weekday())
    return d_name


print(day_of_the_week('1-11-2023'))
print(day_of_the_week('2-11-2023'))
print(day_of_the_week('3-11-2023'))
print(day_of_the_week('4-11-2023'))
