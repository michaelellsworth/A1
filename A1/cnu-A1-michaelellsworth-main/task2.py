import numpy as np
import sys

sys.setrecursionlimit(1500)

red    = ['RED']
yellow = ['YELLOW']
blue   = ['BLUE']
purple = [red, blue]
green  = [yellow, blue]
joker  = [purple, green]

def flatten(list_of_lists):
    '''recursively flatten a list of nested lists'''
    #if all elements of the list have been checked return
    if len(list_of_lists) == 0:
        return list_of_lists
    
    #recursively run on the first element to unpack it and then run on the rest of the list to continue iterating
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    
    #recombine list and return
    return list_of_lists[:1] + flatten(list_of_lists[1:])



def price(widget, r, y, b):
    '''given prices for red yellow abd blue base widgets return the total price of any compound widget'''
    #define dictionary to convert names to prices
    price_converter = {'RED': r, 'YELLOW': y, 'BLUE': b}
    #unpack into a 1D list of just base components
    parts = flatten(widget)
    #map all base widgets to prices and take the sum
    return sum([price_converter[part] for part in parts])

def constituents(widget):
    '''return a list with the number of component red yellow and blue base widgets in that order'''
    #unpack into a 1D list of just base components and counts each type using built in funtions
    parts = flatten(widget)
    return [parts.count("RED"), parts.count("YELLOW"), parts.count("BLUE")]

def reconstruct_prices(orders, totals):
    '''given at least three compound widgets and their prices find the prices of the base red yellow and blue widgets
       assumes at least three of the compund widgets will produce linearly independent equations of red yellow and blue'''
    #find the number of each red, yellow, and blue widget in each element of orders and then making them a coefficient matrix
    coeff_matrix = np.matrix([constituents(order) for order in orders])
    #initialize indices of linearly independent rows (row1 will always remain 0)
    row1, row2, row3 = 0, 0, 0

    #find two vectors with non zero cross product so they are linearly independent (first 2 of the three needed)
    for i, row in enumerate(coeff_matrix[1:]):
        if(not(np.array_equal(np.cross(row, coeff_matrix[row1]), [0, 0, 0]))):
            row2  = i + 1
            break

    #find a third linearly indepedent vector by checking a matrix made up of the two already found and each possible third to find one with a non zero determinant
    for i, row in enumerate(coeff_matrix):
        if np.linalg.det(np.matrix(np.concatenate((coeff_matrix[row1], coeff_matrix[row2], row)))) != 0:
            row3 = i
            break

    #create 3x3 matrix of 3 linearly independent equations from orders
    m = np.matrix(np.concatenate((coeff_matrix[row1], coeff_matrix[row2], coeff_matrix[row3])))
    #solve the system of equations defined by the matrix m and the entried in totals corresponding to the lienarly inependent rows
    return [round(x, 2) for x in list(np.linalg.solve(m, [totals[row1], totals[row2], totals[row3]]))]