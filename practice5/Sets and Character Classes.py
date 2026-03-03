import re
text = "Python3 Is AWESOME 2026"
lowercase = re.findall(r'[a-z]', text)
uppercase = re.findall(r'[A-Z]', text)
digits = re.findall(r'[0-9]', text)
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Digits:", digits)


import re
text = "User@Name#2026!!"
cleaned = re.sub(r'[^A-Za-z0-9]', '', text)
print("Original:", text)
print("Cleaned:", cleaned)


import re
text = "cab abc dog cat bac"
matches = re.findall(r'\b[abc]+\b', text)
print("Only a/b/c words:", matches)