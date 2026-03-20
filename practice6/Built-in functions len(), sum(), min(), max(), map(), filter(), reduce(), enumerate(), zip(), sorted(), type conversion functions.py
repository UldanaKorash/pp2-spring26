nums = [5, 2, 9, 1, 7]
print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))


data = ["1", "2", "3", "4"]
nums = list(map(int, data))
print(nums)
print(sum(nums))



nums = [10, 3, 7, 2, 8, 1]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(sorted(evens, reverse=True))


from functools import reduce
names = ["A", "B", "C"]
scores = [10, 20, 30]
paired = list(zip(names, scores))
print(paired)
for i, (n, s) in enumerate(paired):
    print(i, n, s)
total = reduce(lambda a, b: a + b, scores)
print(total)