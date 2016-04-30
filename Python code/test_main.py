# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import pylab
import random
import math

the_best = []
best_value = []

# sum all total values
sum_of_total_values = 0

class House(object):
    """
    A House represents a location on a two-dimensional field.
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

    def updateDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def getFreespace(self):
        return self.freespace

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


def distance(house, houses): 
    """
    Calculate distance to closest house
    """   

    space_diagonal = []
    space_x = []
    space_y = []

    for j in range(len(houses)):
        
        # check if house is above or underneath house
        if houses[j].y_max > house.y_min and houses[j].y_min < house.y_max:
            
            # calculations for distance to next house left and right 
            if houses[j].x_min > house.x_min:
                distance = houses[j].x_min - house.x_min - house.width 
            else:
                distance = house.x_min - houses[j].x_min - houses[j].width 

            space_x.append(distance)
                
        # fill space_x with fictional high value to ensure space_y or 
        # space_diagonal contain smaller values
        else:
            space_x.append(10000)
        
        # check whether house[j] is in horizontal band next to house        
        if houses[j].x_max > house.x_min and houses[j].x_min < house.x_max:
        
            #  calculations for distance to next house above and under
            if houses[j].y_min > house.y_min:
                distance = houses[j].y_min - house.y_min - house.height  
            else:
                distance = house.y_min - houses[j].y_min - houses[j].height  
            space_y.append(distance)
        
        # fill space_y with fictional high value 
        else:
            space_y.append(10000)
        
        # calculate diagonal distance to house[j] with pythagoras
        # if house[j] is in left top corner of house
        if houses[j].x_min >= house.x_min and houses[j].y_min >= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = houses[j].y_min - house.y_max 
            c = (a**2 + b**2)**0.5
            space_diagonal.append(c)

        # if house[j] is in right top corner of house
        elif houses[j].x_min >= house.x_min and houses[j].y_min <= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = house.y_min - houses[j].y_max 
            c = (a**2 + b**2)**0.5
            space_diagonal.append(c)

        # if house[j] is in left bottom corner of house
        elif houses[j].x_min <= house.x_min and houses[j].y_min >= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = houses[j].y_min - house.y_max 
            c = (a**2 + b**2)**0.5
            space_diagonal.append(c)

        # if house[j] is in right bottom corner of house
        elif houses[j].x_min <= house.x_min and houses[j].y_min <= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = house.y_min - houses[j].y_max 
            c = (a**2 + b**2)**0.5
            space_diagonal.append(c)

        # fill space_diagonal with fictional high value 
        else:
            space_diagonal.append(10000)
        
    # minimum distance is the only one relevant to value
    min_dist_x = min(space_x)
    min_dist_y = min(space_y)
    min_diagonal = min(space_diagonal)

    min_dist = min(min_dist_x,min_dist_y,min_diagonal)

    # save closest neighbour of house
    if min_dist == min_dist_x:
        closest = space_x.index(min_dist_x)
    elif min_dist == min_dist_y:
        closest = space_y.index(min_dist_y)
    elif min_dist == min_diagonal:
        closest = space_diagonal.index(min_diagonal)
    neighbour = houses[closest]

    # get biggest freespace (of house or closest house)
    if house.freespace > neighbour.freespace:
        freespace = house.freespace
    else:
        freespace = neighbour.freespace

    # if freespace is bigger than distance, return negative distance
    if min_dist < freespace:
        return min_dist - freespace

    # update distance to closest neighbour of house
    house.updateDistance(min_dist)

    # if neighbours closest neighbour is further away, update closest neighbour
    if neighbour.distance > min_dist:
        neighbour.updateDistance(min_dist)

    # return distance to closest neighbour's wall of house
    return min_dist

"""
Place houses on field
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

# loop x times for testing
for k in range(1000):
    
    # array of houses per test
    houses = []

    # first house is a maison
    freespace_maison = 6
    width_maison = 11
    height_maison = 10.5

    # set total value to 0
    total_value = 0
    
    # maximal values of field
    bound_x = 160
    bound_y = 150
    
    # generate a random position of first house (type maison) (x_min en y_min is the left down corner)
    type_house = mais
    x_min = random.randrange(getFreespace(type_house), 2 * (bound_x - width_maison - 1)) * 0.5
    y_min = random.randrange(getFreespace(type_house), 2 * (bound_y - height_maison - 1)) * 0.5

    # add house to list houses
    house = House(x_min, y_min, type_house)
    houses.append(house)
    
    # one house has been already made
    i = 1

    # type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
    type_total = mais_total

    # loop over maximal number of houses of this type
    while i < type_total:
        ## generate a new random position
        x_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_x - width_maison - 1)) * 0.5
        y_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_y - height_maison - 1)) * 0.5
            
        # get specifics of house we check against 
        new = House(x_min, y_min, type_house)

        # if house didn't overlap in any case, add house to list
        smallest_dist = distance(new, houses)
        if smallest_dist > 0:
            house = new.updateDistance(smallest_dist)
            houses.append(new)
            i += 1

        # set type_total to number of next type of houses 
        if i == type_total:
            if type_house == mais:
                type_house = bung

                # start loop of placing houses again
                i = 0
                type_total = bung_total

            elif type_house == bung:
                type_house = egw
                type_total = egw_total

                # start loop of placing houses again
                i = 0
    
    # Calculate total value of Amstelhaege
    
    for k in range(len(houses)):
        extraspace = math.floor(houses[k].getDistance() - houses[k].getFreespace())
        
        # value of eengezinswoningen
        if houses[k].type_house == egw:
            value = 285000 * (1+(0.03*extraspace))

        # value of bungalows
        elif houses[k].type_house == bung:
            value = 399000 * (1+(0.04*extraspace))

        # value of maisons
        elif houses[k].type_house == mais:
            value = 610000 * (1+(0.06*extraspace))
        
        # total value is addition of values per loop
        total_value += value
        
    # initiate the best list and update in later sessions
    best_value.append(total_value)

# find map with highest value from tests
highest = max(best_value)
index = best_value.index(highest)
print "index best = ", index
print "value best = ", highest

# find map with lowest value from tests
lowest = min(best_value)
print "lowest = ", lowest

# calculate mean map value of tests
mean_value = sum(best_value)/len(best_value)
print "mean = ", mean_value
