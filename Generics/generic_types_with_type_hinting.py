from typing import TypeVar

T = TypeVar('T')

def identity(x:T) -> T:
    return x

print(identity("hello"))
print(identity(123))
print(identity([1,2,3]))