"""Є список IP адрес:

IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.

Приклад:

{
    '85.157.172.253': 2,
    ...
}
Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.

Пример:

('66.50.38.43', 4)"""


from collections import Counter

def get_count_visits_from_ip(ips):
    # Використовуємо Counter для підрахунку кількості входжень кожної IP-адреси
    ip_counts = Counter(ips)
    return dict(ip_counts)

def get_frequent_visit_from_ip(ips):
    # Використовуємо Counter для підрахунку кількості входжень кожної IP-адреси
    ip_counts = Counter(ips)
    # Знаходимо найбільш часто уживану IP-адресу та її кількість входжень
    most_common_ip, count = ip_counts.most_common(1)[0]
    return most_common_ip, count

# Приклад використання зі списком IP-адрес
IP = [
    "85.157.172.253",
    "66.50.38.43",
    "85.157.172.253",
    "192.168.1.1",
    "66.50.38.43",
    "66.50.38.43",
]
count_visits = get_count_visits_from_ip(IP)
print(count_visits)

most_frequent_visit = get_frequent_visit_from_ip(IP)
print(most_frequent_visit)

