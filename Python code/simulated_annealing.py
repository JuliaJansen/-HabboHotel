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
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("1104_May_23_20bestvalue100000_11341710.0.csv")

# initialise variables
best_houses = list(houses)
temporary_map = beginmap
best_value = start_value
temporary_value = 0

print "best value before", best_value

name1 = str(start_value) + "before" 
nr_of_tests = 50000

# values for simulated annealing, change as you feel fit
temperature = 100000000000
cooldown_rate = 1.0 - float(1.0 / (10000 / 2))
winning = 0

for k in range(nr_of_tests):

	if k % 1000 == 0:
		print 'best value ', best_value

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

		# update our map with the new house if total value of map is higher or because of SA probability
		if temporary_value >= best_value:
			best_value = temporary_value
			best_houses = list(temporary_houses)
		
		# lower value, but still chance to accept change
		else:
			# temperature = 1.0 / float(i + 1)
			temperature = temperature * cooldown_rate
			power = float(((temporary_value - best_value) * 2) * 0.000001) / (temperature)

			# probability to accept deterioration
			prob_accept = math.exp(power)
			check_value = random.randint(0, 1) 

			if prob_accept >= check_value:
				winning += 1
				best_value = temporary_value
				best_houses = list(temporary_houses)

	if winning % 1000 == 0:
		print "k ", k
		print "tussenstand", winning

print "winnning =", winning
print "best value after = ", best_value


name2 = str(best_value) + "after"

best_map = best_houses + water

csv_writer(best_map, pieces_of_water, houses_total, best_value, "simulbest.csv")

# plot maps
plotmap(len(beginmap), beginmap, name1, houses_total)
plotmap(len(beginmap), best_map, name2, houses_total)

















