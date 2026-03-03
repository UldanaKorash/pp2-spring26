import re
text = "Student ID: 20260123, Room: A305"
digits = re.findall(r'\d+', text)
non_digits = re.findall(r'\D+', text)
print("Digits:", digits)
print("Non-digits:", non_digits)



import re
def validate_username(username):
    pattern = r'^\w{5,12}$'
    return bool(re.match(pattern, username))
usernames = ["student_01", "user!", "abc", "validUser123"]
for u in usernames:
    print(u, "->", validate_username(u))