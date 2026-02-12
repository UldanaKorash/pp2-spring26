for item in iterable:
    if some_condition:
        break  


colors = ["Red", "Yellow", "Green", "Blue"]
for color in colors:
    if color == "Green":
        print("Green found! Stop the loop.")
        break
    print(f"Current color: {color}")


answers = ["maybe", "no", "yes", "not sure"]
for answer in answers:
    if answer == "yes":
        print("Correct answer found!")
        break
    else:
        print(f"Checking: {answer}")