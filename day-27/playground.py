def add(*numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


print(add(1, 2, 3, 4, 5))
print(add(10, 50))
print(add(10))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-model", colour="red")
print(my_car.model, my_car.make)
