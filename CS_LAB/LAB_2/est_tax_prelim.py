"""
CS 210 Lab 2
Author:[Sabrina Zhang]
Tax Estimator

"""
# File: est_tax.py

def taxable(income, exemeptions, exempt_amount, deduct_amount):
    """
    Args:
        income: gross income for which the tax is being computed
        exemeptions: the number of personal exemptions
        exemptt_amount: the dollar amount for each exemption
        deduct_amount: the dollar amount for the standard deduction
    
    Returns:
        TODO: Should this function return a value or print the result?
        - Print the function
    >>>>> taxable(43000, 1, 12550, 12550)
    17900    
    """
    
    #TODO: Write the Function Code here
    #Pay Special Attention to the return
    #Return None
    
    TAX_RATE = 0.2
    
    taxable_income = income - deduct_amount
    excempt_adjust = exempt_amount* exemeptions
    taxable_income = taxable_income - excempt_adjust
    
    #print(taxable_income)
    return taxable_income

taxable(43000, 1, 12550, 12550)



def est_tax(income, excemptions):
    """
    computes and prints an estimate for federal income tax.
    It assumes a simple stnadard deduction for $125000
    and a flat tax rate of 20%
    
    Args:
        Income: income for which the tax is being computed 
        Excemptions: Number of exemptions claimed by the taxpayer
        
    Returns: 
        The due tax amound for the given income and the number of exceptions
    
    est_tax(43000, 1)
    print(est_tax)
    """
    
    #Constants for the standard exemption and deduction (USD) 
    STD_DEDUCT = 12550
    STD_EXEMPT = 12550
    
    #Constants for the flat tax rate of 20% 
    TAX_RATE = .20 
    
    #Calculate  federal tax by adjusting reported income 
    # and applying the tax rate
    tax_inc = taxable(income, excemptions, STD_EXEMPT, STD_DEDUCT)
    est_tax = tax_inc * TAX_RATE
    print ("Estimated Tax is:" , est_tax)
    return est_tax

est_tax(43000,1)


    


