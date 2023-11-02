"""Є список, кожен елемент якого є словником з контактами
 користувача наступного виду:

    {"name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,}
Словник містить ім'я користувача name, його email,
 телефонний номер phone та властивість favorite -
  обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації
 списку контактів за допомогою пакета pickle та зберігання
  отриманих даних у бінарному файлі.

Перша функція write_contacts_to_file приймає два параметри:
 filename - ім'я файлу, contacts - список контактів.
  Вона зберігає вказаний список у файл,
   використовуючи метод dump пакету pickle.

Друга функція read_contacts_from_file читає та повертає
 зазначений список contacts з файлу filename,
  використовуючи метод load пакету pickle."""

import pickle


def write_contacts_to_file(file_name, contacts_list):
    with open(file_name, "wb") as fh:
        pickle.dump(contacts_list, fh)


def read_contacts_from_file(file_name):
    with open(file_name, "rb") as fh:
        unpacked = pickle.load(fh)
        return unpacked


if __name__ == "__main__":
    filename = 'data.bin'
    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "(123) 456-7890",
            "favorite": True,
        },
    ]

    # Записуємо контакти у файл
    write_contacts_to_file(filename, contacts)

    # Зчитуємо контакти з файлу
    loaded_contacts = read_contacts_from_file(filename)

    # Виводимо результат
    for contact in loaded_contacts:
        print(contact)
