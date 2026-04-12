"""
CS 210 Project 6 - Population Data Analysis by Visualization
Author:[Sabrina Zhang]
Resources : Plotting coordinate points 
https://stackoverflow.com/questions/45529337/plotting-latitudes-and-longitudes-in-python

"""

import json 
import matplotlib.pyplot as plt
import matplotlib.image as mapping

def plot_pop_data():
    """Opens the json file and takes the latitude and longitude and plots it on a map"""
    with open("population.json", "r") as file:
        label = file.read()
        stats = json.loads(label)
        latitude = [city["lat"] for city in stats]
        longitude = [city["lng"] for city in stats]
        population = [city["pop2023"] for city in stats]

        i = 0
        #for loop to plot each population value 
        for i in range(len(population)):
            if population[i] < 0: # if the index value is equal to zero, skip that value
                i += 1
            else: # else plot it accordingly
                plt.scatter(longitude[i], latitude[i], s = population[i]/1000, c = 'blue')
                i += 1
            
        plt.show()
    return None

def plot_hist(data, nbins = 5):
    """ Plots data onto histogram
    For optional bin sizes, we can set the bins to a default and another value can be entered
    """
    plt.hist(data)
    plt.title("Density Histogram")
    plt.xlabel("density")
    plt.ylabel("Count")
    
    plt.show()
    return None

if __name__ == "__main__":
    #gives the data to the hisogram to be plotted
    with open("population.json", "r") as file:
            label = file.read()
            stats = json.loads(label)
            data = [city["density"] for city in stats]
    plot_hist(data)
    
        
(plot_pop_data())

