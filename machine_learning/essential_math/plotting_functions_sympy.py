from sympy import *
from sympy.plotting import plot3d

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


def plot_plane():
    x, y = symbols('x y')
    f_x_y = 2*x + 3*y
    plot3d(f_x_y)


plot_plane()


def plot_summation(list_of_items, multiplier):
    summation = sum(multiplier*list_of_items[i] for i in range(0, len(list_of_items)))
    plot(summation)

plot_summation([1,2,5,2,3],3)