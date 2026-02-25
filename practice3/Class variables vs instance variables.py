class Phone:
    category = "Electronics"   

    def __init__(self, brand):
        self.brand = brand      



p1 = Phone("iPhone")
p2 = Phone("Samsung")
print(p1.category)
print(p2.brand)
