## Plaats huizen van dezelfde afmetingen random op een veld ##
##############################################################
import random

## list voor huizen
list huizen = []

## create een variabele for aantal huizen 
float huizen_max = 20

## maximale waarden veld
float bound_x = 160
float bound_y = 150

## genereer een random start positie voor huis (links onder hoek)
float x_min = randrange(freespace, bound_x - width - 1, 0.5)
float y_min = randrange(freespace, bound_y - height - 1, 0.5)

# stuur hoek naar class om andere hoeken te bereken, en voeg toe aan list huizen
huis = Position(x_min, y_min, width, height, freespace)
huizen.append(huis)

# there exits one house
i = 1

# loop over maximaal aantal huizen
while (i < huizen_max)

	## generate een nieuwe random plek
	float x_min = randrange(freespace, bound_x - width - 1, 0.5)
	float y_min = randrange(freespace, bound_y - height - 1, 0.5)


	## loop over alle huizen tot nu toe gemaakt
	for (j = 0; j < len(huizen); j++)

		## get coordinates of house we are checking against
		## huis = Position(x_min, y_min, width, height)

		## if newly generated house does overlap, break loop and generate a new house
		if ((huizen[j].x_min - width - freespace < x_min < huizen[j].x_min + width + freespace) && (huizen[j].y_min - height - freespace < y_min < huizen[j].y_min + height +freespace)

			break
		
		## if house didnt overlap in a case, add it to list
		if (j == len(huizen))	
			## plaats huis (voeg toe aan list)
			huis = Position(x_min, y_min, width, height)
			huizen.append(huis)
			i++




