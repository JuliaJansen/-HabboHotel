# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import datetime
import pylab
import random
import math
import time

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# import other files
from csv_writer import *
from data_to_csv import *
from water import * 
from house import *
from visuals import *


# global variables
start_time = time.time()
the_best = []
moneyvalues = []
distances = []

# sum all total values
sum_of_total_values = 0

"""
MAIN: Place houses on field
"""
all_maps = []

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# change how you like: houses to place, pieces of water
# to place and amount of tests
houses_total = 20
pieces_of_water = 1
nr_tests = 10000

# create a variable to hold number of houses of each type
mais_total = houses_total * 0.15
bung_total = houses_total * 0.25
egw_total = houses_total * 0.60

# loop x times for testing
for k in range(nr_tests):

    # array of houses per test
    houses = []

    # list to contain waters per test
    water = []

    # first house is a maison
    freespace_maison = 6
    width_maison = 11
    height_maison = 10.5

    # set total value to 0
    total_value = 0
    total_distance = 0

    # maximal values of field
    bound_x = 160
    bound_y = 150

    # place water in grid first
    piece_of_water = 0
    surface_taken = 0
    surface_total = 0.2 * 160 * 150
    
    # initiate first piece of water with random left bottom corner
    if pieces_of_water == 1:
        
        # if whole water surface goes in one piece, make sure to place it somehwere in the left bottom corner
        x_min = random.randint(0, 2 * (bound_x - 100)) * 0.5
        y_min = random.randint(0, 2 * (bound_y - 100)) * 0.5 
    
    # else, place first piece randomly
    else:
        x_min = random.randint(0, 2 * (0.8 * bound_x - 10)) * 0.5
        y_min = random.randint(0, 2 * (0.8 * bound_y - 10)) * 0.5

    # make new Water object and place it
    new_water = NewWater(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken, water)    
    # append first water to list
    water.append(new_water)
    surface_taken = new_water.surface
    piece_of_water += 1

    while piece_of_water < pieces_of_water:

        # find semi random x_min and y_min
        if pieces_of_water < 3:
            x_min = random.randint(0, 2 * (bound_x - 100)) * 0.5
            y_min = random.randint(0, 2 * (bound_y - 100)) * 0.5
        else:
            x_min = random.randint(0, 2 * (0.8 * bound_x - 10)) * 0.5
            y_min = random.randint(0, 2 * (0.8 * bound_y - 10)) * 0.5

        # new piece of water
        new_water = NewWater(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken, water)
    
        if distanceWater(new_water, water) == True:
            water.append(new_water)
            surface_taken += new_water.surface
            piece_of_water += 1

    # start placing houses
    i = 0

    # type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
    type_total = mais_total
    type_house = mais

    # loop over maximal number of houses of this type
    while i < type_total:

        # generate a new random position
        x_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_x - width_maison - 1)) * 0.5
        y_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_y - height_maison - 1)) * 0.5
            
        # get specifics of house we check against 
        new = House(x_min, y_min, type_house)

        # if water doesn't overlap water
        if distanceWater(new, water) == True:

            # if there are any houses to check against
            if len(houses) > 0:

                # if house didn't overlap in any case, add house to list
                smallest_dist = distance(new, houses)
                if smallest_dist > 0:
                    house = new.updateDistance(smallest_dist)
                    houses.append(new)
                    i += 1

                # set type_total to number of next type of houses 
                if i == type_total:
                    if type_house == mais:
                        type_house = bung

                        # start loop of placing houses again
                        i = 0
                        type_total = bung_total

                    elif type_house == bung:
                        type_house = egw
                        type_total = egw_total

                        # start loop of placing houses again
                        i = 0 

            # append first house
            else:
                houses.append(new)
                i += 1

    # update distance of first house
    update = distance_exclusive(houses[0], houses, 0)

    # Calculate total money value of Amstelhaege
    for k in range(len(houses)):
        extraspace = math.floor(houses[k].getDistance() - houses[k].getFreespace())
        
        # value of eengezinswoningen
        if houses[k].type_house == egw:
            value = 285000 * (1 + (0.03 * extraspace))

        # value of bungalows
        elif houses[k].type_house == bung:
            value = 399000 * (1 + (0.04 * extraspace))

        # value of maisons
        elif houses[k].type_house == mais:
            value = 610000 * (1 + (0.06 * extraspace))
        
        # total value is addition of values per loop
        total_value += value
        
    # initiate the best list and update in later sessions
    moneyvalues.append(total_value)

    # Calculate total freespace of Amstelhaege
    for l in range(len(houses)):
        house_distance = houses[l].distance
        total_distance += house_distance

    # append freespace of current map to list with freespace data of all maps
    distances.append(total_distance)

    #save houses-array in list 
    fill = houses + water
    all_maps.append(fill)

