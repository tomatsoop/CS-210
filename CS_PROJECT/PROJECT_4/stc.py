"""
CS 210 Project 4 - Simple Transposition Cipher
Author:[Sabrina Zhang] 
Even Odd Cipher
"""

def encrypt(msg:str):
    """Appends ch to list depending on the index value to encrypt """
    evenChars= ""
    oddChars = ""
    charCount = 0 
    
    for ch in msg:
        if charCount % 2 == 0:
            evenChars += ch
    
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    msg = oddChars + evenChars
            
        
    return msg

def decrypt(msg:str):
    """Reorders the charaters from encrypted string"""
    
    halfLength = len(msg) // 2
    evenChars = msg[halfLength:]
    oddChars = msg[:halfLength]
    plainText = ""
    
    for i  in range (halfLength):
        plainText =  plainText + evenChars[i]
        plainText = plainText + oddChars[i]
        
    # adds the  last item of ch incase there is a even(?) number in len(string)
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1] #last even charater
        
    return plainText
 
    
def encrypt_decrypt():
    encrypted = encrypt("It was a dark and stormy night")
    print(f'Encrypted = encrypt("{encrypted}")')
    decrypted = decrypt(encrypted)
    print(f'The decrypted message is: ("{decrypted}")')    
#These two define each variable so we can call  it in the main space
# encrypted will run  through the function after taking information  
# from the user input
# and orignal will take that information from encrypted and run it through decrypt


if __name__ == '__main__':
    encrypt_decrypt()
   