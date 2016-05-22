# Class House
# getFreespace(type_house)
# getWidth(type_house)
# getHeight(type_house)
# distance(house, houses)
# distance_exclusive(house, houses, index)
# placeHouses(water, houses_total)
# Heuristieken
# Julia, Maarten en Maarten

import random
import math

from water import *
from csv_writer import *

# define bounds
bound_x = 160
bound_y = 150

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

class House(object):
    """
    A House represents a location on a two-dimensional field filled with a house.
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
       
    def updateX_min(self, x_min):
        self.x_min = x_min

    def updateY_min(self, y_min):
        self.y_min = y_min

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

def getWidth(type_house):
    """
    Define freespace based on type house
    """

    if type_house == mais:
        return 11

    if type_house == bung:
        return 10

    if type_house == egw:
        return 8


def getHeight(type_house):
    """
    Define freespace based on type house
    """

    if type_house == mais:
        return 10.5

    if type_house == bung:
        return 7.5

    if type_house == egw:
        return 8

def changeHouse(houses, house, index, water):
    """
    Replaces a houses on the map randomly
    """
    # get random new position
    x_new = random.randrange(2 * house.freespace, 2 * \
            (bound_x - house.width - house.freespace)) * 0.5
    y_new = random.randrange(2 * house.freespace, 2 * \
            (bound_y - house.height - house.freespace)) * 0.5

    while distanceWater(house, water) == False or distance(house, houses, index, True) < 0:
        # get random new position
        x_new = random.randrange(2 * houses[index].freespace, 2 * \
                (bound_x - house.width - house.freespace)) * 0.5
        y_new = random.randrange(2 * house.freespace, 2 * \
                (bound_y - house.height - house.freespace)) * 0.5

    # insert new house as object in list
    houses[index] = House(x_new, y_new, house.get_type_house)

    return houses

def distance(house, houses, index, skip): 
    """
    Returns distance to closest house.
    Distance is negative if closest house overlaps with house
    """   
    space_diagonal = []
    space_x = []
    space_y = []

    for j in range(len(houses)):

        if j == index and skip == True:
            continue
        
        # check if house is above or underneath house
        if houses[j].y_max > house.y_min and houses[j].y_min < house.y_max:
            
            # calculations for distance to next house left and right 
            if houses[j].x_min > house.x_min:
                distance = houses[j].x_min - house.x_min - house.width 
            else:
                distance = house.x_min - houses[j].x_min - houses[j].width 

            # if distance to another house is bigger than that houses distance,
            # position of house is illegal
            if houses[j].freespace > distance:
                return distance - houses[j].freespace

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
            
             # if distance to another house is bigger than that houses distance,
            # position of house is illegal
            if houses[j].freespace > distance:
                return distance - houses[j].freespace

            space_y.append(distance)
        
        # fill space_y with fictional high value 
        else:
            space_y.append(10000)
        
        # calculate diagonal distance to house[j] with pythagoras
        # if house[j] is in left top corner of house
        if houses[j].x_min >= house.x_min and houses[j].y_min >= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = houses[j].y_min - house.y_max 
            c = (a ** 2 + b ** 2) ** 0.5
            space_diagonal.append(c)

            # if distance to another house is bigger than that houses distance,
            # position of house is illegal
            if houses[j].freespace > c:
                return c - houses[j].freespace

        # if house[j] is in right top corner of house
        elif houses[j].x_min >= house.x_min and houses[j].y_min <= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = house.y_min - houses[j].y_max 
            c = (a ** 2 + b ** 2) ** 0.5
            space_diagonal.append(c)

            # if distance to another house is bigger than that houses distance,
            # position of house is illegal
            if houses[j].freespace > c:
                return c - houses[j].freespace

        # if house[j] is in left bottom corner of house
        elif houses[j].x_min <= house.x_min and houses[j].y_min >= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = houses[j].y_min - house.y_max 
            c = (a ** 2 + b ** 2) ** 0.5
            space_diagonal.append(c)

            # if distance to another house is bigger than that houses distance,
            # position of house is illegal
            if houses[j].freespace > c:
                return c - houses[j].freespace

        # if house[j] is in right bottom corner of house
        elif houses[j].x_min <= house.x_min and houses[j].y_min <= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = house.y_min - houses[j].y_max 
            c = (a ** 2 + b ** 2) ** 0.5
            space_diagonal.append(c)

            # if distance to another house is bigger than that houses distance,
            # position of house is illegal
            if houses[j].freespace > c:
                return c - houses[j].freespace

        # fill space_diagonal with fictional high value 
        else:
            space_diagonal.append(10000)

    # distance to x bounds
    if house.x_min < bound_x / 2 - (0.5 * house.width):
        xbound_dist = house.x_min
    else:
        xbound_dist = bound_x - house.x_max

    # distance to y bounds
    if house.y_min < bound_y / 2 - 0.5 * (house.height):
        ybound_dist = house.y_min
    else: 
        ybound_dist = bound_y - house.y_max

    dist_bound = min(xbound_dist, ybound_dist)
        
    # minimum distance is the only one relevant to value
    min_dist_x = min(space_x)
    min_dist_y = min(space_y)
    min_diagonal = min(space_diagonal)

    min_dist = min(min_dist_x, min_dist_y, min_diagonal, dist_bound)

    # save closest neighbour of house if neighbour is closer than bound
    if min_dist != dist_bound:
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

    # freespace is own freespace in case of no close neighbour
    else:
        freespace = house.freespace

    # if freespace is bigger than distance, return negative distance
    if min_dist < freespace:
        return min_dist - freespace

    # update distance to closest neighbour of house
    house.updateDistance(min_dist)

    # if neighbours closest neighbour is further away, update closest neighbour
    if min_dist != dist_bound:
        if neighbour.distance > min_dist:
            neighbour.updateDistance(min_dist)

    # return distance to closest neighbour's wall of house
    return min_dist

def placeHouses(water, houses_total):
    """
    Returns an array with semi randomly placed houses, taking the existing water 
    into account
    """
    # empty array to contain houses
    houses = []

    # different type of houses
    mais = "maison"
    bung = "bungalow"
    egw = "eengezinswoning"

    # create a variable to hold number of houses of each type
    mais_total = houses_total * 0.15
    bung_total = houses_total * 0.25
    egw_total = houses_total * 0.60

    # maximal values of field
    bound_x = 160
    bound_y = 150

    # start placing houses
    i = 0

    # type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
    type_total = mais_total
    type_house = mais

    # loop over maximal number of houses of this type
    while i < type_total:

        # generate a new random position
        x_min = random.randrange(2 * getFreespace(type_house), 2 * \
            (bound_x - getWidth(type_house) - getFreespace(type_house))) * 0.5
        y_min = random.randrange(2 * getFreespace(type_house), 2 * \
            (bound_y - getHeight(type_house) - getFreespace(type_house))) * 0.5
            
        # get specifics of house we check against 
        new = House(x_min, y_min, type_house)

        # if water doesn't overlap water
        if distanceWater(new, water) == True:

            # if there are any houses to check against
            if len(houses) > 0:

                # if house didn't overlap in any case, add house to list
                smallest_dist = distance(new, houses, 0, False)
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

            # append first house
            else:
                houses.append(new)
                i += 1

    # update distance of first house
    update = distance(houses[0], houses, 0, True)

    # return filled houses array
    return houses
