###########################################
# reads the list of houses and water from #
# a csv file named output.csv, and stores #
# this in the same object-type of list	  #
###########################################

import csv

################################################################################
############################# delete all below later ###########################
houses_total = 3
pieces_of_water = 2
total_items = houses_total + pieces_of_water + 1

# new = House(x_min, y_min, type_house)
# new_water = Water(x_min, y_min, piece_of_water, pieces_of_water)

class House(object): 
	def __init__(self, x_min, y_min, type_house):
		self.x_min = x_min
		self.y_min = y_min
		self.type_house = type_house
	def getX_min(self):
		return self.x_min
	def getY_min(self):
		return self.y_min
	def get_type_house(self):
		return self.type_house
   
class Water(object):
	def __init__(self, x_min, y_min, piece_of_water, pieces_of_water):
		self.x_min = x_min
		self.y_min = y_min
		self.piece_of_water = piece_of_water
		self.pieces_of_water = pieces_of_water    
	def getX_min(self):
		return self.x_min
	def getY_min(self):
		return self.y_min
	def getPiece_of_water(self):
		return self.piece_of_water
	def getPieces_of_water(self):
		return self.pieces_of_water

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

################################ until here ####################################
################################################################################

# open csv file, define fieldnames for houses, instantiate the reader
csvfile = open('output.csv', 'r')
fieldnames = ("one","two","three", "four")
reader = csv.DictReader(csvfile, fieldnames)

# lists to contain houses and water
houses = []
water = []
value = []

# read in houses -> water -> value
count_row = 0
for row in reader:
	
	if (count_row < houses_total):
		print(row['one'], row['two'], row['three'])
		x_min = row['one']
		y_min = row['two']
		type_house = row['three']
		new_house = House(x_min, y_min, type_house)
		houses.append(new_house)
	
	elif (count_row >= houses_total and count_row < total_items - 1):
		print(row['one'], row['two'], row['three'], row['four'])
		x_min = row['one']
		y_min = row['two']
		piece_of_water = row['three']
		pieces_of_water = row['four']
		new_water = Water(x_min, y_min, piece_of_water, pieces_of_water)
		water.append(new_water)
	
	elif (count_row == total_items - 1):
		map_value = row['one']
		print(map_value)
		value.append(map_value)
	
	count_row += 1

fill = houses + water + value

########################################################### 
#### function to check if all was read in properly	   ####
#### should be able to output the same csv file right? ####
#### delete all below later							   ####
###########################################################

# main nested list 
MAIN = []

# loop over each house object, and its coordinates and type.
for objects in fill[:houses_total]:
	XXX = objects.getX_min()
	YYY = objects.getY_min()
	TYPE = objects.get_type_house()
	MAIN.append([XXX, YYY, TYPE])


# loop over each water object, and its coordinates and type.
for objects in fill[houses_total:total_items - 1]:
	XXX = objects.getX_min()
	YYY = objects.getY_min()
	PIECE = objects.getPiece_of_water()
	PIECES = objects.getPieces_of_water()
	MAIN.append([XXX, YYY, PIECE, PIECES])

# append the value of this map to the end of the list
for objects in fill[total_items-1:total_items]:
	MAIN.append([objects])

# write MAIN to csv file
with open('output_check.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)	
	for thing in MAIN:
		writer.writerow(thing)







