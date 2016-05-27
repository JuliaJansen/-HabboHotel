# Class Water and water functies:
# distanceWater(obj, water), 
# placeWater(water, x_min, y_min, piece, pieces_of_water, surface_taken),
# placeAllWater(pieces_of_water) 
# Heuristieken
# Julia, Maarten en Maarten

import random
import math
import time

from visuals import *

# define surface of water
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
    """
    Places water: update attributes of Water objects
    """
    pieces_to_go = pieces_of_water - piece
    tries = 0

    # fictional value
    height = 10000

    # minimum surface for water depending on which piece
    if pieces_of_water < 3:
        minsurf = 4800 / (pieces_of_water + 2)
    else:
        minsurf = 4800 / pieces_of_water 

    while height + y_min > 150 or width + x_min > 160 or \
    new_surface_taken > surface_total + pieces_to_go * 4:    
        
        # calculate ratio
        ratio = random.uniform(0.25,4)
        
        # if more than one piece of water to place
        if pieces_of_water != piece:
            
            # make sure surface is bigger than remaining surface
            if minsurf >= 4800 - (surface_taken + pieces_to_go * 4):
                surface = random.randint(0, 4800 - surface_taken-pieces_to_go*4)
            else:
                surface = random.randint(minsurf, 4800 - surface_taken - \
                    pieces_to_go * 4) 

            # use ratio and surface to calculate height and width of water
            width = (surface / ratio) ** 0.5
            height = width * ratio 
            new_surface_taken = surface_taken + surface
        else:
            width = ((surface_total - surface_taken) / ratio) ** 0.5
            height = width * ratio
            surface = width * height 
            new_surface_taken = surface_taken + surface   

        water.updateXmax(x_min + width)
        water.updateYmax(y_min + height)

    # update attributes
    water.updateXmax(x_min + width)
    water.updateYmax(y_min + height)
    water.updateHeight(height)
    water.updateWidth(width)
    water.updateSurface(surface)
        
def distanceWater(obj, water):
    """
    Returns True if object isn't placed on water, else False
    """
    # loop over list of already placed water
    for w in range(len(water)):

        # check horizontal band
        # check if water is above or underneath new water
        if water[w].y_max > obj.y_min and water[w].y_min < obj.y_max:
            
            # check of water is placed to the left or the right 
            if water[w].x_min > obj.x_min:
                distance_x = water[w].x_min - obj.x_min - obj.width
            else:
                distance_x = obj.x_min - water[w].x_min - \
                (water[w].x_max - water[w].x_min) 
        else:
            distance_x = 1

        # in horizontal band
        if distance_x < 0:
            return False
        
        # check vertical band  
        # check if water is place to the left or to the right of new water
        if water[w].x_max > obj.x_min and water[w].x_min < obj.x_max:
        
            # check if water is above or underneath new water
            if water[w].y_min > obj.y_min:
                distance_y = water[w].y_min - obj.y_min - obj.height  
            else:
                distance_y = obj.y_min - water[w].y_min - \
                (water[w].y_max - water[w].y_min)  
        else:
            distance_y = 1

        if distance_y < 0:
            return False   

    return True

def placeAllWater(pieces_of_water):
    """
    Returns a list with semi randomly placed water and
    the surface taken up by the water objects
    """
    # initialise empty list for water objects
    water = []

    # start with first piece of water
    piece_of_water = 0
    surface_taken = 0

    # maximal values of field
    bound_x = 160
    bound_y = 150

    # calculate total surface of water
    surface_total = 0.2 * bound_x * bound_y

    # initiate first piece of water with random left bottom corner
    if pieces_of_water == 1:
        
        # if whole water surface goes in one piece, make sure to place it somehwere in the left bottom corner
        x_min = random.randint(0, 2 * (bound_x - 100)) * 0.5
        y_min = random.randint(0, 2 * (bound_y - 100)) * 0.5 
    
    # else, place first piece randomly
    else:
        x_min = random.randint(0, 2 * (0.8 * bound_x - 10)) * 0.5
        y_min = random.randint(0, 2 * (0.8 * bound_y - 10)) * 0.5

    # make new Water object
    new_water = Water(x_min, y_min, 0, 0)    
    placeWater(new_water, x_min, y_min, piece_of_water + 1, \
        pieces_of_water, surface_taken)

    # append first water to list
    water.append(new_water)
    surface_taken = new_water.surface
    piece_of_water += 1

    while piece_of_water < pieces_of_water:

        # find semi random x_min and y_min
        if pieces_of_water < 3:
            x_min = random.randint(0, 2 * (bound_x - 100)) * 0.5
            y_min = random.randint(0, 2 * (bound_y - 100)) * 0.5
        else:
            x_min = random.randint(0, 2 * (0.8 * bound_x - 10)) * 0.5
            y_min = random.randint(0, 2 * (0.8 * bound_y - 10)) * 0.5

        # new piece of water
        new_water = Water(x_min, y_min, 0, 0)    
        placeWater(new_water, x_min, y_min, piece_of_water + 1, \
            pieces_of_water, surface_taken)

        if distanceWater(new_water, water) == True:
            water.append(new_water)
            surface_taken += new_water.surface
            piece_of_water += 1

    # return list of water objects
    return water


