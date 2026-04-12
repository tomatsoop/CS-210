"""
CS 210 Project 6 - Population Data Analysis by Table
from JSON file
Author:[Sabrina Zhang]
References: Python Programming Textbook Chapter 5

"""

import json
import statistics as stat

def read_data(file_name: str, keys : list) -> list:
    '''       
    read_data will read the information from a given file. Currently it is a json file,
    so it will only read json files
    '''
    columns = [] #is the same as: 

    with open(file_name, "r") as file:
        label = file.read()
        stats = json.loads(label)
                  
    columns = [city[key] for key in keys for city in stats]
   
    return columns

def stats(an_array: list) -> dict:
    
    '''calculates the statistics of the given list into a dictionary'''
    
    arr_stats = {    
        'min': min(an_array),
        'max': max(an_array), 
        'range': max(an_array) - min(an_array),
        'mean': round((sum(an_array)/len(an_array)), 2),
        'mode': stat.mode(an_array),
        'var': round(stat.variance(an_array), 1),
        'stdev': round(stat.stdev(an_array),2)
        }
    
    return arr_stats

def print_stats(): #file_name: str
    
    """
    Creates a chart based on the stats for Population of 2023 
    Using data only where Population is above 10,000
    The data on the example table does not filter growth or the density by the 10,000(?)
    """
    
    #creates a empty list to hold the filtered data
    pop_10000 = []
    growth_10000 = []
    density_10000= []
    #reading data based on column selection
    list1 = read_data("population.json", ["pop2023"])
    list2 = read_data("population.json", ["growth"])
    list3 = read_data("population.json", ["density"])
    i = 0 # used to count the index value
    for items in list1:
        if items > 10000: #filters population by 10,000th
            pop_10000.append(items) 
            growth_10000.append(list2[i]) #adds each value based on the index number iteration where this is true
            density_10000.append(list3[i])
            i += 1 #increment the index value
    # run it through the stats function 
    population = (stats(pop_10000))
    growth = (stats(growth_10000))
    density = (stats(density_10000))
    
    print("          "," +------------" * 7 + "+")
         # This assigns spaces within 13 spaces, I want to put a word in there   .format tells the code what string to insert
    print("{:12}|{:13}|{:13}|{:13}|{:13}|{:13}|{:13}|{:12}|".format("", "min", "max", "range", "mean", "mode", "var", "st.dev.")) #refenced textbook
    print("          "," +------------" * 7 + "+")
    print("population  |{min:<13}|{max:<13}|{range:<13}|{mean:<13}|{mode:<13}|{var:<13}|{stdev:<12}|".format(**population))
    print("          "," +------------" * 7 + "+")
    print("population  |{min:<13}|{max:<13}|{range:<13}|{mean:<13}|{mode:<13}|{var:<13}|{stdev:<12}|".format(**growth))
    print("          "," +------------" * 7 + "+")
    print("population  |{min:<13}|{max:<13}|{range:<13}|{mean:<13}|{mode:<13}|{var:<13}|{stdev:<12}|".format(**density))
    print("          "," +------------" * 7 + "+")

print_stats()

    


