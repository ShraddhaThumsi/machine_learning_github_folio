from sympy import *


def linear_function():
    x = symbols('x')
    f = 2*x+1
    plot(f)


linear_function()


def quadratic_function():
    x = symbols('x')
    f = x**2+1
    plot(f)


quadratic_function()
