"""
CS 210 Project 3 - Wallis Method
Author:[Sabrina Zhang]
Computing pi
References : 
        Used Textbook for Code
"""
def pi_wallis(num_pairs: int):
    acc = 1
    num = 2
    
    #for aPair is in range of however many is in pairs:
    for aPair in range (num_pairs):
        #calculate left term
        leftTerm = num / (num - 1)
        
        #calculate right term
        rightTerm = num / (num + 1)
        
        #calculate the accumulation 
        acc = acc * leftTerm * rightTerm
        
        num = num + 2
        
    #caluclate pi using the accumation
    pi = acc * 2
    #return and  store the value of pi
    return pi 

#testing 1000 pairs
pairs = 1000

#wallis calls the fuction pi_wallis with a parameter of int stored in pairs
wallis = pi_wallis(pairs)

#print wallis functon after running through the loop in pi wallis 
if __name__ == "__main__":
    print(wallis)