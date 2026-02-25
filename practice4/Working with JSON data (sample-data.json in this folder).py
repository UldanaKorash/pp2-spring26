import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
print("Loaded JSON data:", data)


import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
for user in data["users"]:
    print(f"User: {user['name']}, Email: {user['email']}")


import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
older_users = [user for user in data["users"] if user["age"] > 25]
with open("older-users.json", "w") as f:
    json.dump(older_users, f, indent=2)
print("Filtered users saved to older-users.json!")