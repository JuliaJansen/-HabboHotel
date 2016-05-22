###########################################
# reads the list of houses and water from #
# a csv file named output.csv, and stores #
# this in the same object-type of list    #
###########################################

import csv
from house import *
# from water import *

def csv_reader(filename):
    """
    Writes the values of a map to csv file named datetime_output.csv
    """
    # open csv file, define fieldnames for houses, instantiate the reader
    csvfile = open(filename, 'r')
    fieldnames = ('one','two','three', 'four')
    reader = csv.DictReader(csvfile, fieldnames)

    # lists to contain houses and water
    houses = []
    water = []
    map_value = 0
    houses_total = 0
    pieces_of_water = 0

    number_of_rows = len(list(csv.reader(open(filename))))

    # get number of houses and pieces of water
    if number_of_rows < 30:
        houses_total = 20
        pieces_of_water = number_of_rows - houses_total - 1
    elif number_of_rows < 50:
        houses_total = 40
        pieces_of_water = number_of_rows - houses_total - 1
    else:
        houses_total = 60
        pieces_of_water = number_of_rows - houses_total - 1

    # total amount of objects on the map
    total_items = pieces_of_water + houses_total

    # finally, read in houses -> water -> value
    count_row = 0
    for row in reader:

        # turn houses into house objects
        if count_row < houses_total:
            x_min = float(row['one'])
            y_min = float(row['two'])
            type_house = row['three']
            distance = float(row['four'])
            new_house = House(x_min, y_min, type_house)
            new_house.updateDistance(distance)
            houses.append(new_house)
        
        # turn water into water objects
        elif count_row >= houses_total and count_row < total_items:
            x_min = float(row['one'])
            y_min = float(row['two'])
            x_max = float(row['three'])
            y_max = float(row['four'])
            new_water = Water(x_min, y_min, x_max, y_max)
            water.append(new_water)
        
        # read value of map
        elif count_row == total_items:
            map_value = float(row['one'])

        count_row += 1

    # # return map and map value
    full_map = houses + water
    return (full_map, houses, water, map_value, houses_total, pieces_of_water)






