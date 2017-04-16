###########################
# Try to draw the ball
###########################

import sys
import numpy as np 
import math



def get_origin(r):
	sideNumber = 5
	alpha = np.pi * 36/180
	beta = np.pi * 54/180
	uppercenter = [0, 0]
	lowercenter = [-2*r*np.cos(beta), -4*r - 2 * r * np.sin(beta)]
	
	uppersides = []
	lowersides = []

	# for upper side
	#uppervectors = []
	centers = []
	lowervectors = [] #should be vectors and no change due to workload
	allpoints = []

	currentAlpha = -1*np.pi/2
	for i in range(0, sideNumber):
		temp = np.array([2*r * np.cos(currentAlpha), 2 * r * np.sin(currentAlpha)])
		lowervectors.append(-1 * temp)
		centers.append(temp)
		currentAlpha += 2 * alpha


	currentAlpha = np.pi/2 
	for i in range(0, sideNumber):
		temp = np.array([2 * r * np.cos(currentAlpha), 2 * r * np.sin(currentAlpha)])
		lowervectors.append(-1 * temp)
		tempupdate = np.array(lowercenter) + temp
		centers.append(tempupdate)
		currentAlpha += 2 * alpha
		enlarge = 1.2 #enlarge sticker height
	# lowervector
	for v in range(0, len(centers)):
		cosalpha = lowervectors[v][0]/(np.sqrt(math.pow(lowervectors[v][0], 2) + math.pow(lowervectors[v][1], 2)))
		currentAlpha = np.arccos(cosalpha)
		if lowervectors[v][1] <= 0:
			currentAlpha = -1 * currentAlpha
		centerVector = centers[v]
		tempAlpha = currentAlpha + alpha
		tempR = r / np.cos(alpha)
		currentside_points = []
		for i in range(0, sideNumber):
			tempVector = np.array([tempR * np.cos(tempAlpha), tempR * np.sin(tempAlpha)])
			currentside_points.append(tempVector + centerVector)
			tempAlpha += 2 * alpha
		allpoints.append(currentside_points)
		if v < 5:
			stickerpoint = []
			stickerAlpha = currentAlpha + alpha + np.pi
			stickervector = np.array([tempR * enlarge * np.cos(stickerAlpha), tempR * enlarge * np.sin(stickerAlpha)]) + centerVector
			stickerpoint.append(stickervector)
			stickerpoint.append(currentside_points[2])
			stickerpoint.append(currentside_points[3])
			allpoints.append(stickerpoint)

		if v > 5:
			stickerpoint = []
			stickerAlpha = currentAlpha - alpha + np.pi
			stickervector = np.array([tempR * enlarge * np.cos(stickerAlpha), tempR * enlarge * np.sin(stickerAlpha)]) + centerVector
			stickerpoint.append(stickervector)
			stickerpoint.append(currentside_points[1])
			stickerpoint.append(currentside_points[2])
			allpoints.append(stickerpoint)


	output_point(allpoints)

def output_point(points):
	f = open('ball.txt', 'w+')
	for point in points:
		f.write('\draw ')
		for side in point:
			f.write('(' + format(side[0], '.2f') + ',' + format(side[1], '.2f') + ') --')
		f.write('(' + format(point[0][0], '.2f') + ',' + format(point[0][1],'.2f') + ');' + '\n')
	f.close()

def main():
	get_origin(1.5)

if __name__ == '__main__':
	main()




















