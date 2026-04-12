"""
CS 210 Project 7 - Titanic Bar Charts Extra Credit 
Author:[Sabrina Zhang]

References: Plotting Graphs Side by Side : https://www.geeksforgeeks.org/place-plots-side-by-side-in-matplotlib/#
                Enumerate Code Reference : https://www.geeksforgeeks.org/enumerate-in-python/
             Matlibplot Stacked Bar Chart: https://tinyurl.com/4dx8bmf6

"""

import titanic
import csv 
import statistics as stats
import matplotlib.pyplot as plt
import numpy as np


def load_data(file_name:str, types: dict) -> dict:
    """Loads data"""
    with open(file_name, 'r', encoding = "utf8") as file:
        reader = csv.reader(file) 
        header = next(reader) 
        data = {}
        for items in header: 
            data[(items, types[items])] = [] # This is called initalizing   
        for row in reader: 
            for i, item in enumerate(header):
                stuff = types[header[i]](row[i])
                data[(header[i],types[header[i]])].append(stuff) 

        return data

def survivor_bar(data:dict, col_1:tuple,col_2:tuple)->plt.Figure:
    """Takes the column from the main() function and plots it in a bar chart"""
    
    survival = None
    for items in data: # takes the array of those surivived
        if items[0] == "Survived":
            survival = (data[items])
            break
    # counter for each status by gender
    count_fd = 0  
    count_fa = 0
    count_md = 0
    count_ma = 0
    
    # Filters by gender of survival status
    for i in range(len(survival)): 
        if survival[i] == 0: # if status  is dead
            if data[col_2][i] == "female": # checks the gender
                count_fd += 1
            else:
                count_md += 1 # appends to the count of those dead by gender
                
        else: # else the status  is alive
            if (data[col_2][i]) == "female":
                count_fa += 1 # appends count by gender 
            else: 
                count_ma += 1
    
    # Assigns those who died and alive by gender in a list
    gender_countA = [count_fa, count_ma]
    gender_countD = [count_fd, count_md]
    
    sum_f = count_fa + count_fd
    sum_m = count_ma + count_md
    
    # Calculates the percentage of deaths per gender as a tuple
    gender_perA = [(count_fa/ sum_f) * 100, ( count_ma/ sum_m)* 100]
    gender_perD = [(count_fd/ sum_f)* 100, ( count_md/ sum_m)* 100]
    
    gender = ("Female", "Male") # defines the two categories for the bar chart
    ratio = { # takes the ratio of those alive and dead by gender 
        "alive" : np.array(gender_countA), # must take it as a np.array >>>  ex [31 218]
        "dead": np.array(gender_countD)
    }
    percent = { # takes the percentage of those alive and dead by gender
        "alive" : np.array(gender_perA),
        "dead": np.array(gender_perD)
    }
    
    colors = {"dead" : "red", "alive" : "green"}
    width = 0.5 # sets bin sizes (?)
    bottom = np.zeros(2) # sets where the bins start
    plt.subplot(1,2,1) # row 1, columns 2, count 1 
    # This tells it to make how many graphs in each row 
    
    
                # values in the dict ratio.items()
    for boolean, ratio in ratio.items():
              #Labels, values or %        dead or alive < taken from ratio status  
       plt.bar(gender, ratio, width, label=boolean, bottom = bottom, color = colors[boolean]) # <<< colors is assigned to based on the boolean status
       bottom += ratio # bottom tells you where to start the next data to plot 
       
    plt.title("Count of Deaths per gender")
    plt.ylabel("Count")
    plt.legend(loc = "upper right") # locks the legend to upper right corner
    
    bottom = np.zeros(2) # Need this here to reset the bottom value
    plt.subplot(1,2,2) # row 1, columns 2, count 2
    for boolean, percent in percent.items():
            plt.bar(gender, percent, width, label = boolean, bottom = bottom, color = colors[boolean])
            bottom += percent # updates to where the next bar graph should start bottom from 
    
    
    plt.title("%" " of Deaths per gender")
    plt.legend(loc = "upper right")
    plt.ylabel("Percentage")
    plt.tight_layout() # gives space between the two graphs
    plt.savefig('survival_odds.png')
    plt.show()

def main():
    #Main program driver for Project 3.

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('Titanic-clean.csv', titanic_types)
   
    # 3.4 Visualize results
    fig = survivor_bar(data, ('Age', float), ('Sex', str))



if __name__ == "__main__":
    main()
