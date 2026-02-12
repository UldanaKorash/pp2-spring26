while condition:
    if some_condition:
        break  


while True:
    command = input()
    if command.lower() == "quit":
        print("stop")
        break
    else:
        print(f"You typed: {command}")


