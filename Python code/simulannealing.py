###################################
# Simulated Annealing	
# simulannealing(beginmap, start_value, houses_total, pieces_of_water, type_val)
# Heuristieken
# Amstelhaege
# Julia, Maarten en Maarten
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
from valuation import *
from water import * 
from house import *
from visuals import *
from csv_reader import *
from csv_writer import *

def simulannealing(beginmap, start_value, houses_total, pieces_of_water, type_val):
	'''
	This function applies a hillclimber algorithm on a provided map.
	'''
	# split map up in houses and water
	houses, water = splitmap(beginmap) 

	# initialise variables
	best_houses = list(houses)
	temporary_map = list(beginmap)
	best_value = start_value
	temporary_value = 0
	prob_accept = 0
	power = 0

	# array to hold values of map during optimization
	values = []

	# name to save image of first map
	name1 = str(start_value) + "before" 

	iteraties = 10

	# values for simulated annealing, change as you feel fit
	temperature = 100000
	cooldown_rate = 1.0 - float(1.0 / 100000)
	winning = 0

	for k in range(iteraties):

		# max difference to accept 
		maxdif = 5000 * (0.99999 ** k) 
		
		# loop over each house, and move it once
		for index, house in enumerate(best_houses):

			# set temporary value to 0
			temporary_value = 0

			# copy best_houses
			temporary_houses = list(best_houses)

			# replace house in temporary array
			temporary_houses = list(changeHouse(temporary_houses, house, index, water)) 

			# valuate new map
			if type_val == "euro":
				temporary_value = euroValuation(temporary_houses, temporary_value)
			elif type_val == "space":
				temporary_value = spaceValuation(temporary_houses, temporary_value)

			# temperatuur update
			temperature = temperature * cooldown_rate

			# update our map with the new house if total value of map is higher or because of SA probability
			if temporary_value >= best_value:
				best_value = temporary_value
				best_houses = list(temporary_houses)

			# lower value, but still chance to accept change
			elif (best_value - temporary_value) > maxdif:
				
				# probability to accept deterioration
				power = float(((temporary_value - best_value) * 0.00001) / temperature) 
				prob_accept = math.exp(power)
				check_value = random.uniform(0, 1)
				
				# check prob_accept against random value between 0 and 1
				if prob_accept >= check_value:
					winning += 1
					best_value = temporary_value
					best_houses = list(temporary_houses)

		# keep track of all values of map
		values.append(best_value)

	name2 = str(best_value) + "after"

	# make map
	best_map = best_houses + water

	# write last map to csv file
	csv_writer(best_map, pieces_of_water, houses_total, best_value, "simulbest.csv")

	# plot line
	plotline(values, "Simulated Annealing", "Iterations")

	# plot maps
	plotmap(len(beginmap), beginmap, name1, houses_total)
	plotmap(len(beginmap), best_map, name2, houses_total)

"""
Give option to get map from file by running simulated annealing on it.
Uncomment underneath lines of code and fill in filename of map you'd 
like to improve in code underneath and run via command line
"""
# read map-variables from csv
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("../csv_data/1155_May_24_nr1155_May_24_20bestvalue100000_11611890.0.csv.csv")

# run hillclimber
simulannealing(beginmap, start_value, houses_total, pieces_of_water, "euro")





