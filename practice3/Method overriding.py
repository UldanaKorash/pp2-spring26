class Animal:
    def __init__(self, name):
        self.name = name 
class Cat(Animal):
    def speak(self):
        print("Meow")  
c = Cat("Kitty") 
c.speak() 
print(c.name)  