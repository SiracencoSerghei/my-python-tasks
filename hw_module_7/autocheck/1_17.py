""" Для ініціалізації свого проекту створіть допоміжну функцію
do_setup(args_dict), яка буде викликати функцію setup з параметрами зі словника args_dict.
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
from setuptools import setup

def do_setup(args_dict):
    """Функція для ініціалізації проекту"""
    setup(
        name=args_dict["name"],
        version=args_dict["version"],
        description=args_dict["description"],
        url=args_dict["url"],
        author=args_dict["author"],
        author_email=args_dict["author_email"],
        license=args_dict["license"],
        packages=args_dict["packages"],
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

    # Викликаємо функцію do_setup() з параметрами
    do_setup(ARGS_DICT)
    
    
    # Щоб ініціалізувати проект...  використовуй команду sudo python3 1_17.py install