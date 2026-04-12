'''
CS 210  Project 9 - Clustering
Author: [Sabrina Zhang]

Function create_clusters was modified for 3.6 extra credit

'''

import random
import math
import csv
import matplotlib.pyplot as plt


def load_numerical_data(filename: str, column_titles: list) -> dict:
    """Load data from a CSV file and return a dictionary with keys being the
    row number and values as tuples of the data in each row, converted to float.

    Args:
        filename: The name of the CSV file to load.
        column_titles: A list of columns to load.

    Returns:
        A dictionary where each element corresponds to a data point, with keys 
        corresponding to the row number and values as a tuple of floats.

    Example:
        If column_titles = ['Col1', 'Col3'], and the CSV file has the following data:
            Col1, Col2, Col3
             2.4,  5.6,  7.8
            10.0, 42.5, -3.2
            31.4,  0.5, 12.3
        Then the return dictionary will be:
            {0: (2.4, 7.8), 1: (10, -3.2), 2: (31.4, 12.3)}
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        label = next(reader)
        data = {}
        column = {items: i for i, items in enumerate(label)}

            
        for i, row in enumerate(reader):
                data[i] = tuple(float(row[column[items]]) 
                                for items in column_titles)
                    
    return data
print(load_numerical_data("earthquakes.csv", ('latitude', 'longitude')))
        

def euclid_dist(point1: tuple, point2: tuple) -> float:
    """Compute the Eucledian distance between two points represented as tuples.
    Listing 7.1 in PPC, with modifications for compliance to PEP8

    Args:
        point1: A tuple representing a point in n-dimensional space.
        point2: A tuple representing a point in n-dimensional space.

    Returns:
        float: The Euclidean distance between the two points.

    Example:
        euclid_dist((1, 2.5), (2.1, 4)) should return 1.86 (approximately).
    """
    total = 0 
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        
        total = total + diff
    
    euclidDistance = math.sqrt(total)
    return euclidDistance
    
print(euclid_dist((1, 2.5), (2.1, 4)))



def create_centroids(k: int, data: dict) -> list:
    """Create k centroids by picking random points from the data until 
    you have k unique centroids.

    Args:
        k: The number of centroids to create.
        data: A dictionary where each element corresponds to a data point, with keys
            corresponding to the row number and values as tuples of floats.

    Returns:
        list: a list of centroids, each centroid is a tuple of floats.
    """
    centroids = []
    centroidCount = 0
    centroidKeys = []
    
    # Checks for repeating centorid values
    while centroidCount < k:
        rKey = random.randint(0, len(data))
        if rKey not in centroidKeys:
            centroids.append(data[rKey])
            centroidKeys.append(rKey)
            centroidCount = centroidCount + 1
    return centroids


def create_clusters(k: int, centroids: list, data: dict) -> tuple:
    """
    Create clusters using the k-means algorithm
    From Listing 7.8, modified to comply with PEP8
    Args:
        k: how many clusters to create
        centroids: the list of centroids, one per cluster
        values: list of tuples
        repeats: how many iterations to run

    Returns:
        list, list: two lists are returned -- one is a list of clusters and the 
            second one is the list of centroids
    """
    old_centroids = [] 
    new_centroid = None 
    
    # Checks for repeating centroid conditional 
    while old_centroids != new_centroid: # Code was modified here
        old_centroids = new_centroid 
        clusters = []  # create list of k empty lists
        for i in range(k):
            clusters.append([])

        for dataIndex in range(len(data)):  # calculate distance to centroid
            distances = []
            for clusterIndex in range(k):
                dtoC = euclid_dist(data[dataIndex], centroids[clusterIndex])
                distances.append(dtoC)
                
            minDist = min(distances)  # Find minimum distance
            closestCluster = distances.index(minDist)  # Find index of the min distance
            clusters[closestCluster].append(dataIndex)  # Add to cluster
        
        dimensions = len(data[0])  # Recompute the clusters
        
        for clusterIndex in range(k):
            sums = [0] * dimensions  # Initializes sum for each dimension
            for dataIndex in clusters[clusterIndex]:
                dataPoints = data[dataIndex]
                for ind in range(len(dataPoints)):  # Calculate sums
                    sums[ind] = sums[ind] + dataPoints[ind]
            clusterLen = len(clusters[clusterIndex])
            
            if clusterLen != 0:  # Do not divide by 0
                for ind in range(len(sums)):  # calculate average
                    sums[ind] = sums[ind] / clusterLen
        
            centroids[clusterIndex] = sums  # assign avg to centroid
        new_centroid = centroids # Updates the new centroid
        
        for c in range(k):  # Prints the clusters
            print("CLUSTER #" + str(c + 1))
            for dataIndex in clusters[c]:
                print(data[dataIndex], end=" ")
            print()
        

    return clusters, centroids


def visualize_clusters(dataset_name: str, titles: list, 
                       clusters: list, centroids: list) -> plt.Figure:
    """OPTIONAL - Extra credit (up to 50xp)
    Visualize the clusters and centroids. Use a different color for each cluster. 
    Args: 
        dataset_name: The name of the dataset
        titles: list of string column titles
        clusters: list of lists of tuples
        centroids: list of tuples
    Returns:
        matplotlib.pyplot.Figure: The figure object
    """
    
    cluster_index = {}
    data = (load_numerical_data(dataset_name + ".csv", titles))f
    
    # Accesses data values using cluster index numbers
    for i, list in enumerate(clusters):
        cluster_index[i] = {data[items] for items in list}
    
    # Creates color keys based on cluster index
    colors = {0: "r", 1:"g", 2:"b", 3:"y", 4: "m"}
    for items in cluster_index.keys():
        for indexes in cluster_index[items]:
           plt.scatter(indexes[0], indexes[1], c = colors[items])
        
    # loops through each list of indexes  in centroids
    for items in centroids:
        plt.scatter(items[0], items[1],  marker = "*", c = "k")
    
    # Plotting
    plt.title(f"{dataset_name}-proj8 clusters k = {len(cluster_index)}")
    plt.xlabel(f"{titles[0]}")
    plt.ylabel(f"{titles[1]}")
    plt.savefig(f"clusters_{dataset_name}_{'_'.join(titles)}.png")
    plt.show()
   

def main():
    """ Main driver for the program."""

    # Specifies the files and columns to analyze in the keys, and the number
    # of clusters in the values.
    datasets = {('earthquakes', ('latitude', 'longitude')): 5,
                ('earthquakes', ('depth', 'mag')): 5,
                ('cs210_scores', ('Projects', 'Exams')): 5}
    # Feel free to add more datasets or column pairs and experiment with different values of k

    # Compute clusters for all datasets
    for (dataset, titles), k in datasets.items():
        print(f'\nDataset: {dataset} {titles}')
        # Part 8.1
        data = load_numerical_data(dataset + '.csv', column_titles=titles)

        # Part 8.3
        centroids = create_centroids(k, data)
        print("Initialized the centroids.")

        # Parts 8.2 and 8.4 (create_clusters calls euclid_dist)
        clusters, centroids = create_clusters(k, centroids, data)
        print("\nCreated the clusters.")

        # Optional extra-credit 8.5
        visualize_clusters(dataset, titles, clusters, centroids)
        print("Visualized the clusters.")

if __name__ == '__main__':
    main()