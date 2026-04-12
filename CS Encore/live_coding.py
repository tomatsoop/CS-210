#write a function that takes a stirng and reverses ita function that takes a string and returns the number  of values in it 
 def reverse_string(s):
     length = len(s)
     new_string = ""
     for i in range (length):
         
         new_string += s[-i-1]
    
         
    
         