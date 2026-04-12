'''
CS 210  Project 5 - Postfix Evaluation
Author: [Sabrina Zhang]
Stack Calculator 
Resources: https://pythonguides.com/check-if-a-string-is-an-integer-or-float-in-python/
'''


import doctest


def is_operand(operand:str):

    '''boolean check to see if operand is a string
    (operand: str) -> float
    boolean check to see if string is a float
    Example:
    >>> is_operand("3")
    True
    
    >>> is_operand("+")
    False
    '''
    try: 
        float(operand)
        return True
    except ValueError:
        return False


def is_operator(operator:str):
    
    '''Boolean check to see if string is a operator symbol among the operators
    is_operator("+") -> string
    >>> is_operator("+")
    True
    >>> is_operator("!")
    False
    '''
    if operator in ["+", "-", "*", "/"]:
        return True
    else: 
        return False
    
    
def apply_operator(op: str, oper_1:float, oper_2: float):
    """ Evalutes 

    Args:
        op (str): evalutes which operator it is 
        oper_1 (float): Takes value of oper_1
        oper_2 (float): Takes value of oper_2

    Returns:
        float: Returns the operation value after it has been applied
        to oper_1 and oper_2 depending on the corresponding operator sign
        
    >>> apply_operator("*", 3, 4)
    12
    
    #>>> apply_operator("/", 4, 2)
    2.0
    """
    # Conditionals checking what type of operator it is 
    # And applying the correct one
    if op == '+':
        operation = oper_1 + oper_2
        return operation
    if op == '-':
        operation = oper_1 - oper_2
        return operation
    if op == '*':
        operation = oper_1 * oper_2
    if op == "/":
        operation = oper_1 / oper_2
        
    return operation

    
def eval_postfix(expr_str:str):
    """
    Computes operation based on operator symbol
    Args:
        op (str): Checks the operator symbol
        oper_1 (float): takes the value of float 1
        oper_2 (float): takes the value of float 2
    Returns:
        float : returns the evaulated values of oper_2 and oper_1 with the operator
    >>> eval_postfix("3 4 + 7 *")
    49.0
    >>> eval_postfix("3 3.5 4 + 7 * /")
    0.05714285714285714
    """
    
 
    operate = expr_str.split()
    # Splits the string
    operands_list = []
    # Empty Stack list 
    for ch in operate:
        if is_operand(ch):
        # Checks each value and sees if its a operand
            operands_list.append(ch)
        # if so append item
        elif is_operator(ch):
            # if we get a operator, pop the last two items in 
            # operand list and apply the operator
            oper_2 = float(operands_list.pop()) 
            # this is the last item of the list that we pop out, so it is assigned as oper_2
            oper_1 = float(operands_list.pop())
            evaluate = apply_operator(ch, oper_1, oper_2)
            # take the operands and run it through the calculating function 
            operands_list.append(evaluate)
            # add it to the new list
    if len(operands_list) > 1:
        (print("error on postfix expression"))
        # if there was already something in there that didn't get calcculated
        # it prints the error 
        return # Return nothing 
    else:
        return operands_list[0]
    # Return the calculated value
  
               

print(doctest.testmod())