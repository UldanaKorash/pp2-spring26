def maximum(a, b):
    return a if a > b else b
print(maximum(10, 25))


def squares(n):
    return [i**2 for i in range(n)]
print(squares(6))


def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(safe_divide(10, 2))


def min_max(numbers):
    return min(numbers), max(numbers)
print(min_max([4, 7, 1, 9]))
