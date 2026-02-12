numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


grades = [50, 85, 72, 40, 90]
passed = list(filter(lambda x: x >= 70, grades))
print(passed)


words = ["apple", "kiwi", "banana", "pear"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)
