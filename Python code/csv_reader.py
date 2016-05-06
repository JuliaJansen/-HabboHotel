###########################################
# reads the list of houses and water from #
# a csv file named output.csv, and stores #
# this in the same object-type of list    #
###########################################

import csv
from house import *
from water import *

def csv_reader(filename, houses_total, pieces_of_water):
    """
    Writes the values of a map to csv file named datetime_output.csv
    """
    # open csv file, define fieldnames for houses, instantiate the reader
    csvfile = open(filename, 'r')
    fieldnames = ("one","two","three", "four")
    reader = csv.DictReader(csvfile, fieldnames)

    # lists to contain houses and water
    houses = []
    water = []

    total_items = houses_total + pieces_of_water 

    # read in houses -> water -> value
    count_row = 0
    for row in reader:
        
        if (count_row < houses_total):
            x_min = float(row['one'])
            y_min = float(row['two'])
            type_house = row['three']
            distance = float(row['four'])
            new_house = House(x_min, y_min, type_house)
            print "distance = ", distance
            new_house.updateDistance(distance)
            print "distance hetzelfde? = ", new_house.distance
            houses.append(new_house)
        
        elif (count_row >= houses_total and count_row < total_items):
            x_min = float(row['one'])
            y_min = float(row['two'])
            x_max = float(row['three'])
            y_max = float(row['four'])
            print "xmax y max = ", x_max, y_max
            print "x min y min =", x_min, y_min
            new_water = Water(x_min, y_min, x_max, y_max)
            water.append(new_water)
        
        elif (count_row == total_items):
            map_value = float(row['one'])
        
        count_row += 1

    # return map and map value
    full_map = houses + water
    return (full_map, houses, water, map_value)






