# Define all functions for Task 1 here.
# Any necessary import statements should go at the top of each module.
# For example, if you need Numpy in your Task 1 functions:
import numpy as np
import random

def unsafe_floor_sqrt(x):
    return int((x + 0.5)**(1/2))

def check_floor_root(n, r, power = 2):
    return (r**power <= n) and (n < (r + 1)**power)

def random_number(n):
    return random.randint(10**(n-1), 10**n - 1)

def unsafe_failure_rate(number_sizes, samples = 500):
    '''randomly generates a sample of size samples with size digits for each size in the list number_sizes
       then counts how many times unsafe_floor_sqrt gives an incorrect result in each sample using check_floor_sqrt'''
    #generate a list containing a list of random numbers of each size given in number_sizes
    samples = [[random_number(size) for i in range(samples)] for size in number_sizes]
    #construct a list from counting the number of failures with check_floor_root  for each sample in samples
    return [list(map(lambda x: check_floor_root(x, unsafe_floor_sqrt(x), 2), sample)).count(False) for sample in samples]

def floor_square_root(n):
    #same function as floor_root just with a different name and power = 2
    return floor_root(n)

def floor_root(n, power = 2):
    '''Safely calculates the floor square root of a number never using floats
       Implements the algorithm derived in A1.ipynb'''
    #initialize the root as a default of 0 and cast n to a string
    root, n = ["0"], str(n)
    #ensure the length of n is a multiple of power
    n = "0"*(power - (len(n) % power)) + n
    #divide n into chunks of digits of size power
    chunks = [n[i:i+power] for i in range(0, len(n), power)]

    #for every chunk apply the safe square root algorithm
    for i in range(1, len(chunks) + 1):
        #check every possible digit to add to the solution
        for j in range(10):
            #if the root so far with the digit appended is the floor square root of the chunks so far add the digit and move to the next chunk
            if check_floor_root(int(''.join(chunks[0:i])), int(''.join(root))*10 + j, power):
                root.append(str(j))
                break
    #combine the found root into an int
    return(int(''.join(root)))
