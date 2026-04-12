#3function that compputes fbilnocii sequence

"""
    starts at 1, 1, 2, 3, 5, 8, 8+5
    eveyr number following is the sum fo the last two 
    
    N = (N - 1) + (n - 2)
    
    fucntion 
    value 1 = 1
    value 2 = 1
    value 3 = 2 
    value 3 = 2 
    
    
    n = (1 - 1) + (1 - 2))
    n = 0 + -1 
    
    sum of the previous two numbers 
    
    
"""

def fib(n):
    a = 0
    b = 1
    for i in range (n + 1):
        print(a, end = " ")
        a, b = b, a + b 
    return None
print(fib(3))