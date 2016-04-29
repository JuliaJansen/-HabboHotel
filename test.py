# main python file            #
# add classes and code below  #
# # # # # # # # # # # # # # # #

import pylab
import random
import math

the_best = []
best_value = 0

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


def afstand(house, houses): 
    """
    Calculate distance to closest house
    """   

    afstandschuin = []
    afstandenx = []
    afstandeny = []

    for j in range(len(houses)):
        # check eerst of huis je boven of onder dit huis ligt
        if houses[j].y_max > house.y_min and houses[j].y_min < house.y_max:
            
            # twee berekeningen, een voor links een voor rechts
            if houses[j].x_min > house.x_min:
                afstand = houses[j].x_min - house.x_min - house.width 
            else:
                afstand = house.x_min - houses[j].x_min - houses[j].width 

            afstandenx.append(afstand)
                
        # fake value to fill up list
        else:
            afstandenx.append(10000)
        
        # check eerst of huis j naast dit huis ligt        
        if houses[j].x_max > house.x_min and houses[j].x_min < house.x_max:
        
            # twee berekeningen, een voor onder een voor boven
            if houses[j].y_min > house.y_min:
                afstand = houses[j].y_min - house.y_min - house.height  
            else:
                afstand = house.y_min - houses[j].y_min - houses[j].height  
            afstandeny.append(afstand)
        
        else:
            afstandeny.append(10000)
        
        if houses[j].x_min >= house.x_min and houses[j].y_min >= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = houses[j].y_min - house.y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min >= house.x_min and houses[j].y_min <= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = house.y_min - houses[j].y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min <= house.x_min and houses[j].y_min >= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = houses[j].y_min - house.y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min <= house.x_min and houses[j].y_min <= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = house.y_min - houses[j].y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        else:
            afstandschuin.append(10000)
        
    # minimum distance is the only one relevant to value
    minafstx = min(afstandenx)
    minafsty = min(afstandeny)
    minafstschuin = min(afstandschuin)

    minafst = min(minafstx,minafsty,minafstschuin)

    # save closest neighbour of house
    if minafst == minafstx:
        closest = afstandenx.index(minafstx)
    elif minafst == minafsty:
        closest = afstandeny.index(minafsty)
    elif minafst == minafstschuin:
        closest = afstandschuin.index(minafstschuin)
    neighbour = houses[closest]

    # get biggest freespace (of house or closest house)
    if house.freespace > neighbour.freespace:
        freespace = house.freespace
    else:
        freespace = neighbour.freespace

    # if freespace is bigger than distance, return negative distance
    if minafst < freespace:
        return minafst - freespace

    # update distance to closest neighbour of house
    house.updateDistance(minafst)

    # if neighbours closest neighbour is further away, update closest neighbour
    if neighbour.distance > minafst:
        neighbour.updateDistance(minafst)

    # return distance to closest neighbour's wall of house
    return minafst

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
for session in range(3):
    # first house, hard coded
    freespace_maison = 6
    width_maison = 11
    height_maison = 10.5
    total_value = 0
    best_value = 0

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
        x_min = random.randrange(getFreespace(type_house), 2 * (bound_x - width_maison - 1)) * 0.5
        y_min = random.randrange(getFreespace(type_house), 2 * (bound_y - height_maison - 1)) * 0.5
            
        # get specifics of house we check against 
        new = House(x_min, y_min, type_house)

        # print "x_min eerste huis = ", houses[0].x_min
        # print "x_min nieuwe huis = ", new.x_min      
    
        # if house didn't overlap in any case, add house to list
        min_dist = afstand(new, houses)
        if min_dist > 0:
            house = new.updateDistance(min_dist)
            houses.append(new)
            i += 1

        # set type_total to number of next type of houses
        if i == type_total:
            if type_house == mais:
                type_house = bung
                i = 0
                type_total = bung_total
            elif type_house == bung:
                type_house = egw
                type_total = egw_total
                i = 0
    
    # Calculate total value of Amstelhaege
    
    print "waarde voor loop", total_value
    for k in range(len(houses)):
        extraspace = math.floor(houses[k].getDistance() - houses[k].getFreespace())
        #print "extraspace = ", extraspace
        if houses[k].type_house == egw:
            waarde = 285000 * (1+(0.03*extraspace))
        elif houses[k].type_house == bung:
            waarde = 399000 * (1+(0.04*extraspace))
        elif houses[k].type_house == mais:
            waarde = 610000 * (1+(0.06*extraspace))
        total_value += waarde
        #print "totale waarde is", total_value
        # initiate the best list and update in later sessions
    if (total_value > best_value):
	    the_best = houses
	    best_value = total_value
    print "beste tot nu toe =", best_value
    # update sum of total values variable
    sum_of_total_values =+ total_value
    print "som =", sum_of_total_values
    total_value = 0
    

# calculate mean value of total
mean_value = sum_of_total_values / 3
print "gemiddelde", mean_value
