# Simple metaclass example

# Define a metaclass
class SimpleMeta(type):
    class_count = 0  # Keeps track of how many classes are created

    def __new__(cls, name, bases, dct):
        # Increment the class count
        cls.class_count += 1
        print(f"Creating class: {name} (Total classes: {cls.class_count})")
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a class definition
class MyClassA(metaclass=SimpleMeta):
    pass

class MyClassB(metaclass=SimpleMeta):
    pass

# Output will show how many classes were created using the metaclass
