def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


result = add(2, 3, 4)
print(result)


# keyworded arguments (kwargs)
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


car = Car(make="Nissan", model="GT-R")
print(car.model)
