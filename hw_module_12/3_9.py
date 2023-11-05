"""Є список, кожен елемент якого є словником з контактами
 користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер
 phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку
контактів за допомогою пакету csv та зберігання отриманих даних у
текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри:
filename - ім'я файлу, contacts - список контактів.
Вона зберігає вказаний список у файлі формату csv.

Структура csv файлу має бути такою:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.

Друга функція read_contacts_from_file читає, виконує перетворення даних
 та повертає вказаний список contacts із файлу filename, збереженого
  раніше функцією write_contacts_to_file.

Примітка: При читанні файлу csv ми отримуємо властивість словника
 favorite у вигляді рядка, тобто. наприклад favorite='False' .
 Необхідно його привести до логічного виразу назад, щоб стало
 favorite=False."""
# ============================================================

import csv


def write_contacts_to_file(write_filename, write_contacts):
    with open(write_filename, "w", newline="") as fh:
        header = write_contacts[0].keys()
        contact_writer = csv.DictWriter(fh, fieldnames=header)
        contact_writer.writeheader()
        for contact in write_contacts:
            contact_writer.writerow(contact)


def read_contacts_from_file(input_filename):
    contacts_output = []
    with open(input_filename, "r") as fh:
        contacts_reader = csv.DictReader(fh)
        for row in contacts_reader:
            row["favorite"] = (row["favorite"] == 'True')
            # row.update({"favorite": row["favorite"] == 'True'})

            contacts_output.append(row)
    return contacts_output


filename = "contacts.csv"
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Siracenco Serghei",
        "email": "siracencoserghei@example.com",
        "phone": "(992) 914-3755",
        "favorite": True,
    }
]
write_contacts_to_file(filename, contacts)
print(read_contacts_from_file(filename))

# ===========================================================

# import csv
#
#
# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w", newline="") as fh:
#         header = contacts[0].keys()
#         contact_writer = csv.DictWriter(fh, fieldnames=header)
#         contact_writer.writeheader()
#         for contact in contacts:
#             contact_writer.writerow(contact)
#
#
#
# def read_contacts_from_file(filename):
#     contacts = []
#     with open(filename, "r") as fh:
#         contacts_reader = csv.DictReader(fh)
#         # header = contacts_reader.fieldnames
#         # rows = csv.DictReader(fh, fieldnames=header)
#         # print(header)
#         # print(rows)
#         for row in contacts_reader:
#             row['favorite'] = row['favorite'] == 'True'
#             # print(row)
#             # print(dict(row))
#             # contacts.append(dict(row))
#             contacts.append(row)
#     return contacts
#
# filename = "contacts.csv"
# contacts = [
# {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# },
# {
#     "name": "Siracenco Serghei",
#     "email": "siracencoserghei@example.com",
#     "phone": "(992) 914-3755",
#     "favorite": True,
# }
# ]
# # write_contacts_to_file(filename, contacts)
# read_contacts_from_file(filename)
# print(read_contacts_from_file(filename))
