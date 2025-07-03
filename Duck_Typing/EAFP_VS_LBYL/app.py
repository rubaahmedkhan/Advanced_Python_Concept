# LBYL Approach ( LOOK BEFORE YOU LEAP )
class Cat:
    def meow(self):
        print("meow meow")
cat = Cat()   

if hasattr(cat,"meow"):
    cat.meow()
else:
    print("Can't meow!")    

# EAFP Approach ( Easier to Ask Forgiveness than Permission)   
try:
    cat.meow()
except AttributeError:
    print("Can't meow")     