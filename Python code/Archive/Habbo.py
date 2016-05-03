####################################
# Habbo code                       #
#                                  #
#                                  #
####################################

import math
import random

import habbo_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class RectangularRoom(object):
    """
    comment
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        width: an integer > 0
        height: an integer > 0
        """
        # width, height, and make a list for tiles
        self.width = width
        self.height = height
        self.tiles = []    
        
        # make self.tiles a nested list
        for y in range(0, self.height):
            tiles_row = []
            for x in range(0, self.width):
                tiles_row.append("house")
            self.tiles.append(tiles_row)
        
    def isTileHoused(self, m, n):
        """
        returns: True if (m, n) is taken, False otherwise
        """
        # m and n are switched because of the way I implemented my nested list
        if self.tiles[n][m] == "free":
            return False
        else:
            return True
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        return self.width * self.height
        
    def getNumFreeTiles(self):
        """
        Return the total number of free tiles in the room.
        returns: an integer
        """
        count_free = 0
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.tiles[y][x] == "free":
                    count_free += 1
        return count_free

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        rand_x = random.randint(0, self.width)
        rand_y = random.randint(0, self.height)
        return Position(rand_x, rand_y)
        
    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # check if x and y are greater than 0, and smaller than width and height
        if pos.getX() <= self.width and pos.getX() >= 0 and pos.getY() <= self.height and pos.getY() >= 0:
            return True
        else:
            return False

def runSimulation(width, height):
    """
    comment
    """
    anim = habbo_visualize.RobotVisualization(width, height, 30)
    
    # make a room, list to contain robots, set percentage_clean to zero 
    room = RectangularRoom(width, height)
            
    # trial is over, close simulation
    anim.done()
 
# use this to run without shell
avg = runSimulation(160, 80)