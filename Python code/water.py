# Class Water and distanceWater()
# Heuristieken
# Julia, Maarten en Maarten

import random
import math

class Water(object):
    """
    A Water represents a location on a two dimensional field filled with water.
    """

    def __init__(self, x_min, y_min, pieces_of_water, piece_of_water):
        """
        Initializes a position with coordinates of left down corner
        """
        self.x_min = x_min
        self.y_min = y_min
        self.piece_of_water = piece_of_water
        self.pieces_of_water = pieces_of_water
        self.x_max = 0
        self.y_max = 0
        self.surface = 0

        # self.width, self.height, self.x_max, self.y_max, self.surface = self.placeWater(self.x_min, self.y_min, self.piece_of_water, self.pieces_of_water, surface_taken)

    def getX_min(self):
        return self.x_min

    def getY_min(self):
        return self.y_min

    def getX_max(self):
        return self.x_max

    def getY_max(self):
        return self.y_max

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def placeWater(self, x_min, y_min, piece_of_water, pieces_of_water, surface_taken):

        pieces_to_go = pieces_of_water - piece_of_water

        # fictional value
        height = 10000

        # find right proportions
        while (height + y_min > 150) or surface_taken > surface_total + pieces_to_go * 4:    
            ratio = random.randrange(1, 4)

            if pieces_of_water != piece_of_water:
                width = random.randrange(1, 2 * (160 - y_min)) * 0.5
                height = width * ratio 
            else:
                width = ((surface_total - surface_taken) / (ratio))**0.5
                height = width * ratio

            surface = width * height   
        
        self.x_max = x_min + width
        self.y_max = y_min + height 
        self.width = width
        self.heigth = height
        self.surface = self.width * self.height
        
        # return (width, height, x_max, y_max, surface)

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
                distance = water[w].x_min - obj.x_min - obj.width 
            else:
                distance = obj.x_min - water[w].x_min - water[w].width 
        else:
            distance = 1
        if distance < 0:
            return False
        
        # check vertical band  
        # check if water is place to the left or to the right of new water
        if water[w].x_max > obj.x_min and water[w].x_min < obj.x_max:
        
            # check if water is above or underneath new water
            if water[w].y_min > obj.y_min:
                distance = water[w].y_min - obj.y_min - obj.height  
            else:
                distance = obj.y_min - water[w].y_min - water[w].height  
        else:
            distance = 1
        if distance < 0:
            return False   

    return True
