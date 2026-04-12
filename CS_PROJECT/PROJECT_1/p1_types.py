"""
CS 210 Project 1 - Builtin Types
Author:[Sabrina Zhang]
Learning Properties of Intergers and Floats

"""

a = 10
b = 0.2
c = 0.1




#Subtraction
print ((a + b) - a == b )

#Addition
print ((a + c) + b == (b + c) + a)

#Associative Property (From Mathisnotebook.com)
print (( a * c ) * b == (b * c) * a)

#Distributitve  Property
print ((a * (b + c) == a * b + a * c))

#Division
print((a * b) / c == ((a/c) * b/c))

print ((a + b + c)/c == (a/c + b/c + c/c))