"""
CS 210 Project 2 - Netpay
Author:[Sabrina Zhang]
Netpay Functions Exercise
"""

def tax(gross_pay):
    #the function taxes depend on the input (parameter) for gross pay
    
    tax_amount = 0.15
    #The set tax amount is at 15%
    
    taxed = gross_pay * tax_amount
    #Calculate tax by gross_pay times 15% in taxes
    
    return taxed
    # ^ Store the value in function tax(gross_pay) to be called later
    
    
def netpay(hours_worked):
    #The function net pay is dependent on the input (parameter) for hours worked
    
    hourly_rate = 16.25
    #the hourly standard is $16.25 (imagine that)
    
    gross_pay = hours_worked * hourly_rate
    #Calcualte gross_pay by multiplying hours by the hourly rate (gives you how much before taxes)
   
    income = gross_pay - tax(gross_pay)
    #Income after taxes is by taking gross pay minus 
    #whatever was stored in the function tax(gross_pay)

    return income
    # ^ return income is improtannt so it can store that 
    #information into the function netpay(hours_ worked)
    
def main():
    """Net pay program driver"""
    print("For 1 hour of work, net pay is : $" , (round((netpay(1)), 2)))
    #prints based on the input for netpay(n)
    #using the information stored in the function netpay(hours_worked)
    
    print("For 40 hour of work, net pay is : $" , (round((netpay(40)), 2)))
    return None

if __name__ == "__main__":
    main()