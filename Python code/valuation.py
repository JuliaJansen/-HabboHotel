# Valuation of map in euros and freespace
# Heuristieken
# Amstelhaege
# Julia, Maarten en Maarten

import math
import copy

# import other files
from house import *

def euroValuation(houses, total_value):
    """
    Returns the value of a map in euros.
    """

    # Calculate total money value of Amstelhaege
    for k in range(len(houses)):
        extraspace = math.floor(houses[k].getDistance() - houses[k].getFreespace())
        
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

    return total_value

def spaceValuation(houses, total_distance):
    """
    Returns the freespace of a map in meters.
    """
    # Calculate total freespace of Amstelhaege
    for l in range(len(houses)):
        house_distance = houses[l].distance
        total_distance += house_distance

    return total_distance
