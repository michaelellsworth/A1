# Define all functions for Task 1 here.
# Any necessary import statements should go at the top of each module.
# For example, if you need Numpy in your Task 1 functions:
import numpy as np
import random

def unsafe_floor_sqrt(x):
    '''calculate the floor square root using floats'''
    return int((x + 0.5)**(1/2))

def check_floor_root(number, root, power = 2):
    '''check if root is the powerth floor root of number'''
    return (root**power <= number) and (number < (root + 1)**power)

def random_number(digits):
    '''generate a random number with number of digits, digits'''
    return random.randint(10**(digits-1), 10**digits - 1)

def unsafe_failure_rate(number_sizes, samples = 500):
    '''randomly generates a sample of size samples with size digits for each size in the list number_sizes
       then counts how many times unsafe_floor_sqrt gives an incorrect result in each sample using check_floor_sqrt
       Returns the failure rate as a number between 0 and 1'''
    #generate a list containing a list of random numbers of each size given in number_sizes
    sample_sets = [[random_number(size) for i in range(samples)] for size in number_sizes]
    #construct a list from counting the number of failures with check_floor_root  for each sample in samples
    failure_count = [list(map(lambda x: check_floor_root(x, unsafe_floor_sqrt(x), 2), sample)).count(False) for sample in sample_sets]
    n = [float(count)/samples for count in failure_count]
    return n

def floor_square_root(number):
    '''Safely calculates the floor square root of a number never using floats
       Implements the algorithm derived in A1.ipynb
       Equivelant to floor_root with power = 2'''
    #initialize the root as a default of 0 and cast number to a string
    root, number = ["0"], str(number)
    #ensure the length of number is a multiple of power
    number = "0"*(2 - (len(number) % 2)) + number
    #divide number into chunks of digits of size power
    chunks = [number[i:i+2] for i in range(0, len(number), 2)]

    #for every chunk apply the safe square root algorithm
    for i in range(1, len(chunks) + 1):
        #check every possible digit to add to the solution
        for j in range(10):
            #if the root so far with the digit appended is the floor square root of the chunks so far add the digit and move to the next chunk
            if check_floor_root(int(''.join(chunks[0:i])), int(''.join(root))*10 + j, 2):
                root.append(str(j))
                break
            
    #combine the found root into an int
    return(int(''.join(root)))

def floor_root(number, power = 2):
    '''Safely calculates the floor square root of a number never using floats
       Implements the algorithm derived in A1.ipynb'''
    #initialize the root as a default of 0 and cast number to a string
    root, number = ["0"], str(number)
    #ensure the length of number is a multiple of power
    number = "0"*(power - (len(number) % power)) + number
    #divide number into chunks of digits of size power
    chunks = [number[i:i+power] for i in range(0, len(number), power)]

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
