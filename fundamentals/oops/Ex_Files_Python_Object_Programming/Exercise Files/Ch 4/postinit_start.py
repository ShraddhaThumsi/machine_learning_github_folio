# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes
#this file needs Python3.10 for execution. If unable to change interpreter in the IDE,
# please run this from the terminal using python3.10 postinit_start.py
from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


# # create some Book objects
# b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
# b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
#
# # TODO: use the description attribute
# print(b1.description)
# print(b2.description)
# b1 = Book()
# print(b1)

b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
print(b2)