# Amstelhaege
# Julia Jansen, Maarten Brijker, Maarten Hogeweij
# Minor programmeren

import math
import random

class Position(object):
    """
    A Position represents a location on a two-dimensional field.
    """

    def __init__(self, x_min, y_min, width, height):
        """
        Initializes a position with coordinates (x_min, y_min).
        """
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_min + width
        self.y_max = y_min + height


    def getX_min(self):
        return self.x_min

    def getY_min(self):
        return self.y_min