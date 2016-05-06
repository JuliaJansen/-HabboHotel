import datetime
import pylab
import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
from numpy.random import normal
import matplotlib.patches as patches



def plothisto(len_all_values, all_values, name, lowest, highest):
    """
    Plot histogram values maps
    """

    # size of plot
    plt.figure(figsize=(12, 9)) 

    ax = plt.subplot(111)  
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 

    # ticks of axes
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()  

    # size of ticks
    plt.xticks(range(int(lowest - 1), int(highest + 1)), fontsize=14)  
    plt.yticks(range(100, len_all_values, 1000), fontsize=14)  

    # ax labels
    plt.xlabel("Value Map", fontsize=16)  
    plt.ylabel("Count", fontsize=16)  

    # plot data from list
    plt.hist(all_values, color="#3F5D7D", bins=100)  

    # explanation under graph
    plt.text(1300, -5000, "Test results histogram", fontsize=10)

    # save plot
    # plt.savefig('../plots/' + name + '.png', bbox_inches="tight")

    # show plot
    plt.show()



# make histogram, save and show plot
name3 = time + "histo_" + str(nr_tests) + "tests"
plothisto(len(all_values), all_values, name3, lowest, highest)
Status API Training Shop Blog About
