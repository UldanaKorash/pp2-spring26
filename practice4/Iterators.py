numbers = [10, 20, 30, 40]
my_iter = iter(numbers)  
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
print(next(my_iter))  # 40

fruits = ["apple", "banana", "cherry"]
fruit_iter = iter(fruits)
while True:
    try:
        print(next(fruit_iter))
    except StopIteration:
        print("Iteration finished!")
        break


word = "PYTHON"
letter_iter = iter(word)
print(next(letter_iter))  # P
print(next(letter_iter))  # Y
print(next(letter_iter))  # T