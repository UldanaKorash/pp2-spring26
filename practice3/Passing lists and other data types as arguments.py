def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]
print(filter_even([1, 2, 3, 4, 5, 6]))


def multiply_coordinates(point):
    x, y = point
    return x * y
print(multiply_coordinates((4, 5)))


def update_score(scores, name, points):
    scores[name] = points
    return scores
print(update_score({"Ali": 80}, "Dana", 95))
