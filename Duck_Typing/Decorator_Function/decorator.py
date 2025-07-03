def my_decorator(func):
    def wrapper():
        print("Function Start")
        func()
        print("Function End")
    return wrapper


@my_decorator
def say_hello():
    print("hello, Ruba!")

say_hello()    