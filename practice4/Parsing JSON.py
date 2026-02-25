import json
json_data = '{"name": "Aldana", "age": 20, "city": "Almaty"}'
python_obj = json.loads(json_data)
print("Python object:", python_obj)
print("Name:", python_obj["name"])
print("Age:", python_obj["age"])


import json
with open("data.json", "r") as f:
    data = json.load(f)
for student in data["students"]:
    print(f"{student['name']} scored {student['grade']}")
    