
import json 
import matplotlib.pyplot as plt
import matplotlib.image as mapping


def plot_pop_data():
    
    with open("population.json", "r") as file:
        label = file.read()
        stats = json.loads(label)
        latitude = [city["lat"] for city in stats]
        longitude = [city["lng"] for city in stats]
        population = [city["pop2023"] for city in stats]
        #IMAGE 
        img = mapping.imread("oregon.png")
        ax = plt.axes()
        ax.imshow(img, extent= [min(longitude), max(longitude) , min(latitude), max(latitude)], aspect = "auto")
        i = 0
        for i in range(len(population)):
            if population[i] < 0:
                i += 1
            else: 
                plt.scatter(longitude[i], latitude[i], s = population[i]/1000, c = 'blue', zorder = 2)
                i += 1
        
        
    plt.show()
    return None

        
(plot_pop_data())
