class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current
counter = Countdown(5)
for num in counter:
    print(num)


class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value
fib = Fibonacci(7)
for num in fib:
    print(num)