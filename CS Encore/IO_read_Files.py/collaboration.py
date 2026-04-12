import statistics as stats
"""
Most common word: Word that appears most. Write a python program that takes a .txt file
and returns the word that is most used in that file
"""

def most_common_word(filename:str)->str:
    dict = {}

    with open(filename, 'r') as file:
        file_contents = file.read()
        text = file_contents.split()
        for words in text:
            if words not in dict:
                dict[words] = 1 # this updates the keys    
                          # use = to assign the word a new key    
            else: 
                dict[words] += 1
                # uodate the ditionarry value by 1 to increase frequcny 
           
            
        max_count = 0 # value = freq
          # keys are the actual word
        max_word = ""
        for keys in dict.keys():
           
            if dict[keys]> max_count:
                max_count = dict[keys]
                max_word = keys
        
        return max_word, max_count
        
        #update dict here
    #Go through dict and find the most common word

print(most_common_word("CS Encore/IO_read_Files.py/read_file.txt"))

"""
Return averages: Take a dictionary where the keys are student names and the values are 
lists of test scores. Use the statistics.mean() function to calculate and return a dict 
where the keys are student names and the values are the students average test score.
"""
test_scores = {"a" : [65, 75, 23, 90],
        "b" : [85, 75, 53, 91],
        "c" : [65, 85, 63, 20]}
def return_averages(test_scores:dict)->dict:
    diction = {}
    #key is the student name 
    # value = test scores  == dict[keys]
    # dont name dictionaries dict
    
    for keys in test_scores.keys():
        grades = stats.mean(test_scores[keys])
                            #^^^^^^^^ need to perform mean on the original dictionary
        diction[keys] = grades # this updates the value for each keys 
         #^^^^ this updates the test grades into a new dictionary 
    return diction

print(return_averages(test_scores))


"""
Animals in barn: Takes in a list where the elements are the names of farm animals. Returns 
that string that appears most in the list
"""

def animals_in_barn(barn:list)->str:
    farm = {}
    # current animal in barn = animals
    #keys = animal names in barn
    # values = frewucny of animal 
    max_count = 0
    max_animal = "" 
    for animals in barn:
        if animals not in farm.keys(): #
            farm[animals] = 1
        else: 
            farm[animals] += 1
    
    for animals in farm.keys(): #takes the name of the animals 
        if farm[animals] > max_count:
            max_name = animals
            max_count = farm[animals]
        return max_name
    
print(animals_in_barn(["cow", "chicken", "cow"]))
    


"""
Number of words: Takes in a txt file and return the number of words in that file
"""

def number_of_words(filename:str)->int:
    return


"""
Smallest Each: From a list of (name, value) pairs, select the pairs with the smallest
value for each name.
"""

def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    From a list of (name, value) pairs, select the pairs with the smallest
    value for each name. >>> smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)])
    [('apple', 7), ('orange', 12)]
    """
    

"""
What's their ranking: Function takes in a fighter's name and returns their ranking. 
For example: if I input the name Sean O'Malley into the function the function will return
13.
"""

def what_ranking(fighter_name:str,ranking_file:str):
    return

