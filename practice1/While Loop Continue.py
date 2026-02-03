while condition:
    if some_condition:
        continue  


words = ["apple", "skip", "banana", "cherry"]
index = 0
while index < len(words):
    if words[index] == "skip":
        index += 1
        continue  
    print(words[index])
    index += 1


while True:
    text = input("Type something (or 'quit' to stop): ")
    if text == "":
        continue 
    if text.lower() == "quit":
        print("Loop stopped")
        break
    print(f"You typed: {text}")



responses = ["yes", "", "maybe", "", "no"]
index = 0
while index < len(responses):
    if responses[index] == "":
        index += 1
        continue  
    print(f"Response: {responses[index]}")
    index += 1
