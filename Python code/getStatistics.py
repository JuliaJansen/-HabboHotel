# getStatistics
# Heuristieken
# Amstelhaege
# Julia, Maarten en Maarten

import math
import copy

# import other files
from water import * 
from house import *

def getStatistics(moneyvalues, distances):
    """
    Returns (highest_value, lowest_value, index_highest_value, 
    index_lowest_value, most_freespace, least_freespace, 
    index_most_freespace, index_least_freespace, mean_value, mean_freespace

    """
    # find map with highest_value value from tests
    highest_value = max(moneyvalues)
    index_high_value = moneyvalues.index(highest_value)

    # find map with lowest_value value from tests
    lowest_value = min(moneyvalues)
    index_low_value = moneyvalues.index(lowest_value)

    # calculate mean map value of tests
    mean_value = sum(moneyvalues) / len(moneyvalues)

    # find map with most overall freespace
    most_freespace = max(distances)
    index_most_freespace = distances.index(most_freespace)

    # find map with least overall freespace
    least_freespace = min(distances)
    index_least_freespace = distances.index(least_freespace)

    # find mean freespace per map of all maps
    mean_freespace = sum(distances) / len(distances)

    return (highest_value, lowest_value, index_high_value, \
    index_low_value, most_freespace, least_freespace, \
    index_most_freespace, index_least_freespace, mean_value, mean_freespace)
