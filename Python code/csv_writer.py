# Heuristieken
# Julia, Maarten en Maarten
# Amstelhaege
#

import csv
import datetime

def csv_writer(mappie, nr_water, nr_houses, map_value, name):
    """
    Writes the values of a map to csv file named datetime_output.csv
    """
    # main nested list 
    MAIN = []

    # loop over each house object, and its coordinates and type.
    for objects in mappie[:nr_houses]:
        XXX = objects.x_min
        YYY = objects.y_min
        TYPE = objects.type_house
        DISTANCE = objects.distance
        MAIN.append([XXX, YYY, TYPE, DISTANCE])

    # loop over each water object, and its coordinates and type.
    for objects in mappie[nr_houses:]:
        XMIN = objects.x_min
        YMIN = objects.y_min
        XMAX = objects.x_max
        YMAX = objects.y_max
        MAIN.append([XMIN, YMIN, XMAX, YMAX])

    # append the value of this map to the end of the list
    MAIN.append([map_value])
    
    # write MAIN to csv file
    with open(name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)   
        for thing in MAIN:
            writer.writerow(thing)





