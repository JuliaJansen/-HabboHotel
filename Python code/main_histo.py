# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import datetime
import pylab
import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
from numpy.random import normal
import matplotlib.patches as patches

the_best = []
all_values = []

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

def plothisto(len_all_values, all_values, name, lowest, highest):
    """
    Plot histogram values maps
    """

    # size of plot
    plt.figure(figsize=(12, 9)) 

    ax = plt.subplot(111)  
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 

    # ticks of axes
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()  

    # size of ticks
    plt.xticks(range(int(lowest - 1), int(highest + 1)), fontsize=14)  
    plt.yticks(range(100, len_all_values, 1000), fontsize=14)  

    # ax labels
    plt.xlabel("Value Map", fontsize=16)  
    plt.ylabel("Count", fontsize=16)  

    # plot data from list
    plt.hist(all_values, color="#3F5D7D", bins=100)  

    # explanation under graph
    plt.text(1300, -5000, "Test results histogram", fontsize=10)

    # save plot
    # plt.savefig('../plots/' + name + '.png', bbox_inches="tight")

    # show plot
    plt.show()


def plotmap(len_houses, index, all_maps, name):
    """
    Plot best map
    """
    path = []
    patch_list = []

    # loop over array houses to draw paths
    for l in range(len_houses):
        
        # prepare to plot best map
        verts = [
            (all_maps[index][l].x_min, all_maps[index][l].y_min), #left, bottom
            (all_maps[index][l].x_min, all_maps[index][l].y_max), #left, top
            (all_maps[index][l].x_max, all_maps[index][l].y_max), #right, top
            (all_maps[index][l].x_max, all_maps[index][l].y_min), #right, bottom
            (0., 0.), # ignored
            ]

        codes = [
            Path.MOVETO,
            Path.LINETO, 
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
            ]

        path.append(Path(verts, codes))

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
        
    for m in range(len_houses):

        # add paths maison in blue
        if m < mais_total:
            patch_list.append(patches.PathPatch(path[m], facecolor="#009999", lw=2))
        
        # add paths bungalows in orange
        elif m < mais_total + bung_total:
            patch_list.append(patches.PathPatch(path[m], facecolor="#cc6600", lw=2))
        
        # add paths egws in green
        else:
            patch_list.append(patches.PathPatch(path[m], facecolor="#88cc00", lw=2))

    # add pathches to the figure
    for p in patch_list:
        ax.add_patch(p)

    # set x and y limit
    ax.set_xlim(0,160)
    ax.set_ylim(0,150)

    # show plot
    plt.show()

    fig.savefig('../plots/' + name + '.png', dpi=90, bbox_inches='tight')

"""
MAIN: Place houses on field
"""
all_values = []
all_maps = []

# different type of houses
mais = "maison"
bung = "bungalow"
egw = "eengezinswoning"

# change how you like: houses to place & amount of tests
houses_total = 20
nr_tests = 10000

# create a variable to hold number of houses of each type
mais_total = houses_total * 0.15
bung_total = houses_total * 0.25
egw_total = houses_total * 0.60

# loop x times for testing
for k in range(nr_tests):
    
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
    all_values.append(total_value)

    #save houses-array in list 
    all_maps.append(houses)

# find map with highest value from tests
highest = max(all_values)
index_high = all_values.index(highest)
print "index best = ", index_high
print "value best = ", highest

# find map with lowest value from tests
lowest = min(all_values)
index_low = all_values.index(lowest)
print "lowest = ", lowest

# calculate mean map value of tests
mean_value = sum(all_values)/len(all_values)
print "mean = ", mean_value

# save date/time to name plot
time = datetime.datetime.now().strftime("%I%M_%B_%d_")

# # names of figures:
# # hourminute_month_day_amountofhouses_best/worst_nr.oftests_value.of.map
# name1 = time + str(houses_total) + "bestof" + str(nr_tests) + "_" + str(highest)
# name2 = time + str(houses_total) + "worstof" + str(nr_tests) + "_" + str(lowest)

# # plot best and worst map
# plotmap(len(houses), index_high, all_maps, name1)
# plotmap(len(houses), index_low, all_maps, name2)

# make histogram, save and show plot
name3 = time + "histo_" + str(nr_tests) + "tests"
plothisto(len(all_values), all_values, name3, lowest, highest)
