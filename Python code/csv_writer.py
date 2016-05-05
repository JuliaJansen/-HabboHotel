###########################################
# writes the list of houses and water to  #
# a csv file named output.csv, with every #
# object seperated by row				  #
###########################################

import csv

############################################################################################################
##### delete all below later, just for checking my code as the test_main.py doesnt work atm... :/ ##########

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

# new = House(x_min, y_min, type_house)
# new_water = Water(x_min, y_min, piece_of_water, pieces_of_water)

# some hardcoded lists for try outs
houses = [House(30, 100, mais), House(50, 150, bung), House(80, 15, egw)]
water = [Water(20, 90, 1, 2), Water(55, 99, 2, 2)]
map_value = 9929938847

houses_total = 3
pieces_of_water = 2

fill = houses + water

########################################### delete until here ##############################################
############################################################################################################

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

# append the value of this map to the end of the list
MAIN.append([map_value])

# write MAIN to csv file
with open('output.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)	
	for thing in MAIN:
		writer.writerow(thing)





