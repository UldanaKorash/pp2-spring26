import re
text = "Contact: support@university.kz, admin@university.kz, helpdesk@mail.com"
pattern = r'[\w\.-]+@[\w\.-]+\.\w{2,}'
matches = re.findall(pattern, text)
print("All emails found:", matches) 


import re
text = "Call us: +7 777 123 4567 or +7 701 987 6543"
pattern = r'\+7\s?\d{3}\s?\d{3}\s?\d{4}'
numbers = re.findall(pattern, text)
print("All phone numbers:", numbers)


import re
text = "Exams: 2026-03-03, 2026-06-01, 2026-09-15"
pattern = r'\d{4}-\d{2}-\d{2}'
dates = re.findall(pattern, text)
print("All exam dates:", dates)