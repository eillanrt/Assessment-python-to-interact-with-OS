import csv


def fetch_contacts():
    contacts_lst = []
    with open('contacts.csv', 'r') as contacts:
        contacts_reader = csv.DictReader(
            contacts, fieldnames=['First Name', 'Last Name', 'Email Address'])

        for contact in contacts_reader:
            contacts_lst.append(contact)
        return contacts_lst


contacts = fetch_contacts()


def find_email(credentials):
    try:
        first_name = credentials[1]
        last_name = credentials[2]

        for contact in contacts:
            if contact['First Name'] == first_name and contact['Last Name'] == last_name:
                return contact['Email Address']

        return 'No email address found'
    except IndexError:
        return 'Missing parameters'
