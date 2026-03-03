import re
text = "Years: 1999, 2023, 76, 2026"
pattern = r'\b\d{4}\b'
matches = re.findall(pattern, text)
print("4-digit years:", matches)


import re
text = "Python is fun, powerful, and versatile"
pattern = r'\b[a-zA-Z]{5,}\b'
matches = re.findall(pattern, text)
print("Words with 5+ letters:", matches)


import re
numbers = ["7771234", "7019876543", "123", "888999000"]
pattern = r'^\d{7,10}$'
for num in numbers:
    if re.match(pattern, num):
        print(num, "→ Valid number")
    else:
        print(num, "→ Invalid number")