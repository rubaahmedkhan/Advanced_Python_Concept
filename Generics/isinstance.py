x = 5
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False


# Multiple type check
x = "hello"
print(isinstance(x, (int,float)))   # False
print(isinstance(x, (str,list)))    # True


class Animal: pass
class Dog(Animal): pass

dog = Dog()

print(type(dog) == Animal)     # False
print(isinstance(dog, Animal))  # True