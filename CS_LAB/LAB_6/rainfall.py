
'''
CS 210 Lab 6 - File I/O 
Author:[Sabrina Zhang

Open and Read files 

'''
import matplotlib.pyplot as plt

def read_data(file_name: str) -> list:
    '''
    Open the cvs file and appends the items to a list
    sorted by each comma
    '''
    
    with open(file_name, 'r') as file:
        avg_rainfall = []
        for aLine in file:
            aLine = aLine.strip("\n") # removes the \n
            avg_rainfall.append(aLine.split(",")) #seperates by comma
            
            
    return avg_rainfall


def list_to_dict(a_list : list) -> dict:
    '''
    Takes a list and formats it into a dictionary
    '''
    dictionary = {}
    
    for item in a_list:
    
        dictionary[int(item[0][:4])] = float(item[1])
        # the [:4] takes the first 4 numbers in the list index as a interger
    return dictionary
        
def dict_to_list(a_dict: dict) -> list:
    '''
    Takes a dictionary an formats it into a list
    '''
    a_list =  []    
    for item in a_dict: 
        year = item # this is the key
        inches = a_dict[item] #This is the value
        a_list.append([year,inches]) # This adds the key and values as pairs into a new list
      
    return a_list
                    
                    
def mean_rainfall(values: list) -> float:
    '''
    Calculates the mean of all the rainfall years
   
    ''' 
    total = 0
    count = 0
    inches = []
    year = []
    
    for data in values:
        total = total + data[1]
        # adds each second item from data index
        count += 1
        #takes count of how many there are
        year.append(data[0])
        inches.append(data[1])
        
    avg = total/count
    #calculates the average
    
    plt.plot(year, inches)
    plt.ylabel("inches")
    plt.xlabel("year")
    
    plt.show()
    
    return avg


def high_rain_years(inches, mean_rainfall):
    '''Takes the years where the rainfall * 1.5 was greater than the mean'''
    percipitation = []
    
    for value in inches:
        if value[1] * 1.5 > mean_rainfall:
            percipitation.append(value)
          
    return percipitation
            
def percentage_increase():
    '''
    Calculates the percentage increase and writes outFile to a txt 
    '''
    data_dict = (list_to_dict(read_data("november_rain.csv")))
    
    mean = (mean_rainfall(dict_to_list(list_to_dict(read_data("november_rain.csv")))))
    
    with open("out.txt", "w") as outFile:
        
        for year in data_dict:
            #print(f"Year : {year}, Average Rainfall in Inches: {data_dict[year]}, Percentage Increase Over Mean: {round(((data_dict[year] - mean)/mean) * 100)}")
            
            outFile.write(f"Year: {year}, Average Rainfall in Inches: { data_dict[year] }, Percentage Increase Over Mean: {round((((data_dict[year] - mean)/mean) * 100), 2)} \n" "for each year in high_rain_years")
    #for each year in high rainfall
    

    


#print(read_data("november_rain.csv"))
#print(list_to_dict(read_data("november_rain.csv")))
#print(dict_to_list(list_to_dict(read_data("november_rain.csv"))))
#print(mean_rainfall(dict_to_list(list_to_dict(read_data("november_rain.csv")))))
#(mean_rainfall(dict_to_list(list_to_dict(read_data("november_rain.csv")))))
#print(high_rain_years((dict_to_list(list_to_dict(read_data("november_rain.csv")))),(mean_rainfall(dict_to_list(list_to_dict(read_data("november_rain.csv")))))))
percentage_increase()


