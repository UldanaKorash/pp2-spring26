def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
for num in gen:
    print(num)


def countdown(n):
    while n > 0:
        yield n
        n -= 1
gen = countdown(5)
print(next(gen))  # 5
print(next(gen))  # 4
print(next(gen))  # 3


def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1
for num in fibonacci(7):
    print(num)