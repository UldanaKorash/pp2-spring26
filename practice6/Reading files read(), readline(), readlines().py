with open("text.txt", "r") as f:
    first = f.readline()
    second = f.readline()
    print(first.strip(), second.strip())


with open("text.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))


with open("text.txt", "r") as f:
    lines = f.readlines()
    result = [line.upper() for line in lines if line.strip()]
    print(result)