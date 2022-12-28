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


#plot the following functions using Sympy
#source: https://tutorial.math.lamar.edu/problems/calci/diffformulas.aspx
#1. g(z) = 4z^7-3z^-7+9z
#2. g(x) = x^1/3
#3. f(x) = sqrt(x) + 8cubroot(x) - 2fourthroot(x)

def plot_nthroot(nth_root,power=False):
    x = symbols('x')
    if power:
        g_z = x**nth_root
    else:
        g_z = x ** (1/nth_root)
    print(g_z.subs(x,2))
    return g_z

def prob1():
    x = symbols('x')
    g_z = (4 * plot_nthroot(7,True)) - (3 * plot_nthroot(-7,True)) + 9*x
    print(g_z.subs(x,2))
    plot(g_z)
#plot_nthroot(2,power=True)

prob1()
