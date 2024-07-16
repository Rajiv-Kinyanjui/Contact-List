class Contact:
    """
    class that generates new instances of contacts
    """
    contact_list = [] #Empty contact list
    def __init__(self, first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        Contact.contact_list.append(self)

    def delete_contact(self):
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        """
        method that takes in a number and returns a contact that matches that number
        """
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact