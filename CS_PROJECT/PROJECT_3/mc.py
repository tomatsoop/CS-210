"""
CS 210 Project 3 - Monte Carlo
Author:[Sabrina Zhang]
Computing Pi
References : 
        Used Textbook for Code
"""

import random
import math
import turtle 


def montePi(numDarts):
    inCirlce = 0 
    
    for i in range(numDarts):
        x  = random.random()
        y = random.random()
        
        distance = math.sqrt(x**2 + y**2)
        
        if distance <= 1:
            inCirlce = inCirlce + 1
            
    pi = inCirlce / numDarts * 4 
    
    return pi 

random.seed(42)
#random seed isnt called in all_pi file so it prints 3.14
#but on here it prints 3.12 
#does the random seed need to be called somwehrre

if __name__ == "__main__":
    
    print(montePi(100))
  
    
    
    
    