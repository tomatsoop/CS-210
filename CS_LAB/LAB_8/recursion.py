import doctest

def get_vowel_count(s: str) -> int:
    """ 
    Returns the number of vowels in string
    base case is an empty string: return a number
    
    recursion: 
        if the charater in the string is a vowel return 1 
        else return 0 
        update the stack with the rest of the list starting after the first vowel
        
    >>> get_vowel_count("hello")
    2
    
    """
    if not s: 
        return 0
    if s[0].lower() in "aeiou": 
        return 1 + get_vowel_count(s[1:])
    return 0 + get_vowel_count(s[1:])

    return (1 if s[0].lower() in "aeiou" else 0) + get_vowel_count(s[1:])


def multiply(a: float, b: int) -> float:
    '''
    multiplies a floating point number A and postive interger B
    b is the multiplier so we add a by the number of times of b 
    base case: 
    if b == 0:
        return the stack
    else: 
    return a + multiply(a, b-1) 
    
    subtract 1 iteration from b and add another a to the current a stack 
    
    >>> multiply(2.5, 3)
    7.5
    
    '''
    if b == 0: 
        return 0
    return a + multiply(a, b-1)


def deep_reverse(a: list) -> list:
    '''
    Reverses the items in a list, checks if its a list in a list 
    
    base case: return a list if list is empty
    
    checks if the item is a list:
        if is list then run deep_reverse(a) again on the list
        else return the [-1] last item of teh index 
    
    >>> deep_reverse([1, 2, 3])
    [3, 2, 1]
    >>> deep_reverse([1, [2, 3], 4])
    [4, [3, 2], 1]
    >>> deep_reverse([1, [2, [3, 4], [5, [6, 7], 8]]])
    [[[8, [7, 6], 5], [4, 3], 2], 1]
    
    '''
    if not a: 
        return a
    elif isinstance(a[-1], list):
        return [deep_reverse(a[-1])] + deep_reverse(a[:-1])
    return  [a[-1]] + deep_reverse(a[:-1])

    
    return [deep_reverse(a[-1]) if isinstance(a[-1], list) else a[-1]] + deep_reverse(a[:-1])

if __name__ == "__main__":

    print(doctest.testmod())