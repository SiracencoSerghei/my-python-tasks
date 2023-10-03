
from setuptools import setup

def do_setup(args_dict, requires, entry_points):
    setup(
        name=args_dict['name'],
        version=args_dict['version'],
        description=args_dict['description'],
        url=args_dict['url'],
        author=args_dict['author'],
        author_email=args_dict['author_email'],
        license=args_dict['license'],
        packages=args_dict['packages'],
        install_requires=requires,
        entry_points={
            'console_scripts': entry_points['console_scripts'],
        },
    )

if __name__ == "__main__":
    # Структура словника для entry_points
    entry_points = {
        'console_scripts': [
            'script_name = module_name:setup',  # Додайте свої точки входу тут
        ],
    }
    # package requirements:
    requires = [
        'package1==1.0.0',
        'package2>=2.0.0',
        # Add more package requirements as needed
    ]

    # Структура словника для параметра args_dicts
    args_dict = {
        "name": "useful",
        "version": "1",
        "description": "Very useful code",
        "url": "http://github.com/dummy_user/useful",
        "author": "Flying Circus",
        "author_email": "flyingcircus@example.com",
        "license": "MIT",
        "packages": ["useful"],
    }

    # Викликаємо функцію do_setup з новим параметром entry_points
    do_setup(args_dict, requires, entry_points)
    
    
    # for run script:
    # python3 3_17.py install
    # pip install -e .
    
    
