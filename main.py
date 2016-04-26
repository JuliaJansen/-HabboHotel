# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import pylab
import random
import math

class Position(object):
    """
    A Position represents a location on a two-dimensional field.
    """

    def __init__(self, x_min, y_min, type_house):
        """
        Initializes a position with coordinates of left down corner 
        (x_min, y_min).
        """
        self.x_min = x_min
        self.y_min = y_min
        self.type_house = type_house

        if self.type_house == mais:
            self.width = 11
            self.height = 10.5
            self.freespace = 6

        if self.type_house == bung:
            self.width = 10
            self.height = 7.5
            self.freespace = 3

        if self.type_house == egw:
            self.width = 8
            self.height = 8
            self.freespace = 2

        # x_max, y_max is the top right corner of a house
        self.x_max = x_min + self.width
        self.y_max = y_min + self.height
       
    def getX_min(self):
        return self.x_min

    def getY_min(self):
        return self.y_min

    def get_type_house(self):
        return self.type_house

    def closest_neigbour(self, distance, house):
        self.neighbour = house
        self.distance = distance

def getFreespace(type_house):
    """
    Define freespace based on type house
    """

    if type_house == mais:
        return 6

    if type_house == bung:
        return 3

    if type_house == egw:
        return 2

##############################################################
## Plaats huizen van dezelfde afmetingen random op een veld ##
##############################################################

# list for houses
houses = []

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# create a variable to hold number of houses of each type
houses_total = 20
mais_total = houses_total * 0.15
bung_total = houses_total * 0.25
egw_total = houses_total * 0.60

# first house, hard coded
freespace_maison = 6
width_maison = 11
height_maison = 10.5

# maximal values of field
bound_x = 1600
bound_y = 1500

# generate a random position of first house (type maison) (x_min en y_min is the left down corner)
type_house = mais
x_min = random.randrange(getFreespace(type_house), 2 * (bound_x - width_maison - 1)) * 0.5
y_min = random.randrange(getFreespace(type_house), 2 * (bound_y - height_maison - 1)) * 0.5

# add house to list houses
house = Position(x_min, y_min, type_house)
houses.append(house)

# one house has been already made
i = 1

# type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
type_total = mais_total

# loop over maximal number of houses of this type
while i < type_total:
        
    ## generate a new random position
    x_min = random.randrange(getFreespace(type_house), 2 * (bound_x - width_maison - 1)) * 0.5
    y_min = random.randrange(getFreespace(type_house), 2 * (bound_y - height_maison - 1)) * 0.5
            
    # loop over all houses made so far
    for j in range(len(houses)):

        # get specifics of house we check against 
        new = Position(x_min, y_min, type_house)

        # print "x_min eerste huis = ", houses[0].x_min
        # print "x_min nieuwe huis = ", new.x_min      

        # check horizontal overlapping
        if houses[j].x_min < x_min: # check house < new house
            if houses[j].x_min + houses[j].width + houses[j].freespace > x_min:
                break
        elif x_min <= houses[j].x_min: # new house <= check house
            if x_min > houses[j].x_min - new.width - new.freespace:
                break

        # check vertical overlapping
        if houses[j].y_min < y_min: # check house < new house
            if houses[j].y_min + houses[j].height + houses[j].freespace > y_min:
                break
        elif y_min <= houses[j].x_min: # new house <= check house
            if y_min > houses[j].y_min - new.height - new.freespace:
                break
                    
        # if house didn't overlap in any case, add house to list
        if j == len(houses) - 1:
            print "len houses = ", len(houses)
            house = Position(x_min, y_min, type_house)
            houses.append(house)
            i += 1

    # set type_total to number of next type of houses
    if i == type_total - 1:
        if type_house == mais:
            type_house = bung
            type_total = bung_total
            i = 0
        if type_house == bung:
            type_house = egw
            type_total = egw_total
            i = 0

print houses
print len(houses)
print "end"
