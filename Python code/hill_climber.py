###################################
## Hill Climber					 ##
###################################

import datetime
import csv
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
from csv_reader import *

# read in the best list (from csv_reader.py and calculate its value?)
the_best = fill
best_value = map_value

temporary_list = the_best
temporary_value = 0

biggest_free_space = 6
tracker = 0

# loop over each house, and move it once
for some_house in the_best:

	# get specifics of that house
	x_min = some_house.getX_min()
	y_min = some_house.getY_min
	type_house = some_house.get_type_house()
	free_space = some_house.getFreeSpace(type_house)
	smallest_distance = distance(some_house, the_best)

	# move position by random number (need to update these ranges, only lower limit rn)
	x_new = random.randrange(0, 2 * (smallest_distance - biggest_free_space)) * 0.5
	y_new = random.randrange(0, 2 * (smallest_distance - biggest_free_space)) * 0.5

	# update temporary list with new house
	some_house = House(x_new, y_new, type_house)
	temporary_list[tracker] = some_house

	# check how much value this new position generates  
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
		temporary_value += value

	# update our list with the new house if total value of map is higher
	if (temporary_value > best_value):
		the_best = temporary_list
		best_value = temporary_value

	# update variable to track were in the list we are
	tracker += 1


















