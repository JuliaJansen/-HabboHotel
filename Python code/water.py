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

    def __init__(self, x_min, y_min, x_max, y_max):
        """
        Initializes a position with coordinates of left down corner
        """
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.x_max = 0
        self.y_max = 0
        self.width = 0
        self.height = 0
        self.surface = self.placeWater(self.x_min, self.y_min, self.piece_of_water, self.pieces_of_water, surface_taken, water)

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

    def placeWater(self, x_min, y_min, piece_of_water, pieces_of_water, surface_taken, water):

    pieces_to_go = pieces_of_water - piece_of_water
    pogingen = 0

    # fictional value
    height = 10000
    minsurf = 4800/pieces_of_water+2
    while (height + y_min > 150) or width + x_min > 160 or new_surface_taken > surface_total + pieces_to_go * 4:    
        
        # bedenk ratio
        ratio = random.uniform(0.25,4)
        tries +=1
        if tries % 100 == 0:
                print "tries:", tries, piece_of_water
            # if unsuccesful, print amount of tries

        if pieces_of_water != piece_of_water:
            
            # make sure surface is bigger than remaining surface
            if minsurf >= 4800-(surface_taken+pieces_to_go*4):
                surface = random.randrange(0, 4800 - surface_taken-pieces_to_go*4)
            else:
                surface = random.randrange(minsurf, 4800-surface_taken-pieces_to_go*4) 
            # use ratio and surface to calculate height and width
            width = (surface / ratio) ** 0.5
            height = width * ratio 
            new_surface_taken = surface_taken + surface
        else:
            width = ((surface_total - surface_taken) / ratio)**0.5
            height = width * ratio
            surface = width * height 
            new_surface_taken = surface_taken + surface    
            
    self.x_max = x_min + width
    self.y_max = y_min + height 
    self.width = width
    self.heigth = height
    self.surface = surface
    #tries = 0
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
        #if distance_y == 1 and distance_x == 1:
            # print "overlap"
        #    return False

    return True
