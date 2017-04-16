####################################
# Hedron 3d's net
# based on one original point
# zhuiti with words or pics
# Latex model is the latex folder/ hedron_temp.tex

####################################

import sys
import numpy as np 
import math
import os


def set_orgin(totalsides, height, bottom, color = None):
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
		#print(newside)
	#print(newpoints)
	stickers = []
	r1 = math.sqrt(math.pow(bottom/2.0, 2) + math.pow(height, 2))
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
	last.append([0,0])
	last_alpha = newpoints[-1][-1]
	point = [r1*np.cos(last_alpha), r1*np.sin(last_alpha)]
	mod = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
	second = [r3 * math.cos(last_alpha+math.pi/4), r3 * math.sin(last_alpha+math.pi/4)]
	third = [second[0] + r1*0.6*point[0]/mod, second[1] + r1*0.6*point[1]/mod]
	last.append(point)
	last.append(third)
	last.append(second)



	#get the bottom lid
	beta =  np.pi / totalsides
	r4 = bottom/(2 * np.sin(beta))

	coordinate = [0, -1 * (height + r4 * np.cos(beta))] 

	lids = []
	lids.append(np.pi/2 + beta)
	for i in range(1, totalsides):
		lids.append(lids[-1] - 2*beta)
	
	points_set = []
	for side in newpoints:
		temp = [toppoint]
		for point in side:
			temp.append([r1 * np.cos(point), r1 * np.sin(point)])
		
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
	
	points_set.append(temp)

	out_put(points_set, color)



def out_put(points_set, color):

	
	with open("hedron.txt", 'w+') as f:
		for point in points_set:
			if color:
				f.write('\\filldraw[fill =' + color + ']')
			else:
				f.write('\draw ')
			for p in point:
				f.write('('+format(p[0],'.2f') +','+ format(p[1], '.2f')+') --')
			f.write('(' + format(point[0][0], '.2f') + ',' + format(point[0][1], '.2f')+');' + '\n')
	





def content(totalsides, height, bottom, path, filename, ifpic = 0):
	ratio = 5.0/6
	pic_text_diff = 2
	textangle = []
	rotationangle = []
	textdistance = height * ratio
	picsdistance = textdistance - pic_text_diff
	textpos = []
	picspos = []

	width = (1 - (1 - ratio) * 2) * bottom

	angle = np.arctan(bottom/(2.0*height)) 
	currentangle = -1 * np.pi/2
	for i in range(0, totalsides):
		textpos.append([textdistance * np.cos(currentangle), textdistance * np.sin(currentangle)])
		picspos.append([picsdistance * np.cos(currentangle), picsdistance * np.sin(currentangle)])
		rotationangle.append((np.pi/2 + currentangle) * 180 / np.pi)
		currentangle += 2 * angle 

	textcontent = []
	picscontent = []
	p = 0
	with open(os.path.join(path, filename), 'r') as g:
		for line in g.readlines():
			line = line.strip()
			textcontent.append(line)

	for filename in os.listdir(path):
		if '.jpg' in filename or 'jpeg' in filename or '.png' in filename:
			picscontent.append(os.path.join(path, filename))
	
	if ifpic == 0:
		with open("hedron.txt", 'a') as f:
			for i in range(0, totalsides):
				f.write('\putcontent{' + format(width, '.2f') + '}{' + format(rotationangle[i], '.2f') + '}{' 
				 + format(textpos[i][0], '.2f') + '}{' + format(textpos[i][1], '.2f') + '}{' + textcontent[i] + '};\n')
	else:
		with open("hedron.txt", 'a') as f:
			for i in range(0, totalsides):

				f.write('\putcontentpics{' + format(width, '.2f') + '}{' + format(rotationangle[i], '.2f') + '}{' 
				 + format(textpos[i][0], '.2f') + '}{' + format(textpos[i][1], '.2f') + '}{' + textcontent[i] + '}{'
				 + format(picspos[i][0], '.2f') + '}{' + format(picspos[i][1], '.2f') + '}{' + picscontent[p] + '};\n')
				p += 1
				if p == len(picscontent):
					p = 0






def main():
	colors = ['red!10', 'green!10', 'blue!10', 'orange!10', 'pink!10']
	set_orgin(6, 6, 5, color = colors[0])
	content(6, 6, 5, '/Users/lxb/Documents/yyc/scripts/booksproject/millonscat/', 'proverbs.txt', ifpic=1)

if __name__ == '__main__':
	main()









