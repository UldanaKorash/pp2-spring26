command = ""
while command != "stop":
    command = input("Enter command: ")
    if command != "stop":
        print(f"You typed: {command}")
print("Loop ended")


answer = ""
while answer.lower() != "python":
    answer = input("Programming language: ")
    if answer.lower() != "python":
        print("Try again!")
print("Correct! It's Python!")