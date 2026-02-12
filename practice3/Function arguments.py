def power(base, exponent):
    return base ** exponent
print(power(2, 5))


def total_sum(*numbers):
    return sum(numbers)
print(total_sum(5, 10, 15, 20))


def user_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
user_profile(name="Aruzhan", age=20, city="Almaty")


def order(food, size="Medium", *extras, **details):
    print("Food:", food)
    print("Size:", size)
    print("Extras:", extras)
    print("Details:", details)
order("Pizza", "Large", "Cheese", "Olives", table=5, payment="card")
