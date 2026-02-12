def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
print(celsius_to_fahrenheit(25))


def reverse_word(word):
    return word[::-1]
print(reverse_word("python"))


def rectangle_area(width, height):
    return width * height
print(rectangle_area(5, 8))


def is_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"
print(is_even(17))
