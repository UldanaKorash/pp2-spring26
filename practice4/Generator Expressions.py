numbers = (x for x in range(5))
for num in numbers:
    print(num)


squares = (x * x for x in range(6))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4



words = ["apple", "banana", "cat", "elephant", "dog"]
long_words = (word for word in words if len(word) > 4)
for w in long_words:
    print(w)