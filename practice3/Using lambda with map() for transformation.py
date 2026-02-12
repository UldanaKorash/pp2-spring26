grades = [60, 75, 80, 90]
new_grades = list(map(lambda x: x * 1.1, grades))
print(new_grades)


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)


names = ["uldana", "arman", "dias"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(capitalized)
