'''
CS 210 Lab 5 - Testing and debugging
Author:[Sabrina Zhang]

Testing and debugging

Functions need to be tested and Debugged
'''
import doctest

def ratsBug(weight, rate):
    '''(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)     # normal
    (16.1, 5)
    >>> ratsBug(1, .5)      # edge - just one week
    (1.5, 1)
    '''
    weeks = 0
    total_weight = weight
    # set the starting total_weight to weight
    while total_weight < (1.5 * weight): 
        # the updated weight through each loop 
        # has to be compared to 1.5 * weight each time
        total_weight += total_weight * rate
        # accumulate the total weight += total_weight * rate
        weeks = weeks + 1
        # increase week counter each time 
        # also changed to the correct calling variable
    total_weight = round(total_weight, 1) 
    # update total_weight through each while loop
   
    return (total_weight, weeks)


def countSeqBug(astr):
    # no fix needed??
    '''(str) -> int

    Returns the length of the longest recurring
    sequence in astr

    >>> countSeqBug('abccde')  # normal  	
    2
    >>> countSeqBug('')        # edge - empty string
    0
    '''
    if len(astr) != 0:
        prev_item = astr[0]
        dup_ct = 1
        high_ct = 1
    else:
        high_ct = 0
        dup_ct = 0
        
    for i in range(1, len(astr)):
        if astr[i] == prev_item:
            dup_ct += 1
        else:
            prev_item = astr[i]
			
            if dup_ct > high_ct:
                high_ct = dup_ct
            dup_ct = 1

    return high_ct




def my_averageBug(dataset):
    '''(str) -> float

    Returns average of values in input string values,
    but zeros do not count at all.  Return 0 if there
    is no real data.
    
    >>> my_averageBug('23')    #normal, no zeros
    2.5
    >>> my_averageBug('203')   #normal, a zero
    2.5
    >>> my_averageBug('0000')  #all zeros
    0
    >>> my_averageBug('1')     #single item string
    1.0
    >>> my_averageBug('05050505')  
    5.0
    '''
    count = 0
    total = 0
    
    for value in dataset:
        if value != '0':
            total += int(value)        
# use int to change string to integer
            count += 1
            # count needs to be incremented in the for loop
    if count == 0:
        return 0
    # set the conditional that if count = 0 
    # then there are no int values in the data set
    # eliminating the division by 0 error
    avg = total /count
    # calculate  the average by dividing total by count
    
    return avg

print(doctest.testmod())










