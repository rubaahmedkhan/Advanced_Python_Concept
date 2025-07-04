def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            print("Creating new instance via decorator...")
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class Logger:
    def __init__(self):
        print("Logger initialized")

l1 = Logger()
l2 = Logger()

print(l1 is l2)  # True
