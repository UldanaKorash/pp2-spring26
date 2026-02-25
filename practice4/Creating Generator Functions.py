def simple_gen():
    yield "Hello"
    yield "World"
    yield "!"
gen = simple_gen()
for word in gen:
    print(word)


def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i
for num in square_numbers(5):
    print(num)



def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2
gen = even_numbers(10)
print(next(gen))
print(next(gen))
print(next(gen))