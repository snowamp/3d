########################################
# Draw icosahedron
########################################

import sys
import numpy as np 
import math

def get_orgin(r):
	first = []
	second = []
	third = []
	forth = []
	height = np.sqrt(3)/2 * r

	y = 0
	for i in range(0, 7):
		first.append([0, y])
		y -= r

	y = r/2
	for i in range(0, 7):
		second.append([height, y])
		y -= r

	y = 0
	for i in range(0, 6):
		third.append([2*height, y])
		y -= r

	y = r/2
	for i in range(0, 7):
		forth.append([3*height, y])
		y -= r

	leftCenters = []
	rightCenters = []
	centers = []

	for i in range(1, 6):
		temp = []
		temp.append(second[i])
		temp.append(first[i-1])
		temp.append(first[i])
		leftCenters.append(temp)

	temp = []
	temp.append(third[0])
	temp.append(second[0])
	temp.append(second[1])
	leftCenters.append(temp)

	for i in range(1, 6):
		temp = []
		temp.append(third[i])
		temp.append(forth[i])
		temp.append(forth[i+1])
		rightCenters.append(temp)

	for i in range(1, 6):
		temp = []
		temp.append(first[i])
		temp.append(second[i])
		temp.append(second[i+1])
		centers.append(temp)

	for i in range(1, 6):
		temp = []
		temp.append(second[i])
		temp.append(third[i-1])
		temp.append(third[i])
		centers.append(temp)

	temp = []
	temp.append(third[5])
	temp.append(second[5])
	temp.append(second[6])
	centers.append(temp)

	for i in range(1, 6):
		temp = []
		temp.append(forth[i])
		temp.append(third[i-1])
		temp.append(third[i])
		centers.append(temp)

	for item in leftCenters:
		temp = []
		cen = np.array([0,0])
		for point in item:
			cen = cen + np.array(point)
		cen = cen/3
		temp.append(cen)
		temp.append(item[0])
		temp.append(item[2])
		centers.append(temp)

	for item in rightCenters:
		temp = []
		cen = np.array([0,0])
		for point in item:
			cen = cen + np.array(point)
		cen = cen/3
		temp.append(cen)
		temp.append(item[0])
		temp.append(item[1])
		centers.append(temp)


	output_hedron(centers)

def output_hedron(centers):
	f = open('icosahedron.txt', 'w+')
	for itm in centers:
		f.write('\draw ')
		for point in itm:
			f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --')
		f.write('(' + format(itm[0][0], '.2f') + ',' + format(itm[0][1], '.2f') + ');\n')

	f.close()



def main():
	get_orgin(3)

if __name__ == '__main__':
	main()




