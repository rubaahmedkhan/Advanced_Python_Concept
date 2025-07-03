class Duck:
    def quack(self):
        return f"Quack"
    
class Person:
    def quack(self):
        return "I am quacking like a Duck"    
    

def in_the_forest(animal):         
    print(animal.quack())  

donald = Duck()
john  = Person()


print(in_the_forest(donald))
print(in_the_forest(john))