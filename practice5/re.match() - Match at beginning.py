import re
text1 = "support@university.kz is the contact email."
text2 = "Contact: admin@university.kz"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}'
match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)
print("Text1:", match1.group() if match1 else "No match")
print("Text2:", match2.group() if match2 else "No match")



import re
text = "2026 is the current year"
pattern = r'^\d+'
match = re.match(pattern, text)
print("Starting number:", match.group() if match else "No number at start")


import re
text1 = "Python is fun"
text2 = "python is fun"
pattern = r'^[A-Z]\w*'
match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)
print("Text1:", match1.group() if match1 else "No match")
print("Text2:", match2.group() if match2 else "No match")