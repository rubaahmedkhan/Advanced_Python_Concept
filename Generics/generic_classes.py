from typing import TypeVar , Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get(self)  -> T :
        return self.item
    
init_box = Box(123) 
str_box = Box("hello")   

print(init_box.get())   # 123
print(str_box.get())    # hello