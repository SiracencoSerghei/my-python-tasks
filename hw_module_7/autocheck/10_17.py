"""При роботі веб-сервісів спілкування, за протоколом HTTP, найчастіше відбувається в форматі JSON. І надсилання даних на сервер при запиті POST - це необхідність використовувати словник, оскільки структура формату JSON ідентична словнику Python.

Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у вигляді словника. Дана функція make_request(keys, values) приймає два параметри у вигляді списків. Функція повинна створити словник із ключами з списку keys та значеннями зі списку values.

Порядок відповідності збігається з індексами списків keys та values.
Якщо довжина keys та values не збігаються, поверніть порожній словник."""

def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    request = {}
    for i, key in enumerate(keys):
        request[key] = values[i]
    
    # for i in range(len(keys)):
    #     request[keys[i]] = values[i]
        
    return request


keys = ["name", "age", "city"]
values = ["John", 30, "New York"]

request = make_request(keys, values)
print(request)