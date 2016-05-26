# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import ConfigParser 
import datetime
import pylab
import gc
import random
import math
import time
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# import other Amstelhaege files
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
valuelist = []
meanvaluelist = []
all_maps_val = []
all_maps_space = []
spacelist = []
meanspacelist = []

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
# houses_total = 60
# pieces_of_water = 3
# nr_tests = 20000

# get values from configuration file to define behaviour
config = ConfigParser.ConfigParser()

with open('amstelhaege.cfg') as cfg_file:
    config.readfp(cfg_file) 

for section in config.sections():
    for option, value in config.items(section):
        if option == 'houses':
            houses_total = int(value)
        if option == 'water':
            pieces_of_water = int(value)
        if option == 'nr_of_tests':
            nr_tests = int(value)
        if option == 'hillclimber':
            hilly = value
        if option == 'sim_annealing':
            simmy = value
        if option == 'data':
            csvdata = value
        if option == 'maps':
            plot_maps = value
        if option == 'histo':
            plot_histos = value

# create a variable to hold number of houses of each type
mais_total = houses_total * 0.15
bung_total = houses_total * 0.25
egw_total = houses_total * 0.60

# loop x times for testing
for k in range(nr_tests):

    # pieces_of_water = random.randint(1, 4)

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

    # save only highest and lowest and mean values every 1000 iterations
    # if k % 1000 == 0:

    #     # find highest map of 1000 maps
    #     highest_value = max(moneyvalues)
    #     valuelist.append(highest_value)
    #     index_high_value = moneyvalues.index(highest_value)
    #     all_maps_val.append(all_maps[index_high_value])

    #     # find map with lowest_value value from 1000 maps
    #     lowest_value = min(moneyvalues)
    #     valuelist.append(lowest_value)
    #     index_low_value = moneyvalues.index(lowest_value)
    #     all_maps_val.append(all_maps[index_low_value])

    #     # calculate mean map value of 1000 
    #     mean_value = sum(moneyvalues) / len(moneyvalues)
    #     meanvaluelist.append(mean_value)

    #     # find map with most overall freespace of 1000 maps
    #     most_freespace = max(distances)
    #     spacelist.append(most_freespace)
    #     index_most_freespace = distances.index(most_freespace)
    #     all_maps_space.append(all_maps[index_most_freespace])

    #     # find map with least overall freespace of 1000 maps
    #     least_freespace = min(distances)
    #     spacelist.append(least_freespace)
    #     index_least_freespace = distances.index(least_freespace)
    #     all_maps_space.append(all_maps[index_least_freespace])

    #     # find mean freespace per map of last 1000 maps
    #     mean_freespace = sum(distances) / len(distances)
    #     meanspacelist.append(mean_freespace)

    #     # empty all lists
    #     moneyvalues = []
    #     all_maps = []
    #     distances = [] 

# use lists with moneyvalues to calculate highest, lowest and mean values
# and find the map with those values
highest_value = max(moneyvalues)
index_high_value = moneyvalues.index(highest_value)
lowest_value = min(moneyvalues)
index_low_value = moneyvalues.index(lowest_value)
mean_value = sum(moneyvalues) / len(moneyvalues)

# use distances list to define most, least and average freespace
# and find the map with those values
most_freespace = max(distances)
index_most_freespace = distances.index(most_freespace)
least_freespace = min(distances)
index_least_freespace = distances.index(least_freespace)
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

name11 = "data_" + str(houses_total) + "_" + str(pieces_of_water) + "_" + stime + ".csv"

# calculate runtime 
runtime = (time.time() - start_time) / nr_tests
print "one test time = ", runtime
print("--- %s seconds ---" % (time.time() - start_time))

if plot_maps == 'Yes':
    # plot best and worst map
    plotmap(len(fill), all_maps[index_high_value], name1, houses_total)
    plotmap(len(fill), all_maps[index_low_value], name2, houses_total)

    # plot maps with most and least value
    plotmap(len(fill), all_maps[index_most_freespace], name3, houses_total)
    plotmap(len(fill), all_maps[index_least_freespace], name4, houses_total)

if csvdata == 'Yes':
    # write best and worst map to csv file
    csv_writer(all_maps[index_high_value], pieces_of_water, houses_total, highest_value, name5)
    csv_writer(all_maps[index_low_value], pieces_of_water, houses_total, lowest_value, name6)
    csv_writer(all_maps[index_most_freespace], pieces_of_water, houses_total, most_freespace, name7)
    csv_writer(all_maps[index_least_freespace], pieces_of_water, houses_total, least_freespace, name8)

    # save data of map generation to csv
    data = houses_total, pieces_of_water, nr_tests, mean_value, highest_value, lowest_value, runtime
    data_to_csv(data, name11)

if plot_histos == 'Yes':
    # plot histograms
    plothisto(len(moneyvalues), moneyvalues, name9, lowest_value, highest_value, mean_value)
    plothisto(len(distances), distances, name10, least_freespace, most_freespace, mean_freespace)

# defined by config file: run hillclimber on best and worst map
if hilly == 'Yes':
    print "jaaaa hilly"

# defined by config file: run simulated annealing on best and worst map
if simmy == 'Yes':
    print "simmmmmmyyy"

print 'Done'