import json
data = {
    "name": "Aldana",
    "age": 20,
    "city": "Almaty",
    "skills": ["Python", "JavaScript"]
}
json_string = json.dumps(data)
print("JSON string:", json_string)


import json
fruits = ["apple", "banana", "cherry"]
json_list = json.dumps(fruits)
print("JSON list:", json_list)


