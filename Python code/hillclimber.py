###################################
## hillclimber(beginmap, start_value, houses_total, pieces_of_water)
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

def hillclimber(beginmap, start_value, houses_total, pieces_of_water):
	'''
	This function applies a hillclimber algorithm on a provided map.
	'''
	# split beginmap up in houses and water
	houses, water = splitmap(beginmap) 

	# initialise variables
	best_houses = list(houses)
	temporary_map = beginmap
	best_value = start_value
	temporary_value = 0

	# array to hold values of map during optimization
	values = []

	# name to save visualization
	name1 = str(start_value) + "before" 
	
	iteraties = 20
	for k in range(iteraties):

		# loop over houses, and move each house once
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

	# plot line of values hillclimber over mutations
	data = values
	plotline(values, "Hillclimber", "Mutaties")

	# write data to csv
	csv_writer(best_map, pieces_of_water, houses_total, best_value, stime + "hillclimber.csv")

	# plot beginmap and end map
	plotmap(len(beginmap), beginmap, name1, houses_total)
	plotmap(len(beginmap), best_map, name2, houses_total)

"""
Option to get map from file by running hillclimber.py:
Uncomment underneath lines of code and fill in filename of map you'd 
like to improve in code underneath and run via command line
"""
# # read map-variables from csv
# beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("centered_housing.csv")

# # run hillclimber
# hillclimber(beginmap, start_value, houses_total, pieces_of_water)

















