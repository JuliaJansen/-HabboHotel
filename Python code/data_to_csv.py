# writes data array to csv
# data_to_csv(data, filename)
# Heuristieken
# Julia Jansen, Maarten Brijker en Maarten Hogeweij
# Amstelhaege


import csv

def data_to_csv(data, filename):
    """
    Writes the data values to a csv file
    """
    # main nested list 
    MAIN = []

  # write MAIN to csv file
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)   
        writer.writerow(['Houses', 'Waters', 'Runs', 'Mean', 'Highest Value', 'Lowest Value', 'Runtime/map'])
        writer.writerow(data)


