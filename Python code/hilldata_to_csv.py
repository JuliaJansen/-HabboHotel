# Heuristieken
# Julia, Maarten en Maarten
# Amstelhaege
#

import csv

def hilldata_to_csv(data, name):
    """
    Writes the data values of creating random maps to csv file
    Data: nr of houses, nr of waters, runs, highest value, 
    value of beginmap
    """
    # main nested list 
    MAIN = []

    # for datum in data:
    # 	print datum

  # write MAIN to csv file
    with open(name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)   
        writer.writerow(['Houses', 'Waters', 'Runs', 'Highest Value', 'Begin Value'])
        writer.writerow(data)


