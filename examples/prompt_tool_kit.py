#!/usr/bin/python

import readline
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Список доступних команд
commands = ["add_contact", "edit_contact", "search_contacts", "add_note", "edit_note", "search_notes", "exit"]

# Створюємо об'єкт WordCompleter зі списку команд
completer = WordCompleter(commands)

# Зчитуємо введення користувача
while True:
    user_input = prompt("Введіть команду: ", completer=completer)

    # Ваш код обробки введення користувача
    print(f"Ви ввели: {user_input}")

    completer.get_completions()

    # Вийти з циклу при введенні "exit"
    if user_input == "exit":
        break
