###################################
## Hill Climber Small steps     
## Heuristieken
## Amstelhaege
## Julia, Maarten en Maarten
###################################

import datetime
import csv
# import pylab
import random
import math
import copy
# import matplotlib.pyplot as plt
# from matplotlib.path import Path
# import matplotlib.patches as patches

# # import other files
from valuation import *
# from data_to_csv import * 
from water import * 
from house import *
# from visuals import *
from csv_reader import *
from csv_writer import *

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# get best best from file
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("equal_spacing_map.csv")

# initialise variables
temporary_map = beginmap
best_value = start_value
temporary_value = 0
all_water = water

print "value after = ", best_value


for i in range(len(houses)):
    houses[i].updateDistance(distance(houses[i], houses, i, True))


# valuate new map
best_value = euroValuation(houses, 0)


best_houses = list(houses)

# save date/time to name plot
stime = datetime.datetime.now().strftime("%I%M_%B_%d_")

print "value after = ", best_value

# write value data to csv
name3 = "hill_" + str(stime) + str(houses_total) + "_" + str(best_value) + ".csv"

total_map = best_houses + all_water

# data_to_csv(data, name3)

csv_writer(total_map, pieces_of_water, houses_total, best_value, stime + "equal_spacing_map.csv")




