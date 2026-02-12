class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking!")

d = Dog("Rex")
d.bark()
