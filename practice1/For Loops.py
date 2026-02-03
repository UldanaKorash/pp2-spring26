fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")


word = "Python"
for letter in word:
    print(letter)


responses = ["yes", "", "maybe", "", "no"]
for response in responses:
    if response == "":
        continue  
    print(f"Response: {response}")


colors = ["Red", "Yellow", "Green", "Blue"]
for color in colors:
    if color == "Red":
        print("Stop")
    elif color == "Yellow":
        print("Get ready")
    else:
        print("Go")
