'''Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна	Код ISO	Префікс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_countries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.'''


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    countries = {
        "JP": "+81",
        "SG": "+65",
        "TW": "+886",
        "UA": "+380"
    }

    phone_numbers_by_country = {
        "JP": [],
        "SG": [],
        "TW": [],
        "UA": []
    }

    for phone in list_phones:
        normalized_phone = sanitize_phone_number(phone)
        print(f'normalized_phone: {normalized_phone}')
        found_country = False

        for country_code, prefix in countries.items():
            
            if normalized_phone.startswith(prefix[1::]):
                phone_numbers_by_country[country_code].append(normalized_phone)
                print(f'country_code: {country_code}')
                print(f'prefix: {prefix}')
                print(f'phone: {phone_numbers_by_country}')
                found_country = True
                break

        if not found_country:
            phone_numbers_by_country["UA"].append(normalized_phone)

    return phone_numbers_by_country

phone_list = [
    "+81987654321",
    "+6501234567",
    "+886987654321",
    "+380987654321",
    "+123456789"
]

result = get_phone_numbers_for_countries(phone_list)
print(f'result: {result}')