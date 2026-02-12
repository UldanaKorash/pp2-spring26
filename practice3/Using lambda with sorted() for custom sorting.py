words = ["apple", "kiwi", "banana", "pear"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)


pairs = [(1, 5), (3, 2), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)


names = ["Aruzhan", "Dana", "Ali", "Madi"]
sorted_names = sorted(names, key=lambda name: name[-1])
print(sorted_names)


