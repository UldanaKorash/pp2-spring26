command = ""
while command != "stop":
    command = input("Enter command: ")
    if command != "stop":
        print(f"You typed: {command}")
print("Loop ended")


found = False
colors = ["Red", "Yellow", "Blue", "Green"]
index = 0
while not found and index < len(colors):
    if colors[index] == "Blue":
        found = True
        print("Blue found!")
    index += 1


answer = ""
while answer.lower() != "python":
    answer = input("Guess the programming language: ")
    if answer.lower() != "python":
        print("Try again!")
print("Correct! It's Python!")
