import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"
# Test
emails = [
    "student123@university.kz",
    "wrong-email@com",
    "test.user@mail.com"
]
for e in emails:
    print(e, "->", validate_email(e))



import re
text = """
Contact numbers:
+7 777 123 4567
+7 701 987 6543
Office: 87001234567
"""
pattern = r'\+?7\s?\d{3}\s?\d{3}\s?\d{4}'
numbers = re.findall(pattern, text)
print("Found phone numbers:")
for num in numbers:
    print(num)