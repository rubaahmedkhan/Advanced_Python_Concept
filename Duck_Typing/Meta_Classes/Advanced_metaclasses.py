# Advanced metaclass example with validation

# Define a metaclass that enforces a 'process' method
class ValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Check if the class being created has a method called 'process'
        if 'process' not in dct:
            raise TypeError(f"Class '{name}' must define a method called 'process'")
        
        print(f"✅ Class '{name}' created successfully with 'process' method.")
        return super().__new__(cls, name, bases, dct)

# This class will work because it has a 'process' method
class DataProcessor(metaclass=ValidationMeta):
    def process(self):
        print("Processing data...")

# This class will raise an error because it lacks 'process'
# Uncomment to test
# class InvalidProcessor(metaclass=ValidationMeta):
#     pass
