"""Модифікуємо приклад попередньої задачі. Для функції do_setup необхідно передбачити другий параметр, який буде списком залежностей.

Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами зі словника args_dict та параметром install_requires, який набуває значення requires.

Структура словника для параметра args_dicts має бути наступною

{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}"""

from setuptools import setup, find_namespace_packages


def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=find_namespace_packages(),
          install_requires=requires,
    )
    
    
if __name__ == "__main__":
    # Словник параметрів для ініціалізації проекту
    ARGS_DICT = {
        "name": "useful",
        "version": "1",
        "description": "Very useful code",
        "url": "http://github.com/dummy_user/useful",
        "author": "Flying Circus",
        "author_email": "flyingcircus@example.com",
        "license": "MIT",
        "packages": ["useful"],
    }
    
     # Список залежностей для пакету
    DEPENDENCIES = ['markdown', 'numpy']
    
     # Викликаємо функцію do_setup() з параметрами
    do_setup(ARGS_DICT, DEPENDENCIES)
    
    
    # Щоб ініціалізувати проект...  використовуй команду sudo python3 2_17.py install