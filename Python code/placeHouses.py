# function definition placeHouses
# Heuristieken
# Amstelhaege
# Julia, Maarten en Maarten

import math
import random

# import other files
from water import * 
from house import *

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
        x_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_x - getWidth(type_house) - 1)) * 0.5
        y_min = random.randrange(getFreespace(type_house), 2 * \
            (bound_y - getHeight(type_house) - 1)) * 0.5
            
        # get specifics of house we check against 
        new = House(x_min, y_min, type_house)

        # if water doesn't overlap water
        if distanceWater(new, water) == True:

            # if there are any houses to check against
            if len(houses) > 0:

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

            # append first house
            else:
                houses.append(new)
                i += 1

    # update distance of first house
    update = distance_exclusive(houses[0], houses, 0)

    # return filled houses array
    return houses