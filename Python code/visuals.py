# plotmap()
# Heuristieken
# Julia, Maarten en Maarten

import datetime
import random
import math
import pylab
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def plotmap(len_fill, index, all_maps, name, houses_total):
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
			(all_maps[index][l].x_min, all_maps[index][l].y_min), #left, bottom
			(all_maps[index][l].x_min, all_maps[index][l].y_max), #left, top
			(all_maps[index][l].x_max, all_maps[index][l].y_max), #right, top
			(all_maps[index][l].x_max, all_maps[index][l].y_min), #right, bottom
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

	fig.savefig('../plots/' + name + '.png', dpi=90, bbox_inches='tight')