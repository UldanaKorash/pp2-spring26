words = ["apple", "skip", "banana", "cherry"]
for word in words:
    if word == "skip":
        continue  
    print(f"Word: {word}")


responses = ["yes", "", "maybe", "", "no"]
for response in responses:
    if response == "":
        continue  
    print(f"Response: {response}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        continue 
    print(f"Odd number: {num}") 