##############################################################
## Plaats huizen van dezelfde afmetingen random op een veld ##
##############################################################

import random

# list for houses
list huizen = []

# different type of houses
var mais = "maison"
var bung = "bungalow"
var egw = "eengezinswoning"

# create a variable to hold number of houses of each type
int houses_total = 20
int mais_total = houses_total * 0.15
int bung_total = houses_total * 0.25
int egw_total = houses_total * 0.60

# maximal values of field
float bound_x = 160
float bound_y = 150

# generate a random position of first house (type maison) (x_min en y_min is the left down corner)
float x_min = randrange(freespace, bound_x - width - 1, 0.5)
float y_min = randrange(freespace, bound_y - height - 1, 0.5)
float type_house = mais

# add house to list houses
house = Position(x_min, y_min, type_house)
houses.append(house)

# one house has been already made
int i = 1

# type_total holds number of houses needed to be made of certain type. Instantiate with type maison.
int type_total = mais_total

# loop over maximal number of houses of this type
while (i < type_total):
        
    ## generate a new random position
    float x_min = randrange(freespace, bound_x - width - 1, 0.5)
    float y_min = randrange(freespace, bound_y - height - 1, 0.5)
            
    # loop over all houses made so far
    for (j = 0; j < len(houses); j++):
               
        # get specifics of house we check against 
        house = Position(x_min, y_min, type_house)
                
        # if newly generated house does overlap, break loop and generate a new house
        if ((houses[j].x_min - width - freespace < x_min < houses[j].x_min + width + freespace) && (houses[j].y_min - height - freespace < y_min < houses[j].y_min + height +freespace):
                    
            break
                    
        # if house didn't overlap in any case, add house to list
        if (j == len(houses)):
            house = Position(x_min, y_min, type_house)
            houses.append(house)
            i++

    # set type_total to number of bungalows when all maisons have been made
    if (k == type_mais - 1):
        type_house = bung
        type_total = type_bung
        i = 0

    # set type_total to number of egw's when all bunagalows have been made
    if (k == type_bung - 1):
        type_house = egw
        type_total = type_egw
        i = 0
