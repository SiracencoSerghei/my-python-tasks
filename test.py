# from datetime import date, datetime, timedelta

# def print_birthday_info(user):
#     if 'birthday' in user:
#         birthday = user['birthday']
#         formatted_birthday = birthday.strftime('%Y-%m-%d')  # Форматуємо дату
#         print(f"{user['name']}'s birthday: {formatted_birthday}")
#     else:
#         print(f"No birthday information found for {user['name']}")

# # Приклад використання
# user = {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}
# print_birthday_info(user)

# ===================================

from datetime import date, datetime, timedelta

def calc_current_period():
    current_date = date.today()
    print(f'current_date: {current_date}')
    current_date_index = current_date.weekday()
    print(f'current_date_index: {current_date_index}')
    print(current_date.strftime('%A'))
    if current_date_index == 0:
        start_period = current_date - timedelta(2)
        end_period = current_date +timedelta(4)
    elif (current_date_index >0):
        start_period = current_date
        end_period = current_date + timedelta(6)
        
    return start_period, end_period


# Викликаємо функцію, щоб вивести результати на екран
start_period, end_period = calc_current_period()
print(f'start: {start_period}')
print(f'end: {end_period}')