# find map with highest_value value from tests
highest_value = max(moneyvalues)
index_high_value = moneyvalues.index(highest_value)

# find map with lowest_value value from tests
lowest_value = min(moneyvalues)
index_low_value = moneyvalues.index(lowest_value)

# calculate mean map value of tests
mean_value = sum(moneyvalues) / len(moneyvalues)

# find map with most overall freespace
most_freespace = max(distances)
index_most_freespace = distances.index(most_freespace)

# find map with least overall freespace
least_freespace = min(distances)
index_least_freespace = distances.index(least_freespace)

# find mean freespace per map of all maps
mean_freespace = sum(distances) / len(distances)

# save date/time to name plot
stime = datetime.datetime.now().strftime("%I%M_%B_%d_")

# names of figures:
# hourminute_month_day_amountofhouses_best/worst_nr.oftests_value.of.map
name1 = stime + str(houses_total) + "bestvalue" + str(nr_tests) + "_" + str(highest_value)
name2 = stime + str(houses_total) + "worstvalue" + str(nr_tests) + "_" + str(lowest_value)
name3 = stime + str(houses_total) + "mostfreespace" + str(nr_tests) + "_" + str(most_freespace)
name4 = stime + str(houses_total) + "leastfreespace" + str(nr_tests) + "_" + str(least_freespace)

name5 = name1 + ".csv"
name6 = name2 + ".csv"
name7 = name3 + ".csv"
name8 = name4 + ".csv"

name9 = stime + str(houses_total) + "_" + str(nr_tests)
name10 = stime + str(houses_total) + "_" + str(nr_tests)

name11 = "data_" + str(houses_total) + str(pieces_of_water) + stime + ".csv"

# calculate runtime
runtime = (time.time() - start_time) / nr_tests
print "one test time = ", runtime
print("--- %s seconds ---" % (time.time() - start_time))

# # plot best and worst map
# plotmap(len(fill), all_maps[index_high_value], name1, houses_total)
# plotmap(len(fill), all_maps[index_low_value], name2, houses_total)

# # plot maps with most and least value
# plotmap(len(fill), all_maps[index_most_freespace], name3, houses_total)
# plotmap(len(fill), all_maps[index_least_freespace], name4, houses_total)

# # write best and worst map to csv file
# csv_writer(all_maps[index_high_value], pieces_of_water, houses_total, highest_value, name5)
# csv_writer(all_maps[index_low_value], pieces_of_water, houses_total, lowest_value, name6)
# csv_writer(all_maps[index_most_freespace], pieces_of_water, houses_total, most_freespace, name7)
# csv_writer(all_maps[index_least_freespace], pieces_of_water, houses_total, least_freespace, name8)

# save data of map generation to csv
data = houses_total, pieces_of_water, nr_tests, mean_value, highest_value, lowest_value, runtime
data_to_csv(data, name11)

# plot histograms
plothisto(len(moneyvalues), moneyvalues, name9, lowest_value, highest_value, mean_value)
plothisto(len(distances), distances, name10, least_freespace, most_freespace, mean_freespace)


