# Define all functions for Task 3 here.
import numpy as np
#import scipy.integrate as integrate


def counter(original_f):
    '''
    Decorator to count the number of times original_f is evaluated.
    '''
    # Define our new, decorated function, with added features
    def decorated_f(x):
        # Increment the number of .evals (depending on whether x is a number or an array)
        try:
            l = len(x)
        except:
            l = 1
        decorated_f.evals += l
        
        # Still return the result of the original function
        return original_f(x)
    
    # Initialise the number of evaluations, store it in a new .evals attribute
    decorated_f.evals = 0
    
    # Return the new, decorated function, which now has a .evals value
    return decorated_f


def define_Ka(a):
    '''
    Function which defines and returns a function Ka for a given parameter a.
    The returned function Ka is decorated with counter().
    '''
    @counter
    def Ka(x):
        return 1 / np.sqrt(a - np.cos(x))
    
    # Returns the function itself as an object
    return Ka

def Kintegral(Ka, n):
    '''Numerically integrates Ka with n evaluations of f using the method chosen in A1.ipynb task 3'''
    return trapezoid(Ka, n)

#Do the integral a bunch of ways:
#Note: all integral methods compute the integral from 0 to pi and then double it since Ka is always even this is done for greater accuracy with fewer evalueations
#Left Riemann sum
def riemannL(f, n):
    '''numerically integrates f using left Riemann sum with n calls to f'''
    #calculating x step
    h = np.pi/n
    #setting up points to be evaluated
    points = np.linspace(0, np.pi - h, n)
    #apply left riemann sum rule
    return 2 * np.sum(h * f(points))

#Right Riemann sum
def riemannR(f, n):
    '''numerically integrates f using right Riemann sum with n calls to f'''
    #calculating x step
    h = np.pi/n
    #setting up points to be evaluated
    points = np.linspace(0 + h, np.pi, n)
    #apply right riemann sum rule
    return 2 * np.sum(h * f(points))

#Midpoint rule
def midpoint(f, n):
    '''numerically integrates f using the midpoint rule with n calls to f'''
    #calculating x step
    h = np.pi/(n)
    #setting up points to be evaluated
    points = np.linspace(0, np.pi, n)
    #apply midpoint rule
    return 2 * np.sum(h * f(points))

#Trapezoid Rule
def trapezoid(f, n):
    '''numerically integrates f using the trapezoid rule with n calls to f'''
    #calculating x step
    h = (np.pi)/(n - 1)
    #setting up points to be evaluated
    x = np.linspace(0, np.pi, n)
    #evaluate f at all xs
    values = f(x)
    #apply trapezoid rule
    return (h)*(values[0] + 2 * sum(values[1:n-1]) + values[n-1])

def simpsons(f, n):
    '''numerically integrates f using Simpson's rule with n calls to f'''
    if n % 2 != 0:
         n -= 1
    #calculating x step
    h = np.pi/(n - 1)
    #setting up points to be evaluated
    x = np.linspace(0, np.pi, n)
    values = f(x)
    #apply simpsons rule
    return 2*(h/3) * (values[0] + 2*sum(values[:n-2:2]) + 4*sum(values[1:n-1:2]) + values[n-1])

def simpsons(f, n):
    '''numerically integrates f using Simpson's rule with n or n - 1 calls to f'''
    # ensuring numberof sub intervals is even
    if n % 2 != 0: n -= 1
    #calculating x step
    h = (np.pi - 0) / n
    # apply simpsons rule depending on if it is an odd or even iteration and add in the evaluations at the end points
    return 2* h/3 * (f(0) + f(np.pi) + sum([2*f(0 + i*h) if i%2 == 0 else 4*f(0 + i*h) for i in range(1, n)]))