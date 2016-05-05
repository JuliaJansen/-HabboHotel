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
fieldnames_houses = ("x_min","y_min","type")
reader_houses = csv.DictReader(csvfile, fieldnames_houses)

# lists to contain houses and water
houses = []
water = []

# read in houses
count_row = 0
for row in reader_houses:
	if (count_row < houses_total):
		print(row['x_min'], row['y_min'], row['type'])
		x_min = row['x_min']
		y_min = row['y_min']
		type_house = row['type']
		new_house = House(x_min, y_min, type_house)
		houses.append(new_house)
	count_row += 1

# open csv file again, define fieldnames for water, instantiate the reader
csvfile = open('output.csv', 'r')
fieldnames_water = ("x_min","y_min","piece", "pieces")
reader_water = csv.DictReader(csvfile, fieldnames_water)

# read in water
count_row = 0
for row in reader_water:
	if (count_row >= houses_total):
		print(row['x_min'], row['y_min'], row['piece'], row['pieces'])
		x_min = row['x_min']
		y_min = row['y_min']
		piece_of_water = row['piece']
		pieces_of_water = row['pieces']
		new_water = Water(x_min, y_min, piece_of_water, pieces_of_water)
		water.append(new_water)
	count_row += 1

fill = houses + water

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
for objects in fill[houses_total:]:
    XXX = objects.getX_min()
    YYY = objects.getY_min()
    PIECE = objects.getPiece_of_water()
    PIECES = objects.getPieces_of_water()
    MAIN.append([XXX, YYY, PIECE, PIECES])

# write MAIN to csv file
with open('output_check.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)	
	for thing in MAIN:
		writer.writerow(thing)







