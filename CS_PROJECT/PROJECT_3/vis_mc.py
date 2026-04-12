"""
CS 210 Project 3 - Monte Carlo Visual
Author:[Sabrina Zhang]
Estimating Pi

References : 
        Used Textbook for Code
        Used W3 Schools for random.uniform()
        https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_uniform 

"""

import random
import turtle
import math
random.seed(42)

def monteCarlo_vis(numDarts):
    turtle.speed('fastest')
    win = turtle.Screen()
    t = turtle.Turtle()
    
    win.setworldcoordinates(-2,-2,2,2)
    #sets the window

    t.up()
    t.goto(-1,0)
    t.down()
    t.goto(1,0)
    
    t.up()
    t.goto(0,1)
    t.down()
    t.goto(0,-1)
    #draws the coordinate lines
    
    inCirlce = 0
    t.up()
    
    for i in range (numDarts):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        #Generates random numbers between int -1 and 1 
        #Rather than coding a togo-if-else function 
        #for every coordinate pair 
        #Set parameters to the area and run parameters
        
        distance = math.sqrt(x**2 + y ** 2) 
        
        t.goto(x,y)
        if distance <= 1:
            inCirlce = inCirlce + 1
            #if distance is within 1 make dot blue
            t.color("blue")
        else:
            t.color("red")
            #if distance outside 1 unit make dot red
        t.dot()
        #print dot
      
    pi = inCirlce / numDarts 
    #return pi as the ratio of those who are in he
    
    turtle.done()
    return pi
    #Calculates pi as the ratio of dots in the cirlce vs outside   

numDarts = 500
pi_calc = monteCarlo_vis(numDarts)


if __name__ == "__main__":
    
    print(pi_calc)
    



