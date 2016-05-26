###################################
## Simulated Annealing	
## Heuristieken
## Amstelhaege
## Julia, Maarten en Maarten
###################################

import datetime
import csv
import pylab
import random
import math
import numpy
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

def simulannealing(beginmap, start_value, houses_total, pieces_of_water):
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


	iteraties = 100000

	# values for simulated annealing, change as you feel fit
	temperature = 100000
	cooldown_rate = 1.0 - float(1.0 / 100000)
	winning = 0

	for k in range(iteraties):

		# max difference to accept 
		maxdif = 3000 * (0.99999 ** k) 

		if k % 1000 == 0:
			print 'best value ', best_value
			print "k ======== ", k
			print "temp ===== ", temperature
			print "maxdif === ", maxdif
			print "power ==== ", power
			print "probaccept = ", prob_accept

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

			# temperatuur update
			temperature = temperature * cooldown_rate

			# update our map with the new house if total value of map is higher or because of SA probability
			if temporary_value >= best_value:
				best_value = temporary_value
				best_houses = list(temporary_houses)

			# lower value, but still chance to accept change
			elif (best_value - temporary_value) > maxdif:
				# print "temp = ", temperature
				# print "coooldown rate ", cooldown_rate 
				power = float(((temporary_value - best_value) * 0.0001) / temperature) 
				# print "power = ", power

				# probability to accept deterioration
				prob_accept = math.exp(power)
				# print "temp = ", temperature
				# print "prob accept=", prob_accept
				check_value = random.uniform(0, 1)
				# print "check value = ", check_value

				if prob_accept >= check_value:
					winning += 1
					best_value = temporary_value
					best_houses = list(temporary_houses)

		values.append(best_value)

	name2 = str(best_value) + "after"



	# make map
	best_map = best_houses + water

	# write last map to csv file
	csv_writer(best_map, pieces_of_water, houses_total, best_value, "simulbest.csv")

	# plot line
	plotline(values, "Simulated Annealing")

	# plot maps
	plotmap(len(beginmap), beginmap, name1, houses_total)
	plotmap(len(beginmap), best_map, name2, houses_total)

"""
Give option to get map from file by running hillclimber.py
Fill in filename of map you'd like to improve in code underneath and run via command line
"""
# read map-variables from csv
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("centered_housing.csv")

# run hillclimber
simulannealing(beginmap, start_value, houses_total, pieces_of_water)





