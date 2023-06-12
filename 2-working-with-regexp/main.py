import re
import csv
'''
fake_emails = [
    'user1@example.com',
    'user2@example.com',
    'user3@example.com',
    'user4@example.com',
    'user5@example.com',
    'user6@example.com',
    'user7@example.com',
    'user8@example.com',
    'user9@example.com',
    'user10@example.com'
]
'''

# change the domain from 'example.com' to example.xyz


def change_domain(email, new_domain):
    pattern = r'@(.+)$'

    new_email = re.sub(pattern, '@' + new_domain, email)

    return new_email


# fake_emails = [change_domain(email, 'yahoo.com') for email in fake_emails]

# print(fake_emails)
data = []
with open('accounts.csv', 'r') as accounts:
    reader = csv.DictReader(accounts, fieldnames=[
                            'Name', 'Email Address', 'Occupation'])
    for account in reader:
        old_email_address = account.get('Email Address')
        updated_email_address = change_domain(old_email_address, 'example.xyz')
        account['Email Address'] = updated_email_address
        data.append(account)

# Create an updated csv file

with open('accounts_updated.csv', 'w', newline='') as accounts_updated:
    writer = csv.DictWriter(accounts_updated, fieldnames=[
                            'Name', 'Email Address', 'Occupation'])
    # writer.writeheader()

    for value in data:
        writer.writerow(value)
