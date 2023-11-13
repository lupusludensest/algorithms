# Decorators/wrappers

from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args):
        print("Inside decorator")
        func(*args)

    return wrapper


# @decor
# def foo():
#     print("Inside function")

# foo()

def foo():
    print("Inside function")


foo = decor(foo)

foo()
print(foo.__name__)


# Inheritance

class flyMixin:
    def fly(self):
        print("Flies")


class Animals:
    def __init__(self, name):
        self.name = name

    def make_sound(self, name):
        print("Sound")


class Dogs(Animals, flyMixin):
    def make_sound(self, name):
        print(f'{name}: "Gaw-gaw"')


class Cats(Animals, flyMixin):
    def make_sound(self, name):
        print(f'{name}: "Meowww"')


dog = Dogs("Bobic")
cat = Cats("Vaska")

dog.make_sound("Bobic")
dog.fly()
cat.make_sound("Vaska")
cat.fly()

# Polymorphism
strng = "Hello, guys"
lst = [1, 'b', 1 == "d", ('tuple', bool)]
print(len(strng))
print(len(lst))

# Solid principles

# Magic methods

# Work with errors in Python
# Type syncing(signatures)
from typing import List


def foo(a: float, b: float) -> float:
    return a / b


# foo(10, 0)
try:
    res = foo(10, 6)
except ZeroDivisionError:
    print("Divide by ZERO is tabu")
else:
    print(res)
finally:
    print("Job is done")

# Asynrchonicy in Python !!!

# SQL (relational data bases) !!!

# Limit, offset !!!