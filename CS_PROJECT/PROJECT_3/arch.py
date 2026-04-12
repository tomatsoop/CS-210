"""
CS 210 Project 3 - Archimedes Method
Author:[Sabrina Zhang]
Computing pi
References : 
        Used Textbook for Code
"""
import math 

def pi_arch(num_sides: int):
   
    innerAngleB = 360.0 /num_sides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = num_sides * sideS 
    pi = polygonCircumference / 2
    return pi


num_sides = 8

archimedes = pi_arch(num_sides)

if __name__ == "__main__":
    print(archimedes)