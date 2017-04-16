##########################################
# Draw the five sides pythongon
#latex template is "hedrop_temp.txt"
##########################################

import numpy as np 
import os
import math
import sys

def get_points(totalsides, width):
	
	points = []
	alpha =  2.0 * np.pi/totalsides
	current = 0
	for i in range(0, totalsides):
		current = i * alpha
		points.append([width * np.cos(current), width * np.sin(current)])

	output(points)

def output(points):
	with open("prism.txt", 'a') as f:
		f.write('\\null\\newpage\n')
		f.write('\draw')
		for point in points:
			f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --')
		f.write('cycle;\n')





def main():
	get_points(6, 4)

if __name__ == '__main__':
	main()









