# Heuristieken
# Amstelhaege
# Team $HabboHotel

# Dit programma berekent de waarde van een plattegrond met specifieke indeling:
# Water in vier stukken
# Water aan de randen
# 20 Huizen aan water en gelijk verdeeld over de ruimte

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

# initialize value variable
total_value = 0

# get best best from file
plannedmap, houses, water, start_value = csv_reader("planned_map.csv", houses_total, pieces_of_water)

# calculate min distances
for i in range(len(houses)):
	houses[i].updateDistance(distance_exclusive(houses[i], houses, i))
	print "closest house = ", houses[i].distance

# calculate map value
for k in range(len(houses)):
	extraspace = math.floor(houses[k].distance - houses[k].freespace)
	
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
	total_value += value

print "map value = ", total_value

# plot map
name1 = "planned" + str(total_value)
plotmap(len(plannedmap), plannedmap, name1, houses_total)

