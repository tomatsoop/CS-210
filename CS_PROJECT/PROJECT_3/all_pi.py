"""
CS 210 Project 3 - Estimating Pi method
Author:[Sabrina Zhang]
Calculating error
References : 
        Used Textbook for imported code
"""

#Using from import will import only that function
#from the file called from
from mc import montePi
from arch import pi_arch
from wallis import pi_wallis
import math
import random

def arches(err_total : float):
    num_sides = 1
    #calculate total error by taking abs value
    # minuse pi calcualte the error
    total_error = (abs(pi_arch(num_sides) - math.pi))
    
    while total_error > err_total:
        #while the conditon that total_error is greater than err_total (assigned  error)
        num_sides += 1
        #Increase side count by 1 
            #num_sides += 1 needs to come before no after the total error count
        total_error = (abs(pi_arch(num_sides) - math.pi))
        #Then test the error again
    
    return num_sides, total_error
    #break out of while loop and store num_sides and total_errorr

def wallises(err_total : float):
    #Do the same for wallis and carlos
    num_pairs = 1
            
    total_error = (abs(pi_wallis(num_pairs) - math.pi))
    
    while total_error > err_total:
        num_pairs += 1
        total_error = (abs(pi_wallis(num_pairs) - math.pi))
    
    return num_pairs, total_error

def monte_carlos(err_total : float):
    numDarts = 1
        
    total_error = (abs(montePi(numDarts) - math.pi))
        
    while total_error > err_total:
        numDarts += 1
        total_error = (abs(montePi(numDarts) - math.pi))
        random.seed(42)
 
    return numDarts, total_error
                

def all_pi(err_total : float): 
        
    
        num_method = []
        #make empty array
        arch_sides, arch_err = arches(err_total)
        #store each retuned value from the function individually
        wallis_pairs, wallis_err = wallises(err_total)
        monte_darts, monte_err = monte_carlos(err_total)
        
        num_method.append(arch_sides)
        num_method.append(wallis_pairs)
        num_method.append(monte_darts)
        #Append Items to the empty list and take only the quantity not the error
        
       

        print(f"Archimedes: num_sides = {arch_sides} (Differs by {arch_err})")
        print(f"Wallis: Needs num_pairs = {wallis_pairs} (Differs by {wallis_err})")
        print(f"Monte Carlo: num_pairs = {monte_darts} (Differs by {monte_err})")
        print(num_method)
        #Prints the array 



if __name__ == "__main__":
    (all_pi(0.1))
    #sets our parameters for err_total