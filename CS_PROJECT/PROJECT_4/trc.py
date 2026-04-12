"""
CS 210 Project 4 - Three Rail Cipher
Author:[Sabrina Zhang]
Transpositon Cipher

"""
def  encrypt(msg:str):
    """
    Divides the charater in strings depending on the 
    index value and its divisibility by 3
    
    """
    charSet_one = ""
    charSet_two = ""
    charSet_three = ""
    counter = 0
   
    for ch in msg:
        if counter % 3 == 1:
            charSet_two += ch
            
        elif counter % 3 == 2:
            charSet_three  += ch
    
        elif counter % 3 == 0:
            charSet_one += ch
          
        counter += 1
      
    msg = charSet_one + charSet_two + charSet_three
    
    return msg



def decrypt(msg:str): 
    """
    Takes the encrypted message and adds to empty charatere list
    depending on how divisible the encrypt(msg) is, sorted through conditionals
    
    """
    charSet_one = ""
    charSet_two = ""
    charSet_three = ""
    rail_length = (len(msg))
    third_rail = rail_length//3
    
    plainText = ""
    
   # Case One where rail_length is divisible by 3
    if rail_length % 3 == 0: #case 1 where thirdLength is divisble by 3
        charSet_one += msg[:third_rail] # colon in front gives the first third
        charSet_two += msg[third_rail: 2 * third_rail]
        charSet_three += msg[2 * third_rail:] # value of the number of indexes up til here 
    
        
                                               # and slice it to the  end 
    # Case two where  rail_length divided by 3 has remainder 1
    elif rail_length % 3 == 1: #case 2 where thirdLength is divisble by 3 remainder 1
        charSet_one += msg[:third_rail + 1] # colon in front gives the first third
        charSet_two += msg[len(charSet_one): len(charSet_one) + third_rail]
        charSet_three += msg[len(charSet_one + charSet_two):] # value of the number of indexes up til here 
    
        
    else: #case 3 where thirdLength is divisble by 3 remainder 2 
        charSet_one += msg[:third_rail + 1] # colon in front gives the first third
        charSet_two += msg[len(charSet_one): len(charSet_one) + third_rail+ 1]
        charSet_three += msg[len(charSet_one + charSet_two):] # value of the number of indexes up til here 
        
            
    for i in range (third_rail):
        #add the strings back together
        plainText = plainText + charSet_one[i]
        plainText = plainText + charSet_two[i]
        plainText = plainText + charSet_three[i]
        
    # if the charSet_one has more charaters than charSet_three (remainder 1)
    # add the last index value to plainText
    if len(charSet_one) > len(charSet_three):
        plainText = plainText + charSet_one[-1]
    
    # if the charSet_two has more charaters than charSet_three
    # add the last index value to plainText
    # we know that if this runs then the charSet_one conditional
    # statement already happened
    if len(charSet_two) > len(charSet_three):
        plainText = plainText + charSet_two[-1]
        # this one will check if charSet_two[-1]
        # we dont need a and statment because
        # if charSet_two happened, charSet_one[-1] happenedd already 
    return plainText
    
      
def encrypt_decrypt():
    #encrypted = encrypt("There is no reason anyone would want a computer")
    encrypted = encrypt("Ahoy, there!")
    print(f'Encrypted = encrypt ("{encrypted}")')
    
    decrypted = decrypt(encrypted)
    print(f'Original = decrypted ("{decrypted}")')
    
    
if __name__ == "__main__":
    encrypt_decrypt()