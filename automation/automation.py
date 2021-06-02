import shutil
import re


# email_pattern = "[a-z0-9]+@[a-z]+\.(com|org|net)"
email_pattern = '[\w\.-]+@[\w\.-]+'
phone_pattern = '[0-9*]'


with open('potential-contacts.txt','r') as f:
    potential_contacts_file=f.read()
    emails=re.findall(email_pattern, potential_contacts_file)
    phone_numbers=re.findall(phone_pattern, potential_contacts_file)


with open('emails.txt','w') as f:
    # remove dupllicates
    emails = list(set(emails))
    # sort emails in an ascending order
    emails.sort()
    for element in emails:
        f.write(element+"\n")

with open('phone_numbers.txt','w') as f:
    # remove dupllicates
    phone_numbers = list(set(phone_numbers))
    # sort emails in an ascending order
    phone_numbers.sort(key=float)
    # write each phone number
    for number in phone_numbers:
        f.write(number+"\n")
