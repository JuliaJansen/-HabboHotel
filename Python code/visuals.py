# plotmap()
# Heuristieken
# Julia, Maarten en Maarten

import datetime
import math
import pylab
import matplotlib.pyplot as plt
from matplotlib.path import Path
from numpy.random import normal
import matplotlib.patches as patches
import numpy as np

def plothisto(len_all_values, all_values, name, lowest, highest, mean):
    """
    Plot histogram values maps
    """
    # mean of distribution
    mu = mean
    sigma = np.std(all_values)

    # size of plot
    plt.figure(figsize=(12, 9)) 

    # make axes
    ax = plt.subplot(111)  
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False) 

    # ticks of axes
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()  

    plt.axis([lowest, highest, 0, len_all_values/20])
    # size of ticks
    # plt.yticks((range(100, len_all_values, 1000) / len_all_values), fontsize=14)  

    # ax labels
    plt.xlabel("Value Map", fontsize=16)  
    plt.ylabel("Count (bins = 100)", fontsize=16)  

    # plot data from list
    plt.hist(all_values, color="#3F5D7D", bins=100)  

    # title
    plt.title("Histogram of test results")

    # explanation under graph
    plt.text(0.7, 0.93, "mean = " + str(mean) + "  " + r"$\sigma="+ str(sigma) + "$", 
        fontsize=12,
        horizontalalignment='center',
        verticalalignment='center',
        transform = ax.transAxes)

    # show grid
    plt.grid(True, which='both', color='0.65',linestyle='-')

    # show plot
    plt.show()

    # save plot
    # plot_url = py.plot_mpl(fig, filename='..plots/histo/' + name + '.png')
    # plt.saveplt('../plots/histo/' + name + '.png', bbox_inches="tight")

def plotmap(len_fill, a_map, name, houses_total):
    """
    Plot best map
    """
    path = []
    patch_list = []

    # create a variable to hold number of houses of each type
    mais_total = houses_total * 0.15
    bung_total = houses_total * 0.25
    egw_total = houses_total * 0.60

    # loop over array houses to draw paths
    for l in range(len_fill):
        
    # prepare to plot best map
        verts = [
            (a_map[l].x_min, a_map[l].y_min), #left, bottom
            (a_map[l].x_min, a_map[l].y_max), #left, top
            (a_map[l].x_max, a_map[l].y_max), #right, top
            (a_map[l].x_max, a_map[l].y_min), #right, bottom
            (0., 0.), # ignored
            ]

        codes = [
            Path.MOVETO,
            Path.LINETO, 
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
            ]

        path.append(Path(verts, codes))

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    for m in range(len_fill):

        # add paths maison in gold
        if m < mais_total:
            patch_list.append(patches.PathPatch(path[m], facecolor="#009999", lw=2))
        
        # add paths bungalows in orange
        elif m < mais_total + bung_total:
            patch_list.append(patches.PathPatch(path[m], facecolor="#cc6600", lw=2))
            
        # add paths egws in green   
        elif m < mais_total + bung_total + egw_total:
            patch_list.append(patches.PathPatch(path[m], facecolor="#88cc00", lw=2))

        # add paths water in blue
        else:
            patch_list.append(patches.PathPatch(path[m], facecolor="#00e6ac", lw=2))

    # add pathches to the figure
    for p in patch_list:
        ax.add_patch(p)

        # set x and y limit
        ax.set_xlim(0,160)
        ax.set_ylim(0,150)

    # show plot
    plt.show()

    fig.savefig('../plots/' + str(houses_total) + '/' + name + '.png', dpi=90, bbox_inches='tight')

 