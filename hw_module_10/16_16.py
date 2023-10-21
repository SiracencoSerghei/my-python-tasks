"""Завершуємо функціональність класу Contacts. На цьому етапі ми додамо до класу метод remove_contacts. Метод винен видаляти контакт по унікальному id у списку contacts. Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.

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
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
         self.contacts = list(filter(lambda contact: contact["id"] != id, self.contacts))
        # self.contacts = [contact for contact in self.contacts if contact["id"] != id]
        
    # Example usage:

# Create an instance of the Contacts class:
my_contacts = Contacts()
# Add contacts using the add_contacts method:
my_contacts.add_contacts("Wylie Pope'", "(692) 802-2949", "est@utquamvel.net", False)
my_contacts.add_contacts("Cyrus Jackson", "(501) 472-5218", "nibh@semsempererat.com", False)
my_contacts.add_contacts("John Doe", "(123) 456-7890", "john@example.com", True)
my_contacts.add_contacts("Jane Smith", "(987) 654-3210", "jane@example.com", False)

print(my_contacts.list_contacts())
# Remove a contact by ID
my_contacts.remove_contacts(2)

print(my_contacts.list_contacts())