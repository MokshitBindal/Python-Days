# putting parameters as * and then a variable name
# we can let this function take as many arguments as possible

def add(*args):
    print(type(args))  # args is a tuple here
    print(args[0])
    sum = 0
    for i in args:
        sum += i
    return sum

# this is unlimited positional arguments


print(add(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))


def calculate(n, **kwargs):
    print(type(kwargs))  # kwargs is a dict here
    # for key, val in kwargs.items():
    #     print(key, val)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

        # when using kwargs["model"], we risk getting a error when it doesnt get model specified
        # so we use get method as it returns None when nothing is received


my_car = Car(make="Buggati") # works
print(my_car.make)
print(my_car.model)
