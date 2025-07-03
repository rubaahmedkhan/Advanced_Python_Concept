from typing import TypeVar

# only allow init, float
numeric = TypeVar('Numeric', int, float)

def add(a: numeric, b: numeric) -> numeric:
    return a + b


p = add("hello","word")
print(p)