while condition:
    if some_condition:
        break  


while True:
    command = input("Enter command: ")
    if command.lower() == "quit":
        print("Loop stopped")
        break
    else:
        print(f"You typed: {command}")


words = ["apple", "banana", "cherry", "date"]
index = 0
while True:
    if words[index] == "cherry":
        print("Cherry found!")
        break
    index += 1


