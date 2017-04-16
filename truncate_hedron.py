####################################
# Hedron 3d's net
# based on one original point
#zhui tai ti
####################################

import sys
import numpy as np 
import math


def set_orgin(totalsides, height, bottom, up):
	newpoints = [] #save the points
	alpha = np.arctan(bottom/(2.0*height))
	toppoint = [0,0]
	temp = [-1*np.pi/2-alpha, -1*np.pi/2 + alpha]
	newpoints.append(temp)
	for i in range(1, totalsides):
		newside = []
		newside.append(newpoints[-1][-1])
		newside.append(newpoints[-1][-1] + 2* alpha)
		newpoints.append(newside)

	stickers = []
	r1 = math.sqrt(math.pow(bottom/2.0, 2) + math.pow(height, 2))
	r1_short = r1 * up/bottom
	r2 = r1 + 1
	correct = alpha/3
	
	for i in range(1, totalsides):
		temp = newpoints[i][:]
		temp.append(temp[0] + correct)
		temp.append(temp[1] - correct)
		stickers.append(temp)
	r3 = 1.414
	#the last sticker
	last = []
	last_alpha = newpoints[-1][-1]
	first = [r1_short * np.cos(last_alpha), r1_short * np.sin(last_alpha)]
	point = [r1*np.cos(last_alpha), r1*np.sin(last_alpha)]
	mod = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
	second = [r3 * math.cos(last_alpha+math.pi/4), r3 * math.sin(last_alpha+math.pi/4)]
	third = [second[0] + r1 * 0.6*point[0]/mod, second[1] + r1 * 0.6*point[1]/mod]
	fourth = [second[0] + r1_short*0.7*point[0]/mod, second[1] + r1_short*0.7*point[1]/mod]
	last.append(first)
	last.append(point)
	last.append(third)
	last.append(fourth)



	#get the bottom lid
	beta =  np.pi / totalsides
	r4 = bottom/(2 * np.sin(beta))

	coordinate = [0, -1 * (height + r4 * np.cos(beta))] 

	lids = []
	lids.append(np.pi/2 + beta)
	for i in range(1, totalsides):
		lids.append(lids[-1] - 2*beta)
	print(lids)

	points_set = []
	for side in newpoints:
		temp = []
		temp.append([r1_short * np.cos(side[0]), r1_short * np.sin(side[0])])
		temp.append([r1 * np.cos(side[0]), r1 * np.sin(side[0])])
		temp.append([r1 * np.cos(side[1]), r1 * np.sin(side[1])])
		temp.append([r1_short * np.cos(side[1]), r1_short * np.sin(side[1])])
		points_set.append(temp)

	for point in stickers:
		temp = []
		temp.append([r1 * np.cos(point[0]), r1 * np.sin(point[0])])
		temp.append([r2 * np.cos(point[2]), r2 * np.sin(point[2])])
		temp.append([r2 * np.cos(point[3]), r2 * np.sin(point[3])])
		temp.append([r1 * np.cos(point[1]), r1 * np.sin(point[1])])
		
		points_set.append(temp)

	points_set.append(last)

	temp = []

	for angle in lids:
		temp.append([r4 * np.cos(angle) + coordinate[0], r4 * np.sin(angle) + coordinate[1]])
	#print(temp)
	points_set.append(temp)

	out_put(points_set)

def out_put(points_set):
	for point in points_set:
		sys.stdout.write('\draw ')
		for p in point:
			sys.stdout.write('('+format(p[0],'.2f') +','+ format(p[1], '.2f')+') --')
		sys.stdout.write('(' + format(point[0][0], '.2f') + ',' + format(point[0][1], '.2f')+');' + '\n')

def main():
	set_orgin(8, 6, 6, 4)

if __name__ == '__main__':
	main()









