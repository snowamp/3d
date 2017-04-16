##########################################
#Draw a trunctated cylinder net

# yuanzhu ti, truncated

# move the ellipse to other block
##########################################

import sys
import numpy as np 
import math


def get_point(bottom, shortHeight, tallHeight):
	number = 20
	r = bottom/2.0
	alpha = np.pi/number
	points = []
	temp = 0
	for i in range(0, number+1):
		temp = i * alpha
		points.append(r * np.cos(temp))
	#print(points)
	height = []
	difference = (tallHeight - shortHeight)/2
	for itm in points:
		height.append(shortHeight + difference+ itm * difference * 2/bottom)
	#print(height)
	points_set = []
	dis = np.pi * r / number


	for i in range(0, len(points)):
		points_set.append([i*dis, height[i]])

	points_draw = []

	for i in range(len(points_set)-1, -1, -1):
		points_draw.append([-1*points_set[i][0], points_set[i][1]])

	for i in range(1, len(points)):
		points_draw.append(points_set[i])

	points_output(points_draw)

def points_output(points_draw):
	newpoint = points_draw[0][0]
	endpoint = points_draw[-1][0]

	f = open('tr_cylinder.txt', 'w+')

	f.write('\draw (' + format(newpoint, '.2f') + ', 0) --' + '(' + format(points_draw[0][0], '.2f') + ',' + format(points_draw[0][1], '.2f') + ');')
	f.write('\n')
	f.write('\draw plot [smooth] coordinates {')
	for point in points_draw:
		f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') ')
	f.write('};\n')
	f.write('\draw (' + format(points_draw[-1][0], '.2f') + ',' + format(points_draw[1][1], '.2f') + ') -- (' + format(endpoint, '.2f') + ',0);'  )
	f.write('\n')
	f.write('\draw(' + format(endpoint, '.2f') + ', 0) --')
	f.write('(' + format(newpoint, '.2f') + ',0);' + '\n')
	f.close()

def obtain_ellipse(bottom, shortHeight, tallHeight):
	long_inner = np.sqrt(math.pow(bottom, 2) + math.pow(tallHeight-shortHeight, 2) )/2
	short_inner = bottom/2
	difference = long_inner * 0.13
	long_outside = long_inner + difference
	short_outside = short_inner + difference
	alpha = np.pi/6
	beta = np.pi/12
	temp = alpha
	points = []
	innerpoint_begin = get_pointvalue(long_inner, short_inner, alpha-beta)
	outerpoint = get_pointvalue(long_outside, short_outside, alpha)
	innerpoint_end = get_pointvalue(long_inner, short_inner, alpha + beta)
	points.append([innerpoint_begin, outerpoint, innerpoint_end])
	for i in range(1, 12):
		temp = []
		current_alpha = alpha + i * alpha
		innerpoint_begin = points[-1][-1][:]
		outpoint = get_pointvalue(long_outside, short_outside, current_alpha)
		innerpoint_end = get_pointvalue(long_inner, short_inner, current_alpha + beta)
		points.append([innerpoint_begin, outpoint, innerpoint_end])

	lids_output(long_inner, short_inner, points)


def get_pointvalue(longaxis, shortaxis, alpha):
	ratio = np.tan(alpha)
	coef = 1/math.pow(longaxis, 2) + math.pow(ratio, 2)/math.pow(shortaxis, 2)
	x = np.sqrt(1/coef)
	if np.cos(alpha) < 0:
		x = -1*x
	y = ratio * x

	return([x,y])

def lids_output(long_inner, short_inner, points):
	f = open('tr_cylinder.txt', 'a')
	f.write('\n')
	f.write('\draw(0, 0) ellipse (' + format(long_inner, '.2f') + ' and ' + format(short_inner, '.2f') + '); \n')
	for point in points:
		f.write('\draw (' + format(point[0][0], '.2f') + ',' + format(point[0][1], '.2f') + ') --')
		f.write('(' + format(point[1][0], '.2f') + ',' + format(point[1][1], '.2f') + ') --')
		f.write('(' + format(point[2][0], '.2f') + ',' + format(point[2][1], '.2f') + '); \n')
	f.close()







def main():
	get_point(4, 4, 8)
	obtain_ellipse(4, 4, 8)


if __name__ == '__main__':
	main()





