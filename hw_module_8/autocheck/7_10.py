"""У нас є іменований кортеж для зберігання котів у змінній Cat. На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.

Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.

Якщо функція convert_list приймає у параметрі cats список іменованих кортежів

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
То функція поверне наступний список словників:

[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
І в той же час, якщо функція convert_list приймає в параметрі cats список словників, то результатом буде зворотна операція та функція поверне список іменованих кортежів.

Для визначення типу параметра cats використовуйте функцію isinstance."""

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
def convert_list(cats):

    # Перевіряємо, чи cats - це список іменованих кортежів Person
    if isinstance(cats[0], Cat):
        # Якщо так, конвертуємо у список словників
        return [{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]
    # Якщо cats - це список словників
    elif isinstance(cats[0], dict):
        # Конвертуємо у список іменованих кортежів Person
        return [Cat(cat["nickname"], cat["age"], cat["owner"]) for cat in cats]

# Приклад використання зі списком іменованих кортежів Person
cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
converted_to_dict = convert_list(cats_namedtuple)
print(converted_to_dict)

# Приклад використання зі списком словників
cats_dict = [
    {"nickname": "Fluffy", "age": 2, "owner": "John"},
    {"nickname": "Whiskers", "age": 4, "owner": "Alice"},
    {"nickname": "Tom", "age": 6, "owner": "Bob"}
]
converted_to_namedtuple = convert_list(cats_dict)
print(converted_to_namedtuple)

    
        
            
                