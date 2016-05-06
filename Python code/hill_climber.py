###################################
## Hill Climber				
## Heuristieken
## Amstelhaege
## Julia, Maarten en Maarten
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
from hillclimber_distance import *
from visuals import *
from csv_reader import *

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# fill in as you like :)
houses_total = 20
pieces_of_water = 4

# get best best from file
beginmap, houses, water, start_value = csv_reader("output.csv", houses_total, pieces_of_water)

print "value of first map", start_value

first_map = beginmap
best_houses = houses
temporary_houses = best_houses
temporary_map = beginmap
best_value = start_value
temporary_value = 0

name1 = "before" + str(start_value)
nr_of_tests = 1000

for i in range(nr_of_tests):

	tracker = 0

	if i % 100 == 0:
		print "best value nu = ", best_value
		print "temp value was =", temporary_value

	# set temporary value to 0
	temporary_value = 0

	# loop over each house, and move it once
	for house in best_houses:

		# get specifics of that house
		x_min = house.x_min
		y_min = house.y_min
		type_house = house.type_house
		freespace = house.freespace

		# update x and y
		x_new = house.x_min + random.randrange(-4, 4) * 0.5
		y_new = house.y_min + random.randrange(-4, 4) * 0.5

		# update temporary map with new house
		temp_house = House(x_new, y_new, type_house)

		# make sure houses don't move of the fiels
		if temp_house.x_min < temp_house.freespace or temp_house.x_max > (160 - temp_house.freespace) or \
			temp_house.y_min < 0 or temp_house.freespace > (150 - temp_house.freespace):
			continue

		# if house will be moved to water, continue to next house
		if distanceWater(temp_house, water) == False:
			continue

		# make sure houses don't overlap
		temp_distance = hill_distance(temp_house, best_houses, tracker)
		if temp_distance > 0:
			temporary_houses[tracker] = House(temp_house.x_min, temp_house.y_min, temp_house.type_house)
			temporary_houses[tracker].updateDistance(temp_distance)

		# update variable to track were in the map we are
			tracker += 1

	# check how much value this new map generates  
	for k in range(len(temporary_houses)):
		extraspace = math.floor(temporary_houses[k].distance - temporary_houses[k].freespace)
		
		# value of eengezinswoningen
		if temporary_houses[k].type_house == egw:
			value = 285000 * (1 + (0.03 * extraspace))

		# value of bungalows
		elif temporary_houses[k].type_house == bung:
			value = 399000 * (1 + (0.04 * extraspace))

		# value of maisons
		elif temporary_houses[k].type_house == mais:
			value = 610000 * (1 + (0.06 * extraspace))
		
		# total value is addition of values per loop
		temporary_value += value

	# update our map with the new house if total value of map is higher
	if temporary_value > best_value:
		best_houses = temporary_houses 
		best_value = temporary_value

	if i % 100 == 0:
		mappp = best_houses + water
		name = "tussenstop_" + str(i)
		plotmap(len(first_map), mappp, name, houses_total)

# FF CHECKEN
print "best value = ", best_value

name2 = "after" + str(best_value)

temporary_map = best_houses + water

plotmap(len(first_map), first_map, name1, houses_total)
plotmap(len(first_map), temporary_map, name2, houses_total)

















