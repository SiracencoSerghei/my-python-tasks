"""Є список contacts, елементи якого - словники контактів наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, який містить електронні адреси всіх контактів зі списку list_contacts. Використовуйте функцію map."""


def get_emails(list_contacts):
    list_emails = list(map(lambda contact: contact["email"], list_contacts))
    return list_emails

contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
]

print(get_emails(contacts))
