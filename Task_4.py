
class Contactlist(list):
    def __init(self, name, surname):
        self.name = name
        self.surname = surname
        Contacts.all_contacts.append(self)

    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = Contactlist()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


contact1 = Contact('Вася П.', 'vasya_p@example.com')
contact2 = Contact('Вася Н.', 'vasya_n@example.com')
contact3 = Contact('Елена О.', 'elena@example.com')
contact4 = Contact('Татьяна Н.', 'tanya@example.com')

print([c.name for c in Contact.all_contacts.search('Вася')])