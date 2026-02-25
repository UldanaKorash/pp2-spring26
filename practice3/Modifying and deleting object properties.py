class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Ali", 20)
p.age = 21      
del p.name      
print(p.age)
