from datetime import date, datetime

def print_birthday_info(user):
    if 'birthday' in user:
        birthday = user['birthday']
        formatted_birthday = birthday.strftime('%Y-%m-%d')  # Форматуємо дату
        print(f"{user['name']}'s birthday: {formatted_birthday}")
    else:
        print(f"No birthday information found for {user['name']}")

# Приклад використання
user = {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}
print_birthday_info(user)