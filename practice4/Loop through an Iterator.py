numbers = [1, 2, 3, 4]
my_iter = iter(numbers)
while True:
    try:
        value = next(my_iter)
        print(value)
    except StopIteration:
        break


numbers = [10, 20, 30]
my_iter = iter(numbers)
for num in my_iter:
    print(num)


word = "HELLO"
letter_iter = iter(word)
for letter in letter_iter:
    print("Letter:", letter)