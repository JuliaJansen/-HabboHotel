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
        self.distance = 160
        self.neighbour = None

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


"""
Plaats huizen van dezelfde afmetingen random op een veld
"""
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
bound_x = 160
bound_y = 150

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
            
    # get specifics of house we check against 
    new = Position(x_min, y_min, type_house)

    # print "x_min eerste huis = ", houses[0].x_min
    # print "x_min nieuwe huis = ", new.x_min      

    # if house didn't overlap in any case, add house to list
    if afstand(new, houses) > 0:
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
