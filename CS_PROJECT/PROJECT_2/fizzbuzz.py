"""
CS 210 Project 2 - Fizzbuzz
Author:[Sabrina Zhang]
FizzBuzz conditionals
"""


def fb(n):
        """
        If n is divisible by 3, return "fizz"
        If it is  divisible by 5, return "buzz"
        If it is divisibleby
        """
        #Conditional based on the remainder of dividing
        if n % 5 == 0 and n % 3 == 0:
            
            #print fizzbuzz if n is divisible by 5 and 3
            print("fizzbuzz")
        
        elif n % 3 == 0:
            #print fizz if n divisible by 3
            print("fizz")
        
        elif n % 5 == 0:
            #print buzz if n divisible by 5
            print("buzz")
        
        else:
            #print n 
            print (int(n))
        return None
        


def fbloop(n):
    #function fbloop takes a parameter in fbloop(n)
    #n is set as a interger when the fuunction is called
   
    for n in range (1, n + 1): 
        #when n is in range between 1 and n + 1 (n + 1 because itstarts at 0)
        fb(n)
        #run the function fb(n) n times 
    
    #exit the loop and print game over
    print("Game Over!")
    
    #return None because theres nothing you need to return 
    return None

#Checks if you are in the main space 
    #If true then run the code
    #if you run the program __name__ will contain __main__
if __name__ == '__main__':
    fbloop(15)