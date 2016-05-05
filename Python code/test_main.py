# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import datetime
import pylab
import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# import other files
from water import * 
from house import *
from visuals import *

the_best = []
best_value = []

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
pieces_of_water = 2
nr_tests = 2 

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
    
    # maximal values of field
    bound_x = 160
    bound_y = 150

    # place water in grid first
    piece_of_water = 0
    surface_taken = 0
    surface_total = 0.2 * 160 * 150
    
    # initiate first piece of water with random left bottom corner
    x_min = random.randrange(0, 2 * (bound_x)) * 0.5
    y_min = random.randrange(0, 2 * (bound_y)) * 0.5
    new_water = Water(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken)
    
    # append first water to list
    water.append(new_water)
    surface_taken = new_water.surface
    piece_of_water += 1

    while piece_of_water < pieces_of_water:
        x_min = random.randrange(0, 2 * (bound_x - 20)) * 0.5
        y_min = random.randrange(0, 2 * (bound_y - 20)) * 0.5

        # new piece of water
        new_water = Water(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken)

        if distanceWater(new_water, water) == True:
            surface_taken += new_water.surface
            water.append(new_water)
            piece_of_water += 1

    print "placed all waters"
    print "surface taken should be 4800:", surface_taken
    
    # one house has been already made
    i = 0

    # type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
    type_total = mais_total
    type_house = mais

    # loop over maximal number of houses of this type
    while i < type_total:
        ## generate a new random position
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
            else:
                houses.append(new)
                i += 1
    
    # Calculate total value of Amstelhaege
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
    best_value.append(total_value)

    #save houses-array in list 
    fill = houses + water
    all_maps.append(fill)

# find map with highest value from tests
highest = max(best_value)
index_high = best_value.index(highest)

# find map with lowest value from tests
lowest = min(best_value)
index_low = best_value.index(lowest)

# calculate mean map value of tests
mean_value = sum(best_value) / len(best_value)

# save date/time to name plot
time = datetime.datetime.now().strftime("%I%M_%B_%d_")

# names of figures:
# hourminute_month_day_amountofhouses_best/worst_nr.oftests_value.of.map
name1 = time + str(houses_total) + "bestof" + str(nr_tests) + "_" + str(highest)
name2 = time + str(houses_total) + "worstof" + str(nr_tests) + "_" + str(lowest)

# plot best and worst map
plotmap(len(fill), index_high, all_maps, name1, houses_total)
plotmap(len(fill), index_low, all_maps, name2, houses_total)




