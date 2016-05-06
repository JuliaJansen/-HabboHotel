# Class Water and distanceWater()
# Heuristieken
# Julia, Maarten en Maarten

import random
import math

# global variable
surface_total = 0.2 * 160 * 150

class Water(object):
    """
    A Water represents a location on a two dimensional field filled with water.
    """

    def __init__(self, x_min, y_min, piece_of_water, pieces_of_water, surface_taken):
        """
        Initializes a position with coordinates of left down corner
        """
        self.x_min = x_min
        self.y_min = y_min
        self.piece_of_water = piece_of_water
        self.pieces_of_water = pieces_of_water
        self.x_max = 0
        self.y_max = 0
        self.width = 0
        self.height = 0
        self.surface = self.placeWater(self.x_min, self.y_min, self.piece_of_water, self.pieces_of_water, surface_taken)

    def getX_min(self):
        return self.x_min

    def getY_min(self):
        return self.y_min
        
    def getPiece_of_water(self):
        return self.piece_of_water

    def getX_max(self):
        return self.x_max

    def getY_max(self):
        return self.y_max

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def updateXmax(self, xmax):
        return self.x_max

    def placeWater(self, x_min, y_min, piece_of_water, pieces_of_water, surface_taken):

        pieces_to_go = pieces_of_water - piece_of_water

        # fictional value
        height = 10000

        # find right proportions
        while (height + y_min > 150) or new_surface_taken > surface_total + pieces_to_go * 4:    

            # give ratio
            ratio = random.randrange(10, 40) * 0.1
            print "ratio =", ratio

            if pieces_of_water != piece_of_water:
                surface = random.randrange(400, 4400) / (pieces_of_water - piece_of_water)
                width = (surface / ratio) ** 0.5
                height = width * ratio 
                new_surface_taken = surface_taken + surface
            else:
                print "surface taken, total = ", surface_taken, surface_total
                width = ((surface_total - surface_taken) / ratio)**0.5
                height = width * ratio
                surface = width * height  
                new_surface_taken = surface_taken + surface     
        
        self.x_max = x_min + width
        self.y_max = y_min + height 
        self.width = width
        self.heigth = height
        self.surface = surface

        return self.surface 
        
def distanceWater(obj, water):
    """
    Returns True if object isn't placed on water, else False
    """
    # loop over water already placed
    for w in range(len(water)):

        # check horizontal band
        # check if water is above or underneath new water
        if water[w].y_max > obj.y_min and water[w].y_min < obj.y_max:
            
            # check of water is placed to the left or the right 
            if water[w].x_min > obj.x_min:
                distance_x = water[w].x_min - obj.x_min - obj.width 
            else:
                distance_x = obj.x_min - water[w].x_min - water[w].width 
        else:
            distance_x = 1

        if distance_x < 0:
            # print "in horizontal band"
            return False
        
        # check vertical band  
        # check if water is place to the left or to the right of new water
        if water[w].x_max > obj.x_min and water[w].x_min < obj.x_max:
        
            # check if water is above or underneath new water
            if water[w].y_min > obj.y_min:
                distance_y = water[w].y_min - obj.y_min - obj.height  
            else:
                distance_y = obj.y_min - water[w].y_min - water[w].height  
        else:
            distance_y = 1

        if distance_y < 0:
            # print "in vert band"
            return False   

        # if object is in both horizontal and vertical band of water object
        # they overlap... so return False
        if distance_y == 1 and distance_x == 1:
            # print "overlap"
            return False

    return True
