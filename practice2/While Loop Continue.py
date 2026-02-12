while condition:
    if some_condition:
        continue  


words = ["apple", "skip", "board", "real"]
index = 0
while index < len(words):
    if words[index] == "s":
        index += 1
        continue  
    print(words[index])
    index += 1



