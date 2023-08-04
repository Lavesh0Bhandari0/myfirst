def hello_world():
    print("Hello world!")


hello_world()


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2 is not int):
        return 0
    return num1 + num2


print(sum(10, 20.5))


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_names_itmes(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_names_itmes(first="lavesh", last="bhandari")
