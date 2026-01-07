"""
Python Notes – Basics to Advanced
---------------------------------
This file contains learning notes and examples covering:
- Strings, Lists, Sets, Tuples
- Generators & Async Generators
- Decorators
- Magic methods
- Typing & docstrings

Author: Prince kumar [AnakinCodeWalker]
"""

from typing import Generator, AsyncGenerator
import asyncio

# -------------------------------------------------
# STRING OPERATIONS
# -------------------------------------------------

print("Hey There buddy !")

name = "Rajaji"

# reverse a string using slicing
# [start : end : step]
print(name[::-1])


# -------------------------------------------------
# LIST OPERATIONS
# -------------------------------------------------

# List can hold mixed data types
List = [1, "Anish"]

print(type(List))

# extend() adds multiple elements at once
List.extend([23, 33, 5])

print(List)


# -------------------------------------------------
# SET OPERATIONS
# -------------------------------------------------

# creates an empty set , doesn't take any set as an args
a = set()  # empty set

set1 = {1, 2, 3}

# a set can not have another set inside of it
# set2 = {1, 2, 3, {2, 3}}  ❌ INVALID

# remove() will throw KeyError if element not present
# set1.remove(4)  ❌ ERROR

# discard() will NOT throw error, returns None
print(set1.discard(4))


# -------------------------------------------------
# TUPLE OPERATIONS
# -------------------------------------------------

Tuple = (1, 2, 3)

# tuple is immutable, convert to list to modify
newList = list(Tuple)

newList.append(4)

# convert back to tuple
Tuple = tuple(newList)

print(Tuple)


# -------------------------------------------------
# print() FUNCTION
# -------------------------------------------------

# print() -> takes 3 args:
# print(*objects, sep=' ', end='\n')


# -------------------------------------------------
# QUESTION - what is unpacking ?
# -------------------------------------------------

# unpacking == object destructuring
# a, b = (1, 2)


# -------------------------------------------------
# SEARCH TOPICS
# -------------------------------------------------

# search on web:
# ollama
# vllm (used in production)
# what is autoscaling ?


# -------------------------------------------------
# TEMPERATURE CONVERSION
# -------------------------------------------------

# WAP to convert Fahrenheit to Celsius

# f = int(input("enter the temp in fahrenheit"))
# c = (f - 32) * 5 / 9
# print(f"temp is {c} degree celsius")


# -------------------------------------------------
# RANGE & GENERATORS
# -------------------------------------------------

print(type(range(4)))  # -> range class

# you could use type inference in python like static typed languages
# used to check and throw error -- pydantic
# to use pydantic you must provide type hints
# typing module helps define custom data types


# range is NOT a generator but behaves like one (lazy evaluation)
# generator lets you pass data into chunks via yield
# instead of passing a large chunk at once
# used heavily in ML / fine-tuning pipelines


# -------------------------------------------------
# QUESTION - WHAT IS YIELD ?
# -------------------------------------------------

def gen(stop: int) -> Generator[int, None, None]:
    """
    Generator function
    yield pauses execution and returns value one at a time
    """
    for i in range(stop):
        yield i


# consuming generator
for value in gen(5):
    print(value)


# -------------------------------------------------
# ASYNC GENERATOR
# -------------------------------------------------

async def async_gen(stop: int) -> AsyncGenerator[int, None]:
    """
    Async generator
    Used with async for
    """
    for i in range(stop):
        yield i
        await asyncio.sleep(0.1)


# you can not use async outside an async function in python
async def main():
    async for i in async_gen(5):
        print(i)


asyncio.run(main())


# -------------------------------------------------
# MAGIC METHODS (DUNDER METHODS)
# -------------------------------------------------

# magic methods are written inside a class
# they start and end with double underscore (__)

class MyName:
    """
    Example class demonstrating magic methods
    """

    name: str

    def __init__(self, name: str):
        # __init__ is a magic method (constructor)
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


name_obj = MyName("Kabir")
name_obj.greet()


# -------------------------------------------------
# PYTHON DOCSTRING
# -------------------------------------------------

# Docstring is written using triple quotes
# used for documentation and introspection
# accessible using help() or __doc__


# -------------------------------------------------
# DECORATORS
# -------------------------------------------------

# yaha pr myfunction aya then we will access it
def changecase(func):
    """
    Decorator function
    Modifies behavior of another function
    """
    def myinner():
        return func().upper()
    return myinner


# this specifies ki yeh decorator hai
@changecase
def myfunction():  # --> yaha se changecase mai jayega
    return "Hello sally"


print(myfunction())
