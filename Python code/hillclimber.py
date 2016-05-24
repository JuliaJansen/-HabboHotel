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
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("0126_May_22_20bestvalue10000_11471460.0.csv")

# initialise variables
best_houses = list(houses)
temporary_map = beginmap
best_value = start_value
temporary_value = 0

name1 = str(start_value) + "before" 
nr_of_tests = 1000

for k in range(nr_of_tests):

	if k % 100 == 0:
		print k

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

name2 = str(best_value) + "after"

best_map = best_houses + water

csv_writer(best_map, pieces_of_water, houses_total, best_value, "bestbest.csv")

# plot maps
plotmap(len(beginmap), beginmap, name1, houses_total)
plotmap(len(beginmap), best_map, name2, houses_total)
















