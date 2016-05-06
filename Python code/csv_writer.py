#
#
#

def csv_writer(map, nr_water, nr_houses):
    """
    Writes the values of a map to csv file named datetime_output.csv
    """
# main nested list 
MAIN = []

# loop over each house object, and its coordinates and type.
for objects in fill[:houses_total]:
	XXX = objects.getX_min()
	YYY = objects.getY_min()
	TYPE = objects.get_type_house()
	MAIN.append([XXX, YYY, TYPE])


# loop over each water object, and its coordinates and type.
for objects in fill[houses_total:]:
    XXX = objects.getX_min()
    YYY = objects.getY_min()
    PIECE = objects.getPiece_of_water()
    PIECES = objects.getPieces_of_water()
    MAIN.append([XXX, YYY, PIECE, PIECES])

# append the value of this map to the end of the list
MAIN.append([map_value])

# write MAIN to csv file
with open('output.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)	
	for thing in MAIN:
		writer.writerow(thing)





