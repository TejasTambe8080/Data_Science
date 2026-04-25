
import re

data = [
    "  Tejas123@gmail.com ",
    "RAHUL@@test.com",
    "anita#mail.com"
]

valid_emails = []

# Email regex pattern (standard)
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

for email in data:
    clean_email = email.strip()   # remove spaces
    
    if re.match(pattern, clean_email):
        valid_emails.append(clean_email)

print(valid_emails)