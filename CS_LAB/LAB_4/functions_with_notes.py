"""
CS 210 Lab 4 - Functions and Arugments
Author:[Sabrina Zhang]

How to call functions in a function
As well as taking arugments in a function 
"""

type(1)
# <class 'int'>
#This is a interger

type("1")
#<class 'str'>
#This is a string

type(1.0)
# <class 'float'>
#This is a float

# type(f(a))
# this  is a function that can call a function 
# with a parameter 


#ARGUEMNTS ARE VALUES PASSED TO A FUCTION 



def hello(first_name):
    '''
    TODO: Write the docstring!
    '''
    print("Hello, " + first_name + "!")
    #hello function takes the parameter 'first_name'
    # and returns none for no information stored
    # but when called with parameter first_name
    #prints (hello, first_name!)
    return None


def ciao(first_name):
    '''
    TODO: Write the docstring!
    '''
    print("Ciao, " + first_name + "!")
    #ciao can also do the same thing as func hello
    return None

print(type(hello))
#<class 'function'>

print(type(ciao))
#<class 'function'>

hello1= hello
#t this assigns the function hello to a variable
# hello is stored as hello1 

print(hello1("Apple"))
# Hello, Apple!

#^ That takes the function hello
# and takes an arugment where first_name is now 
# assigned to ("Apple")
# That arugment passes through the hello function
# and prints out Hello, Apple!

print(hello1.__name__)
# hello
# THIS PRINTS THE FUNCTION NAME 
# something here.__name__ prints the name of the function 

def greeting (f, s):
    #This function calls for two parameters
    # f calls a function
    # s calls the string
    # we set f(s) in the def greeting
    # so it defines f as a function and s 
    # will take a sting value 
   
    f(s)
    # ^^^ this calls the two parameters into a function
# f becomes the function hello
#s is the string for olivia

    return None
    #returning none updates the function when you call it

print(greeting(hello, "Orange"))
# Because greeting takes two parameters 
# and we set f to a function that takes 
# the argument of whatever was stored in 
# the function hello (which takes first name as a string)

# f(s) evaluates to hello("Orange")
    
    
def add_3(a, b, c):
    #the function add_3 takes three arugements
    return  a + b + c
    # When you return it, it  stores the 3 arguments and 
    # adds them as the function is supposed to
    # when the function is called the arugments is returned

def mult_3(a,  b, c):
    result = a * b * c
    return  result
    # return stores the infomation of waht to do with the arugments 
    # or you can do this as seen with monte_pi or the  other files

def higher_order(f, a, b, c):
    #highere order calls 4 arugments
    result = f(a, b, c)
    # result tells it that f is a function 
    # that takes 3 parameters
    
    print("Function:", f.__name__)
    # f.__name__ prints the name of the function
    
    print(f"{f.__name__}, {a , b , c} = {result}")
    # this prints the function namme and the parameters
    # and the results
    
    
    return result
    # we want to store the result as a updated information
    # when we call the function and its parameters down here

if __name__ == "__main__":
     
    print(higher_order(add_3, 1, 2, 3))
    print(higher_order(mult_3, 1, 2, 3))
    # This calls the function we want to run
    # as well as the parameters we want 
    # the values stored in return will output the result 
    # if you put return None it will print none unless 
    # you specifically call for result in your code

