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
from water import * 
from house import *
from visuals import *
from csv_reader import *
from csv_writer import *

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# # fill in as you like :)
# houses_total = 40
# pieces_of_water = 2

# get best best from file
beginmap, houses, water, start_value, houses_total, pieces_of_water = csv_reader("centered_housing.csv")

print ("value of first map", start_value)

# initialise variables
best_houses = list(houses)
temporary_map = beginmap
best_value = start_value
temporary_value = 0

name1 = str(start_value) + "before" 
nr_of_tests = 1000

for k in range(nr_of_tests):

	if k % 1000 == 0:
		print k

	# loop over each house, and move it once
	for index, house in enumerate(best_houses):

		# set temporary value to 0
		temporary_value = 0

		# copy best_houses
		temporary_houses = list(best_houses)

		# replace house in temporary array
		temporary_houses = list(changeHouse(temporary_houses, house, index, water)) 

		# # save old house
		# temp_house = house

		# # update temporary map with new house
		# house = House(x_new, y_new, type_house)
		# best_houses[index] = house
		
		# # make sure houses don't move out of the field
		# if house.x_min < house.freespace or house.x_max > (160 - house.freespace) or \
		# 	house.y_min < 0 or house.freespace > (150 - house.freespace):
		# 	best_houses[index] = temp_house
		# 	index += 1
		# 	continue

		# # if house will be moved to water, continue to next house
		# if distanceWater(house, water) == False:
		# 	best_houses[index] = temp_house
		# 	index += 1
		# 	continue

		# # make sure houses don't overlap
		# temp_distance = distance_exclusive(house, best_houses, index)
		# if temp_distance < 0:
		# 	best_houses[index] = temp_house
		# 	index += 1
		# 	continue

		# # check how much value this new map generates  
		# for k in range(len(best_houses)):
		# 	extraspace = math.floor(best_houses[k].distance - best_houses[k].freespace)
			
		# 	# value of eengezinswoningen
		# 	if best_houses[k].type_house == egw:
		# 		value = 285000 * (1 + (0.03 * extraspace))

		# 	# value of bungalows
		# 	elif best_houses[k].type_house == bung:
		# 		value = 399000 * (1 + (0.04 * extraspace))

		# 	# value of maisons
		# 	elif best_houses[k].type_house == mais:
		# 		value = 610000 * (1 + (0.06 * extraspace))
			
		# 	# total value is addition of values per loop
		# 	temporary_value += value

		temporary_value = euroValuation(temporary_houses, temporary_value)

		# update our map with the new house if total value of map is higher
		if best_value < temporary_value:
			best_houses = list(temporary_houses)

	# # print maps
	# for j in range(4):
	# 	print "TEMPORARY HOUSES :::: ", best_houses[j].x_min, best_houses[j].y_min
	# 	print "BEST HOUSES ::::::::: ", best_houses[j].x_min, best_houses[j].y_min
	
# FF CHECKEN
print ("best value = ", best_value)

name2 = str(best_value) + "after"

best_map = best_houses + water

csv_writer(best_map, pieces_of_water, houses_total, best_value, "bestbest.csv")


# plotmap(len(beginmap), beginmap, name1, houses_total)
# plotmap(len(beginmap), best_map, name2, houses_total)

















