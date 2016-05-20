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
from getStatistics import *
from water import * 
from house import *
from valuation import *
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
nr_tests = 1000

# create a variable to hold number of houses of each type
mais_total = houses_total * 0.15
bung_total = houses_total * 0.25
egw_total = houses_total * 0.60

# loop x times for testing
for k in range(nr_tests):

    # set total value and total distances between houses to 0
    total_value = 0
    total_distance = 0

    # maximal values of field
    bound_x = 160
    bound_y = 150

    # place water in grid first
    piece_of_water = 0
    surface_taken = 0
    surface_total = 0.2 * 160 * 150
    
    # place all pools on the map
    water = placeAllWater(pieces_of_water)

    # place all cribs on the map
    houses = placeHouses(water, houses_total)

    # calculate money value of this Amstelhaege map
    total_value = euroValuation(houses, total_value)
        
    # append value to list with all values of this test
    moneyvalues.append(total_value)

    # calculate total freespace of Amstelhaege
    total_distance = spaceValuation(houses, total_distance)

    # append freespace of current map to list with freespace data of all maps
    distances.append(total_distance)

    # save houses and water lists in one map list  
    fill = houses + water
    all_maps.append(fill)

# get statistics for plotting maps and writing data to csv
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


