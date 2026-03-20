with open("data.txt", "w") as f:
    f.write("Hello\nWorld\nPython")


nums = [1, 2, 3, 4, 5]
with open("numbers.txt", "w") as f:
    for n in nums:
        f.write(str(n * n) + "\n")
    


text = input("Enter text: ")
with open("notes.txt", "a") as f:
    f.write(text + "\n")