def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("level")) 


def average(numbers):
    return sum(numbers) / len(numbers)
print(average([10, 20, 30])) 


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))


def cube(number):
    return number ** 3
print(cube(3))


def greet(name):
    return f"Hello, {name}!"

print(greet("Uldana"))
