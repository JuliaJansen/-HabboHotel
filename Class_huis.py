# Amstelhaege
# Julia Jansen, Maarten Brijker, Maarten Hogeweij
# Minor programmeren

import math
import random

class Position(object):
    """
    A Position represents a location on a two-dimensional field.
    """

    def __init__(self, x_min, y_min, type_house):
        """
        Initializes a position with coordinates (x_min, y_min).
        """
        self.x_min = x_min
        self.y_min = y_min
        self.type_house = type_house

        if self.type_house = mais:
            self.width = 11
            self.height = 10.5
            self.freespace = 6
            self.x_max = x_min + self.width
            self.y_max = y_min + self.height

        if self.type_house = bung:
            self.width = 10
            self.height = 7.5
            self.freespace = 3
            self.x_max = x_min + self.width
            self.y_max = y_min + self.height

        if self.type_house = egw:
            self.width = 8
            self.height = 8
            self.freespace = 2
            self.x_max = x_min + self.width
            self.y_max = y_min + self.height
        
    def getX_min(self):
        return self.x_min

    def getY_min(self):
        return self.y_min

    def get_type_house(self):
        return self.type_house