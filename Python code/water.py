# Class Water and distanceWater()
# Heuristieken
# Julia, Maarten en Maarten

import random
import math
import time
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
        self.width = 0
        self.height = 0
        self.surface = 0

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def updateXmax(self, xmax):
        self.x_max = xmax

    def updateYmax(self, ymax):
        self.y_max = ymax

    def updateWidth(self, width):
        self.width = width

    def updateHeight(self, height):
        self.height = height

    def updateSurface(self, surface):
        self.surface = surface

def placeWater(water, x_min, y_min, piece, pieces_of_water, surface_taken):

    pieces_to_go = pieces_of_water - piece
    tries = 0

    # fictional value
    height = 10000

    # minimum surface for 
    if pieces_of_water < 3:
        minsurf = 4800 / (pieces_of_water + 2)
    else:
        minsurf = 4800 / pieces_of_water 

    while height + y_min > 150 or width + x_min > 160 or new_surface_taken > surface_total + pieces_to_go * 4:    
        
        tries += 1
        if tries % 100 == 0:
            print tries
            print piece

            print height + y_min > 150
            print width + x_min > 160 
            print new_surface_taken > surface_total + pieces_to_go * 4

        # bedenk ratio
        ratio = random.uniform(0.25,4)
        
        # if more than one piece of water to place
        if pieces_of_water != piece:
            
            # make sure surface is bigger than remaining surface
            if minsurf >= 4800 - (surface_taken + pieces_to_go * 4):
                surface = random.randint(0, 4800 - surface_taken-pieces_to_go*4)
                #print "1"
            else:
                surface = random.randint(minsurf, 4800 - surface_taken - pieces_to_go * 4) 

            # use ratio and surface to calculate height and width
            width = (surface / ratio) ** 0.5
            height = width * ratio 
            new_surface_taken = surface_taken + surface
        else:
            width = ((surface_total - surface_taken) / ratio)**0.5
            height = width * ratio
            surface = width * height 
            new_surface_taken = surface_taken + surface   
            #print "3" 

    water.updateXmax(x_min + width)
    water.updateYmax(y_min + height)
    water.updateHeight(height)
    water.updateWidth(width)
    water.updateSurface(surface)
        
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
