"""
Generate the half cylinder

latex model: half_cylinder

"""

import sys
import os
import numpy as np 
import math

def get_points(height, width, truncated_alpha):
	#get the center point
	 #truncate alpha by degree
	sticker_alpha = 15

	radius = width/(2 * np.sin(truncated_alpha/360.0 * np.pi))
	total_length = np.pi * 2 * radius * (360-15)/360.0 + width

	#center of page
	leftmost = -1 * total_length / 2.0

	fourpoints = []
	middleline = []

	circle_center = []
	# draw the biggest frame
	fourpoints.append([leftmost, 0])
	fourpoints.append([leftmost, -1*height])
	fourpoints.append([-1 * leftmost, -1*height ])
	fourpoints.append([-1 * leftmost, 0])

	middle = -1 * leftmost - width
	#draw half truncated face
	middleline.append([middle, 0])
	middleline.append([middle, -1*height])

	
	

	alpha = np.pi/ 180 * sticker_alpha #every 30 degree to draw a sticker

	circle_center = np.array([-1 * leftmost - width/2.0, 0])

	sticker_points = []

	count = 10

	sticker_stop = total_length - radius 

	grid_length = sticker_stop / 10

	sticker_height = 1

	current = np.array([leftmost,0])

	for i in range(0, count):
		temp = []
		temp.append(current)
		temp.append(np.array([current[0] + grid_length/2, current[1] + sticker_height]))
		temp.append(np.array([current[0] + grid_length, current[1]]))
		current = temp[-1]

		sticker_points.append(temp)

	current = np.array([leftmost, -1*height])

	for i in range(0, count):
		temp = []
		temp.append(current)
		temp.append(np.array([current[0] + grid_length/2, current[1] - sticker_height]))
		temp.append(np.array([current[0] + grid_length, current[1]]))
		current = temp[-1]

		sticker_points.append(temp)

	output_points(fourpoints, middleline, sticker_points, circle_center, radius, truncated_alpha)


def output_points(fourpoints, middleline, sticker_points, circle_center, radius, truncated_alpha):
	with open("half_cylinder.txt", 'w+') as f:
		f.write('\draw')
		for point in fourpoints:
			f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --')
		f.write('cycle;\n')

		f.write('\draw(' + format(middleline[0][0], '.2f') + ',' + format(middleline[0][1], '.2f') + ') --')
		f.write('(' + format(middleline[1][0], '.2f') + ',' + format(middleline[1][1], '.2f') + ');\n')

		#draw the arc
		begin = -90 + truncated_alpha/2.0
		end = 270 - truncated_alpha/2.0
		f.write('\draw(' + format(fourpoints[-1][0], '.2f') + ',' + format(fourpoints[-1][1], '.2f') + ') arc (' + str(begin) + ':' + str(end) + ':' + format(radius, '.2f') + ');\n')
		begin = 90 - truncated_alpha/2.0
		end = -270 + truncated_alpha/2.0
		f.write('\draw(' + format(fourpoints[-2][0], '.2f') + ',' + format(fourpoints[-2][1], '.2f') + ') arc (' + str(begin) + ':' + str(end) + ':' + format(radius, '.2f') + ');\n')
		for pointset in sticker_points:
			f.write('\draw')
			for point in pointset[:-1]:
				f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --')
			point = pointset[-1] 
			f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ');\n')
			

def main():
	get_points(3, 1, 15)



if __name__ == '__main__':
	main()








