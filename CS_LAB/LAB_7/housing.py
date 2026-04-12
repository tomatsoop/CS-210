"""

CS 210 LAB 7 - City Scores and Columns
Author:[Sabrina Zhang]
 
"""

import matplotlib.pyplot as plt
import csv

file ="city-scores.csv"
def read_data(file_name) -> dict:
    """Takes the csv file and creates a dictionary with (city, country)as the keys
    The values are a dictionary of the catergory scores as the keys along with the scores as the values
    Dictionary: 
    {(city, country): (housing: #### .... etc )}"""
    
    with open(file_name, 'r', newline = '') as file:
        reader = csv.reader(file) 
        header = next(reader) 
    
        new_dict = {(row[0], row[1]): 
            # This assigns a tuple containing the city and the country
            ({header[i]:row[i] for i in range(3, len(header))} )for row in reader}
        # for each row in reader, and for i in range of the length of the row (minus the two header indices)\
            # assign the items to the tuple (row[0], row[1])
            # this will store the items for each city as a dictionary
            # where teh key values are the city and the couuntry     
    return new_dict
(read_data(file))


def create_total_score(data_dict):
    """ Adds the sum of all scores from each city """
        
    for city in data_dict: # city is the key ex  ('Yerevan', 'Armenia')
        
        data = [float(num) for num in list(data_dict[city].values())]
        #take data_dict[city].values() into a list so it can be iterated into floats
        
        (data_dict[city]["total_score"]) = sum(data)
        # assigns the value of data to the total housing score for each city
        
    return data_dict #returns the updated dictionary 
    

def plot_data(data_dict):
    """Creates a scatter plot of the given data"""
                    
    housing = [data_dict[city]["Housing"] for city in data_dict for items in city]
    #collects a list of the housing scores
    
    cost_of_living = [data_dict[city]["Cost_of_Living"] for city in data_dict for items in city]
    # collects a list of cost of living scores
    
    housing_num = [float(num) for num in housing]
    #changes the items in housing into a float
    
    cost_of_living_num = [float(num) for num in cost_of_living]
    # type casts the items in cost of living to a float 
    
    #creaates a scatter plot 
    plt.scatter(housing_num, cost_of_living_num, s = 2)
    
    #labels x y axis
    plt.xlabel("Housing")
    plt.ylabel("Cost_of_Living")
    plt.show()
    return None


if __name__ == "__main__":
    # the main conditional execution
    print(create_total_score(read_data(file)))
    plot_data(create_total_score(read_data(file)))