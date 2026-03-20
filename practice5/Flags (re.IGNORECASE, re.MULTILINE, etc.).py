import re
text = "Python is powerful. python is fun."
pattern = r'python'
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print("Matches ignoring case:", matches)


import re
text = """ERROR: Failed login
INFO: Server started
WARNING: Low disk space"""
pattern = r'^(ERROR|WARNING)'
matches = re.findall(pattern, text, flags=re.MULTILINE)
print("Critical logs:", matches)