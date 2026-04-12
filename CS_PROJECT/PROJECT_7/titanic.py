"""
CS 210 Project 7 - Titanic Data and Visualization 
Author:[Sabrina Zhang]
References: Pearson Function - Python Programming Textbook Chapter 5
            Eumerate Code -  https://www.geeksforgeeks.org/enumerate-in-python/
"""


import titanic
import csv 
import statistics as stats
import matplotlib.pyplot as plt
#https://www.geeksforgeeks.org/enumerate-in-python/
        

def load_data(file_name:str, types: dict) -> dict:
    """Loads data and changes data type using titanic dictionary in main() """
    with open(file_name, 'r', encoding = "utf8") as file:
        reader = csv.reader(file) 
        header = next(reader) 
        data = {}
        
        for items in header: # for each label in header: create a empty list
            data[(items, types[items])] = [] # This is called initalizing 
        
        for row in reader: #this allows you to iterate through the entire data set rows
            for i, item in enumerate(header): # enumerate assigns a counter for each item
                # this iterates through each item of the header data 
                column = types[header[i]](row[i])
                # type casts the item according to he header index of dict and types(row[i])
                data[(header[i], types[header[i]])].append(column)
                # adds the type to header and appends the list of values in row to header

        return data
        
def summarize(data:dict): 
    """ Prints summary of the data in a formatted method for items in data """
        
    for item in data:
        if item[1] == int or item[1] == float:
            print(f"Statistics for {item[0]}:")
            print("{:>6}:{:>7}".format("min", float(min(data[item]))))
            print("{:>6}:{:>7}".format("max", float(max(data[item]))))
            print("{:>6}:{:>7.1f}".format("mean", float(stats.mean(data[item]))))
            print("{:>6}:{:>7.1f}".format("stdev",float(stats.stdev(data[item]))))
            print("{:>6}:{:>7}".format("mode", float(stats.mode(data[item]))))
            print("__________________________________________")
        elif item[1] == str: # Follows a different format if the column type is a string
            setItem = []
            for stuff in data[item]:
                if stuff not in setItem:
                    setItem.append(stuff)
                
            print(f"Statistics for {item[0]}:")
            
            print(f"Number of unique values: {len(setItem)}")
            print(f"      Most common value: {stats.mode(data[item])}")
            print("___________________________________________")
            
def pearson_corr(x:list, y:list) -> float:
    """ Shows the pearson correlation on a visual (referenced code from textbook)"""
    xBar = stats.mean(x)
    yBar = stats.mean(y)
    xStd = stats.stdev(x)
    yStd = stats.stdev(y)
    num = 0.0
    for i in range(len(x)):
        num = num + (x[i] - xBar) * (y[i] - yBar)
    corr = num / ((len(x) - 1) * xStd * yStd)
    return corr
      
def survivor_vis(data:dict, col_1:tuple,col_2:tuple)->plt.Figure:
    """Visualizes the number of survivors depending on different variables """

    survival = None # initializing data sets
    col_1_alive = []
    col_1_dead = []
    col_2_alive = []
    col_2_dead= []
    for items in data:
        if items[0] == "Survived": #takes the data set for suruvived column
            survival = (data[items])
            break
        
    for i in range(len(survival)): 
        if survival[i] == 0: # if died
            col_1_dead.append(data[col_1][i]) # append the dead for each individal in col_1 and col_2
            col_2_dead.append(data[col_2][i]) 
        else: # if survived 
            col_1_alive.append(data[col_1][i]) # if survived append the survivors for each index in col_1 and col_2
            col_2_alive.append(data[col_2][i])
        
    plt.figure(figsize=(8,4))
    plt.scatter(col_1_alive, col_2_alive, marker='o',c='green',label='Survived') 
    # mark green for survived
    plt.scatter(col_1_dead,col_2_dead,marker='x',c='red',label='Dead') 
    # mark red for dead
    plt.title(f"Survival for {col_1} vs. {col_2[0]}")
    plt.xlabel("Age")
    plt.ylabel(f"{col_2[0]}")
    plt.legend() # makes the legend 
    plt.savefig(f'scatter_{col_1[0]}_{col_2[0]}.png',)

    plt.show(block = False)



# ------ You shouldn't have to modify main --------
def main():
    #Main program driver for Project 3.

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('Titanic-clean.csv', titanic_types)
    print(data)
    print("__________________________")
    # 3.2 Print informative summaries
    print("\nPart 3.2")

    summarize(data)

    print("\nPart 3.3")
    # 3.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 3.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 3.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 3.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()
