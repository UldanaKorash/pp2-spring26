import re
text = "color colour colouur colr"
pattern = r'colou?r'
matches = re.findall(pattern, text)
print("Matches:", matches)



import re
text = "Grades: A B C D F A C B"
pattern = r'\b[A-C]\b'
grades = re.findall(pattern, text)
print("Valid grades:", grades)


import re
text = "Exam date: 2026-03-03"
pattern = r'(\d{4})-(\d{2})-(\d{2})'
match = re.search(pattern, text)
if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    print("Year:", year)
    print("Month:", month)
    print("Day:", day)