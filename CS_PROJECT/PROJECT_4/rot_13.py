"""
CS 210 Project 4 - ROT-13 Cipher
Author:[Sabrina Zhang]
Subsitution Shifting Cipher
"""



def encrypt(msg:str):
    """Encrypts message taken from user_input
    
    Args:
        user_input: (str) takes input from encrypt__message function
        
            Takes string and finds each charater in the alphabet, storing 
            it each time as a index value. 
           
            The index calue is taken and compared if is it within the range 
            of 26 when (index - 13) or (index + 13). 
            
            If index does not go out of range, then ch is appended into (an empty string)
            cipherText += alphabet[index + 13] <<< (plus or minus 13 depending 
            on which if statement it satisfys)
            
    Returns: cipherText
        For each iteration, the cipherText gets a charater(ch) appended 
        with respect to its encoded range.
        cipherText is returned to be called during decryption
    
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    msg = msg.lower()
    cipherText = ""
    for ch in msg:
        index = alphabet.find(ch) #this line of code is from textbook pg 96
        # assigns a index number based on the index value of ch with respect to alphabet
        
        if index == -1:
            cipherText += " "
        # if index is out of range, then charater is a [space]
        
        elif  0 < index + 13 < len(alphabet):
            cipherText+= alphabet[index + 13]
        # if index + 13 is less than len(alphabet) << (26), then go foward on 
        # the alphabet with alphabet[index + 13] and append ch to msg
            
        elif  0 < index + 13 > len(alphabet):
            cipherText += alphabet[index -13]
        # if index + 13 is out of range of len(alphabet) << (26), then go backwards
        # on the alphabet strings with alphabet[index - 13] and append ch to msg
          
        elif index == 13:
            cipherText += alphabet[index - 13]
        # this is the test case that it lands on 'n'
        # because the len(alphabet) = 26 while starting at 0, 
        # there is a exact median number where it fits in both cases that it will
        # append two letters at once
        # if index == 13, then assign index 13 to alphabet[index - 13]
    
    return cipherText
    

def decrypt(msg:str):
    """ Decrypts the message using the returned value of cipherText in 
    encrypt_text

    Args:
        cipherText: (str) Takes the encrypted string

    Returns:
        uncipherText: (str) Runs through decrypt_text
        based on index value relative to + or - 13
        and appending ch to the empty string uncipherText 
        for the length of cipherText
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    uncipherText = ""

    for ch in msg:
        index = alphabet.find(ch)
        # assigns index value to ch with respect to alphabet
       
        if index == -1:
            uncipherText += " "
        # if index is out of range ch == [space]
        
        elif index == 0:
            uncipherText += alphabet[index + 13]
        # solves the case that ch index is 0 then ch = alphabet[index + 13]
            
        elif index - 13 < len(alphabet):
            uncipherText += alphabet[index - 13]
        # if [index - 13] is within range of alphabet
        # then assign [index - 13] and append to uncipherText
            
        elif index + 13 < len(alphabet):
            uncipherText += alphabet[index + 13]
        # if [index + 13] is within range of alphabet
        # then assign [index + 13] and append to uncipherText
    return uncipherText


def encrypt_decrypt():
    
    
    encrypted = encrypt("Two driven jocks help fax my big quiz")
    print(f'The Encrypted Message is: "{encrypted}"')
    
    decrypted = decrypt(encrypted)
    print(f'The Decrypted Message is: ("{decrypted}")')


if __name__ == "__main__":
    encrypt_decrypt()

            