"""
Project 10 solution
Author:
Date:
"""
import doctest

def count_smaller(lst: list, item: int) -> int:
    """ 
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) 
    4
    >>> count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) 
    0
    >>> count_smaller([], 5) 
    0
    """
    # TODO: implement this function
    if not lst:
        return 0
    
    if lst[0] < item:
        return 1 + count_smaller(lst[1:], item)
    else:
        return 0 + count_smaller(lst[1:], item)
    return (1 if lst[0] < item else 0) + count_smaller(lst[1:], item)

#print(count_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))

def is_palindrome(s: str) -> bool:
    """
    Takes a string and returns True only if it is a palindrome
    
    Base Case :
    if not s: # '' has been reached
        return True
        
    Only occurs if the string is infact a palindrome, 
    in that case, the string has reached the end and an empty string occurs. 
    This will return the function True
    
    Recursion: 
    return False if s[-1] != s[0] or is_palindrome(s[1:-1]) == False else True
    
    Will first return False if the first two outer charaters are not equal (s[-1] != s[0])
    If it does equal, then it will loop through is_palindrome(s[1:-1]) until False occurs
    and it will exit the recursion and return False 
    or else return True (where recursion continues till base case is met and returns True
    
    >>> is_palindrome('racecar') 
    True
    >>> is_palindrome('racecars') 
    False
    >>> is_palindrome('racecarssr') 
    False

    """
    if not s:
        return True
    elif s[-1] != s[0] or is_palindrome(s[1:-1]) == False:
        return False
    return True
    return False if s[-1] != s[0] or is_palindrome(s[1:-1]) == False else True


def avg_word_length(lst:list, length:int=0, count:int=0)->float:
    '''
    Base Case: 
    If the list is empty: return length/count
        return the average of the words in the list
    
    Recursion: avg_word_length(lst[1:], len(lst[0]) + length, count + 1)
        return takes the length of the string and stores it as a running total in length
               counts how many words are in the list and iterates 
    
    >>> avg_word_length(['hello', 'world'])
    5.0
    >>> avg_word_length(['hello', 'world', 'meh'])
    4.3
    '''
    if not lst:
        return round(length/count, 1)
    
    return avg_word_length(lst[1:], len(lst[0]) + length, count + 1)

   



def flatten(a_list: list) -> list:
    '''
    Takes in a list and flattens it into a list, removes the nesting list 
    into one list. 
    
    Base case: 
    if not a_list:
        return []
        
    If we have reached the end of the list, stack all the items each recursion back
    into a list
    
    Nested Case:
    If the item in a_list[0] is a list, recursively call the function again
    which htakes the first item in the list and updates the list with +  flatten(a_list[1:])
    
    else:  return [a_list[0]] +  flatten(a_list[1:])
    Just return the first item in the list and +  flatten(a_list[1:])
    
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> flatten([1, [2, 3], 4]) 
    [1, 2, 3, 4]
    >>> flatten([1, [2, [3, 4, [5], 6], 7], 8]) 
    [1, 2, 3, 4, 5, 6, 7, 8]
    
    
    '''
    if not a_list:
        return []
    elif isinstance(a_list[0], list):
        return flatten(a_list[0]) + flatten(a_list[1:])
    else:
        return [a_list[0]] +  flatten(a_list[1:])
    

if __name__ == "__main__":

    print(doctest.testmod())