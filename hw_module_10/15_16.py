"""Продовжуємо розширювати функціональність класу Contacts. На цьому етапі ми додамо до класу метод get_contact_by_id. Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді."""

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == int(id):
                return contact
        return None

# Example usage:

# Create an instance of the Contacts class:
my_contacts = Contacts()
# Add contacts using the add_contacts method:
my_contacts.add_contacts("Wylie Pope'", "(692) 802-2949", "est@utquamvel.net", False)
my_contacts.add_contacts("Cyrus Jackson", "(501) 472-5218", "nibh@semsempererat.com", False)
# Print the contact with searching id :
searching_id = input('Input ID: ')
print(f"Contact with id {searching_id} is: {my_contacts.get_contact_by_id(searching_id)}")
                