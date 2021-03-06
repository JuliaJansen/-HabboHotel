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
from water import * 
from house import *
from visuals import *
start_time = time.time()
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
houses_total = 60
pieces_of_water = 3
nr_tests = 10000
# create a variable to hold number of houses of each type
mais_total = houses_total * 0.15
bung_total = houses_total * 0.25
egw_total = houses_total * 0.60

# loop x times for testing
for k in range(nr_tests):
    if k % 100 == 0:
        print k
    
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
    if pieces_of_water == 1:
        # if whole water surface goes in one piece, make sure to place it somehwere in the left bottom corner
        x_min = random.randint(0, 2 * (bound_x-100)) * 0.5
        y_min = random.randint(0, 2 * (bound_y-100)) * 0.5 
    else:
        # else, place first piece randomly
        x_min = random.randint(0, 2 * (0.8 * bound_x-10)) * 0.5
        y_min = random.randint(0, 2 * (0.8 * bound_y-10)) * 0.5
    new_water = Water(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken, water)
    
    # append first water to list
    water.append(new_water)
    surface_taken = new_water.surface
    piece_of_water += 1
    counter = 0
    while piece_of_water < pieces_of_water:
        # place each piece randomly, padding on right/upper side
        x_min = random.randint(0, 2 * (0.8 * bound_x-10)) * 0.5
        y_min = random.randint(0, 2 * (0.8 * bound_y-10)) * 0.5
        
        # new piece of water
        new_water = Water(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken, water)
        
        # error checking
        if distanceWater(new_water,water) == False:
            counter =+ 1
        if counter % 100 == 0 and counter > 0:
            print "distwater", counter
        
        if distanceWater(new_water, water) == True:
            water.append(new_water)
            surface_taken += new_water.surface
            piece_of_water += 1

    # one house has been already made
    i = 0

    # type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
    type_total = mais_total
    type_house = mais

    # loop over maximal number of houses of this type
    #print "start houses"
    while i < type_total:

        # generate a new random position
        x_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_x - width_maison - 1)) * 0.5
        y_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_y - height_maison - 1)) * 0.5
            
        # get specifics of house we check against 
        new = House(x_min, y_min, type_house)

        # if water doesn't overlap water
        #print "new coordinates are ", new.x_min, new.y_min
        #print "true or not? ", distanceWater(new, water) == True
        #for w in range(len(water)):
        #    print "watercoordinates", water[w].x_min,  water[w].y_min, water[w].x_max, water[w].y_max
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
    
    #print "all houses"

    #for h in houses:
    #    print "house x = ", h.x_min

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
print "highest, lowest, mean", highest, lowest, mean_value

# save date/time to name plot
stime = datetime.datetime.now().strftime("%I%M_%B_%d_")

# names of figures:
# hourminute_month_day_amountofhouses_best/worst_nr.oftests_value.of.map
name1 = stime + str(houses_total) + "bestof" + str(nr_tests) + "_" + str(highest)
name2 = stime + str(houses_total) + "worstof" + str(nr_tests) + "_" + str(lowest)

# plot best and worst map
#print "len fill = ", len(fill)
#plotmap(len(fill), index_high, all_maps, name1, houses_total)
#plotmap(len(fill), index_low, all_maps, name2, houses_total)
print("--- %s seconds ---" % (time.time() - start_time))




