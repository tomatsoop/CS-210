"""
CS 210 Lab 3 - Pizza_CPSI
Author:[Sabrina Zhang]
Pizza and Doctest

"""

import math
import doctest


def pizza_CPSI(diameter, cost):
    #Doctest is doctesting the doc down here:
    '''
    (int, num) -> float
    Calculates and returns the cost per square inch,
    given the diameter and cost of a pizza.
    Examples:
    >>> pizza_CPSI(14, 18)
    0.117
    >>> pizza_CPSI(14, 20.25)
    0.132
    '''
    
    area = circle_area(diameter) 
 
    cost_per_inch = cost/area 
    #print(cost_per_inch)
    cost_per_inch = round(cost_per_inch, 3)
    return cost_per_inch

def circle_area(diameter):
    r = diameter / 2 
    #circle area takes the parameter diameter
    # and divides it by 2
    
    area = math.pi* (r **2)
    # Find the area by doing pi*r^2
    return area
#rember to return what number you want in the function

diameter = 14
cost = 20.25


result = pizza_CPSI(diameter, cost)



print(doctest.testmod())