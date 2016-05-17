# function definition placeWater
# Heuristieken
# Amstelhaege
# Julia, Maarten en Maarten

import math
import copy
import random

# import other files
from water import * 
from house import *

def placeAllWater(pieces_of_water):
    """
    Returns a list with semi randomly placed water and
    the surface taken up by the water objects
    """
    # initialise empty list for water objects
    water = []

    # maximal values of field
    bound_x = 160
    bound_y = 150

    # calculate total surface of water
    surface_total = 0.2 * bound_x * bound_x

    # initiate first piece of water with random left bottom corner
    if pieces_of_water == 1:
        
        # if whole water surface goes in one piece, make sure to place it somehwere in the left bottom corner
        x_min = random.randint(0, 2 * (bound_x - 100)) * 0.5
        y_min = random.randint(0, 2 * (bound_y - 100)) * 0.5 
    
    # else, place first piece randomly
    else:
        x_min = random.randint(0, 2 * (0.8 * bound_x - 10)) * 0.5
        y_min = random.randint(0, 2 * (0.8 * bound_y - 10)) * 0.5

    # make new Water object
    new_water = NewWater(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken, water)    
    
    # append first water to list
    water.append(new_water)
    surface_taken = new_water.surface
    piece_of_water += 1

    while piece_of_water < pieces_of_water:

        # find semi random x_min and y_min
        if pieces_of_water < 3:
            x_min = random.randint(0, 2 * (bound_x - 100)) * 0.5
            y_min = random.randint(0, 2 * (bound_y - 100)) * 0.5
        else:
            x_min = random.randint(0, 2 * (0.8 * bound_x - 10)) * 0.5
            y_min = random.randint(0, 2 * (0.8 * bound_y - 10)) * 0.5

        # new piece of water
        new_water = NewWater(x_min, y_min, piece_of_water + 1, pieces_of_water, surface_taken, water)
    
        if distanceWater(new_water, water) == True:
            water.append(new_water)
            surface_taken += new_water.surface
            piece_of_water += 1

    # return list of water objects
    return water



