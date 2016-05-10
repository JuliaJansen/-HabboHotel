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
import copy
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# import other files
from water import * 
from house import *
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
beginmap, houses, water, start_value = csv_reader("planned_map.csv", houses_total, pieces_of_water)

print ("value of first map", start_value)

# initialise variables
best_houses = list(houses)
temporary_houses = list(best_houses)
temporary_map = beginmap
best_value = start_value
temporary_value = 0

name1 = "before" + str(start_value)
nr_of_tests = 20

for i in range(nr_of_tests):

	index = 0

	# set temporary value to 0
	temporary_value = 0

	print "run //////////////////////// :", i

	# loop over each house, and move it once
	for house in best_houses:

		# get specifics of that house
		x_min = house.x_min
		y_min = house.y_min
		type_house = house.type_house
		freespace = house.freespace

		# update x and y
		x_new = house.x_min + (random.randint(-4, 4) * 0.5)
		y_new = house.y_min + (random.randint(-4, 4) * 0.5)

		# print "nieuwe x en y = ", x_new - house.x_min, y_new - house.y_min

		# update temporary map with new house
		temp_house = House(x_new, y_new, type_house)

		# make sure houses don't move of the fiels
		if temp_house.x_min < temp_house.freespace or temp_house.x_max > (160 - temp_house.freespace) or \
			temp_house.y_min < 0 or temp_house.freespace > (150 - temp_house.freespace):
			index += 1
			continue

		# if house will be moved to water, continue to next house
		if distanceWater(temp_house, water) == False:
			index += 1
			continue

		# make sure houses don't overlap
		temp_distance = distance_exclusive(temp_house, best_houses, index)
		if temp_distance > 0:
			temporary_houses[index] = House(temp_house.x_min, temp_house.y_min, temp_house.type_house)
			temporary_houses[index].updateDistance(temp_distance)

		# update variable to track were in the map we are
		index = index + 1

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
		print "nr test:", i, "temporary_value:", temporary_value, "best value:", best_value
		best_houses = list(temporary_houses) 
		best_value = temporary_value

	# print maps
	for j in range(4):
		print "TEMPORARY HOUSES :::: ", temporary_houses[j].x_min, temporary_houses[j].y_min
		print "BEST HOUSES ::::::::: ", best_houses[j].x_min, best_houses[j].y_min
	
# FF CHECKEN
print ("best value = ", best_value)

name2 = "after" + str(best_value)

best_map = best_houses + water

# plotmap(len(beginmap), beginmap, name1, houses_total)
plotmap(len(beginmap), best_map, name2, houses_total)

















