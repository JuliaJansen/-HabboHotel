##############################################################
## Plaats huizen van dezelfde afmetingen random op een veld ##
##############################################################

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

    print "in loop"
        
    ## generate a new random position
    x_min = random.randrange(getFreespace(type_house), 2 * (bound_x - width_maison - 1)) * 0.5
    y_min = random.randrange(getFreespace(type_house), 2 * (bound_y - height_maison - 1)) * 0.5
            
    # loop over all houses made so far
    for j in range(len(houses)):
               
        # get specifics of house we check against 
        new = Position(x_min, y_min, type_house)
                
        # check horizontal overlapping
        if houses[j].x_min < x_min : # check house < new house
            if houses[j].x_min + houses[j].width + houses[j].freespace > x_min :
                break
        else if x_min <= houses[j].x_min: # new house <= check house
            if x_min > houses[j].x_min - new.width - new.freespace:
                break

        # check vertical overlapping
        if houses[j].y_min < y_min : # check house < new house
            if houses[j].y_min + houses[j].height + houses[j].freespace > y_min:
                break
        else if y_min <= houses[j].x_min: # new house <= check house
            if y_min > houses[j].y_min - new.height - new.freespace:
                break
                    
        # if house didn't overlap in any case, add house to list
        if j == len(houses):
            house = Position(x_min, y_min, type_house)
            houses.append(house)
            i = i + 1

    # set type_total to number of bungalows when all maisons have been made
    if k == type_mais - 1:
        type_house = bung
        type_total = type_bung
        i = 0

    # set type_total to number of egw's when all bunagalows have been made
    if k == type_bung - 1:
        type_house = egw
        type_total = type_egw
        i = 0

print houses
print len(houses)
print "end"
