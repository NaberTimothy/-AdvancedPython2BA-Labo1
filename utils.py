# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt



def fact(n):
    total = 1
    if n == 0:
        total = 1
    while n > 0:
        total *= n
        n-=1
    return total

def roots(a, b, c):

    delta =((b**2) - (4*a*c))
    if delta > 0:
        x1=((-b + sqrt(delta))/(2*a))
        x2 =((-b - sqrt(delta))/(2*a))
        return (x1,x2)

    if delta == 0:
        x= (-b/2*a)
        return x

    if delta < 0:
        return None
    pass

def integrate(function, lower, upper):


    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(2, 5, 2))
    print(integrate('x ** 2 - 1', -1, 1))
