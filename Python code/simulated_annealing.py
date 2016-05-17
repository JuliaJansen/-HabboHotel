###################################
## Simulated annealing - houses		
## Heuristieken
## Amstelhaege
## Julia, Maarten en Maarten
###################################

import datetime
import csv
# import pylab
import random
import math
import copy
# import matplotlib.pyplot as plt
# from matplotlib.path import Path
# import matplotlib.patches as patches

# import other files
from water import * 
from house import *
# from visuals import *
from csv_reader import *

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# fill in as you like :)
houses_total = 20
pieces_of_water = 4

# get best best from file
beginmap, houses, water, start_value = csv_reader("centered_housing.csv", houses_total, pieces_of_water)
print ("value of first map", start_value)

# initialise variables
best_houses = list(houses)
temporary_houses = list(best_houses)
temporary_map = beginmap
best_value = start_value
temporary_value = 0

name1 = str(start_value) + "before" 
nr_of_tests = 10000

# values for simulated annealing, change as you feel fit
temperature = 100000000000
cooldown_rate = 0.999
winning = 0

for i in range(nr_of_tests):

	index = 0

	# loop over each house, and move it once
	for house in best_houses:

		# prob for this house for simulated annealing
		# prob_house = random.uniform(0, temperature)

		# set temporary value to 0
		temporary_value = 0

		# get specifics of that house
		x_min = house.x_min
		y_min = house.y_min
		type_house = house.type_house
		freespace = house.freespace

		# update x and y
		x_new = house.x_min + (random.randint(-4, 4) * 0.5)
		y_new = house.y_min + (random.randint(-4, 4) * 0.5)

		# print "nieuwe x en y = ", x_new - house.x_min, y_new - house.y_min

		# remember old house
		temp_house = house

		# update temporary map with new house
		house = House(x_new, y_new, type_house)
		best_houses[index] = house
		
		# make sure houses don't move out of the field
		if house.x_min < house.freespace or house.x_max > (160 - house.freespace) or house.y_min < 0 or house.freespace > (150 - house.freespace):
			best_houses[index] = temp_house
			index += 1
			continue

		# if house will be moved to water, continue to next house
		if distanceWater(house, water) == False:
			best_houses[index] = temp_house
			index += 1
			continue

		# make sure houses don't overlap
		temp_distance = distance_exclusive(house, best_houses, index)
		if temp_distance < 0:
			best_houses[index] = temp_house
			index += 1
			continue

		# check how much value this new map generates  
		for k in range(len(best_houses)):
			extraspace = math.floor(best_houses[k].distance - best_houses[k].freespace)
			
			# value of eengezinswoningen
			if best_houses[k].type_house == egw:
				value = 285000 * (1 + (0.03 * extraspace))

			# value of bungalows
			elif best_houses[k].type_house == bung:
				value = 399000 * (1 + (0.04 * extraspace))

			# value of maisons
			elif best_houses[k].type_house == mais:
				value = 610000 * (1 + (0.06 * extraspace))
			
			# total value is addition of values per loop
			temporary_value += value



		# probability to accept, update each time (old version)
		# prob_accept = random.uniform(0, temperature) / temperature
		# check_value = random.uniform(0.2, 1)
		


		# update our map with the new house if total value of map is higher or because of SA probability
		if temporary_value >= best_value:
			best_value = temporary_value


		else:

			# temperature = 1.0 / float(i + 1)
			temperature = temperature * cooldown_rate


			power = float(temporary_value - best_value) / (temperature)

			# print "verkoeling = ", temporary_value - best_value
			# print "power = ", power

			prob_accept = math.exp(power)
			check_value = random.uniform(0, 1)

			# print "prob accept = ", prob_accept
			# print "check value = ", check_value 
			# print ""

			print "///////////////////////", i, "//////////////////////////"
			if prob_accept >= check_value:
				winning += 1
				best_value = temporary_value

		
			else:
				best_houses[index] = temp_house 


		# update variable to track were in the map we are
		index = index + 1

	# # print maps
	# for j in range(4):
	# 	print "TEMPORARY HOUSES :::: ", best_houses[j].x_min, best_houses[j].y_min
	# 	print "BEST HOUSES ::::::::: ", best_houses[j].x_min, best_houses[j].y_min
	
# FF CHECKEN
print ("best value = ", best_value)
print("winning = ", winning)

name2 = str(best_value) + "after"

best_map = best_houses + water

plotmap(len(beginmap), beginmap, name1, houses_total)
plotmap(len(beginmap), best_map, name2, houses_total)

















