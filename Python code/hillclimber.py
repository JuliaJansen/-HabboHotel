###################################
## Hill Climber Small steps		
## Heuristieken
## Amstelhaege
## Julia, Maarten en Maarten
###################################

import datetime
import csv
import pylab
import random
import math
import copy
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# import other files
from valuation import *
from data_to_csv import * 
from water import * 
from house import *
from visuals import *
from csv_reader import *
from csv_writer import *

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# get best best from file
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("1255_May_24_60worstvalue20000_22377870.0.csv")

# initialise variables
best_houses = list(houses)
temporary_map = beginmap
best_value = start_value
temporary_value = 0

values = []

name1 = str(start_value) + "before" 
nr_of_tests = 300

for k in range(nr_of_tests):

	# loop over each house, and move it once
	for index, house in enumerate(best_houses):

		# set temporary value to 0
		temporary_value = 0

		# copy best_houses
		temporary_houses = list(best_houses)

		# replace house in temporary array
		temporary_houses = list(changeHouse(temporary_houses, house, index, water)) 

		# valuate new map
		temporary_value = euroValuation(temporary_houses, temporary_value)

		# update our map with the new house if total value of map is higher
		if best_value < temporary_value:
			best_houses = list(temporary_houses)
			best_value = temporary_value

	values.append(best_value)

name2 = str(best_value) + "after"

best_map = best_houses + water

# save date/time to name plot
stime = datetime.datetime.now().strftime("%I%M_%B_%d_")

print "value after = ", best_value

# write value data to csv
data = values
name3 = "hill_" + str(stime) + str(houses_total) + "_" + str(best_value) + ".csv"
data_to_csv(data, name3)

csv_writer(best_map, pieces_of_water, houses_total, best_value, stime + "hillclimber.csv")

# plot maps
plotmap(len(beginmap), beginmap, name1, houses_total)
plotmap(len(beginmap), best_map, name2, houses_total)

















