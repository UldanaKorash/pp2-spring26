import json
with open("data.json", "r") as f:
    data = json.load(f)
print("Loaded JSON:", data)
print("Name:", data["name"])
print("Age:", data["age"])


import json
with open("fruits.json", "r") as f:
    fruits = json.load(f)
for fruit in fruits:
    print("Fruit:", fruit)


import json
with open("students.json", "r") as f:
    data = json.load(f)
for student in data["students"]:
    print(f"{student['name']} scored {student['grade']}")