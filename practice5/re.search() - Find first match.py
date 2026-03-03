import re
text = "Contact us: support@university.kz, admin@university.kz"
match = re.search(r'[\w\.-]+@[\w\.-]+\.\w{2,}', text)
if match:
    print("First email found:", match.group())
else:
    print("No email found")


import re
text = "Call +7 777 123 4567 or +7 701 987 6543"
pattern = r'\+7\s?\d{3}\s?\d{3}\s?\d{4}'
match = re.search(pattern, text)
if match:
    print("First phone number:", match.group())


import re
text = "python is fun. Python is powerful."
pattern = r'\b[A-Z][a-z]*\b'
match = re.search(pattern, text)
if match:
    print("First capitalized word:", match.group())