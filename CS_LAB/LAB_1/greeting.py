"""
CS 210 Lab 1 - Lab 1 Exercises
Author:[Sabrina Zhang]
Credits:[Acknowledgements - Lab group, perhaps others]
Lab exercises demonstrating how IDLE Editor and Shell Interact
"""

welcome = "hello, Python"
def is_even(n):
    """
    (int) -> Boolean
    Returns True if
    n is even
    >>> is_even(100)
    True 
    >>> is_even(101)
    Falsefrom 
    >>> is_even(0)
    True
    """
    return(n % 2) == 0 
