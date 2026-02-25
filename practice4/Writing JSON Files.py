import json
data = {
    "name": "Aldana",
    "age": 20,
    "city": "Almaty"
}
with open("data.json", "w") as f:
    json.dump(data, f)
print("JSON file created!")



import json
data = {
    "students": ["Alice", "Bob", "Charlie"],
    "grades": [90, 85, 88]
}
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)
print("Formatted JSON file saved!")


import json
fruits = ["apple", "banana", "cherry"]
with open("fruits.json", "w") as f:
    json.dump(fruits, f, indent=2)
print("Fruits JSON saved!")