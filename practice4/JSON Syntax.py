import json
sample = {
    "bool": True,
    "none_val": None,
    "list": [1, 2, 3]
}
print(json.dumps(sample))


import json
json_data = '{"name": "Bob", "age": 25, "skills": ["Python","JS"]}'
python_obj = json.loads(json_data)
print(python_obj)
print("Name:", python_obj["name"])
print("First skill:", python_obj["skills"][0])


import json
quiz = {
    "question": "What is the capital of France?",
    "options": ["Paris", "London", "Berlin", "Madrid"],
    "answer": "Paris"
}
quiz_json = json.dumps(quiz, indent=2)
print(quiz_json)