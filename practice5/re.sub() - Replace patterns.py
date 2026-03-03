import re
text = "Python    is   very    powerful"
cleaned = re.sub(r'\s+', ' ', text)
print("Before:", text)
print("After:", cleaned)


import re
text = "Room101, Room202, Room303"
masked = re.sub(r'\d+', '#', text)
print("Masked text:", masked)



import re
log = "Server started on 2026-03-03 at 10:00"
formatted = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', log)
print("Formatted log:", formatted)