"""
CS 210 Lab 4 - Functions and Arugments
Author:[Sabrina Zhang]

How to call functions in a function
As well as taking arugments in a function 
"""
import doctest

type(1)
# <class 'int'>

type("1")
#<class 'str'>

type(1.0)
# <class 'float'>

def hello(first_name):
    '''
    TODO: Write the docstring!
    >>> hello("Olivia")
    Hello, Olivia!
    '''
    print("Hello, " + first_name + "!")
   
    return None

def ciao(first_name):
    '''
    TODO: Write the docstring!
    >>> ciao("Olivia")
    Ciao, Olivia!
    '''
    print("Ciao, " + first_name + "!")
  
    return None

print(type(hello))
#<class 'function'>

print(type(ciao))
#<class 'function'>

hello1= hello

print(hello1("Apple"))
# Hello, Apple!

print(hello1.__name__)
# hello


def greeting (f, s):
    f(s)
    return None
  
print(greeting(hello, "Orange"))
# f(s) evaluates to hello("Orange")
    
def add_3(a, b, c):
    """
    This adds three intergers (a, b, c)
    >>> add_3(1, 2, 3)    
    6
    """
    #the function add_3 takes three arugements
    result = a + b + c 
    return  result

def mult_3(a,  b, c):
    """
    This function multiplies three intergers (a, b, c)
    >>> mult_3(1, 2, 3)
    6
    """
    result = a * b * c
    return  result
    # return stores the infomation of waht to do with the arugments 

def higher_order(f, a, b, c):
      #higher_order calls 4 arugments
    result = f(a, b, c)
    # result tells it that f is a function 

    
    print("Function:", f.__name__)
    # f.__name__ prints the name of the function
    
    print(f"{f.__name__}, {a , b , c} = {result}")
    # this prints the function namme and the parameters
    
    return result
 
if __name__ == "__main__":
    print(doctest.testmod())
    print(higher_order(add_3, 1, 2, 3))
    print(higher_order(mult_3, 1, 2, 3))
    # This calls the function we want to run
    # as well as the parameters we want 
    # the values stored in return will output the result 
    # if you put return None it will print none unless 
    # you specifically call for result in your code
    print(hello)
