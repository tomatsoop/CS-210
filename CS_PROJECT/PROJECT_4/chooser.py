"""
CS 210 Project 4 - Cryptography Chooser
Author:[Sabrina Zhang]
Applying 3 cryptography methods

"""

import rot_13
import stc
import trc

   
def crypt(string,func):
    """Function to call function and a string"""
    return func(string)


msg = ("Ahoy, there!")



encrypted_stc = crypt(msg, stc.encrypt)
decrypted_stc= crypt(encrypted_stc, stc.decrypt)

print("stc:")
print(encrypted_stc)
print(decrypted_stc)
print("-----------")


encrypted_trc = crypt(msg, trc.encrypt)
decrypted_trc = crypt(encrypted_trc, trc.decrypt)

print("trc:")
print(encrypted_trc)
print(decrypted_trc)
print("-----------")

encrypted_rot_13 = crypt(msg, rot_13.encrypt)

decrypted_rot_13= crypt(encrypted_rot_13, rot_13.decrypt)

print("rot_13:")
print(encrypted_rot_13)
print(decrypted_rot_13)
print("-----------")