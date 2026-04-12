def is_even(n):

    """Determines if n is an even number
    Args: 
      n : an interger number
    Returns: 
        True if n is an even number, False otherwise 3"""

    print("in function is_even")
    return (n % 2) == 0

def welcome():
    """Print a welcome message.
    >>> welcome()
    Good morning, CS 210!
    """
    print('Good morning, CS 210!')
    return None
welcome()