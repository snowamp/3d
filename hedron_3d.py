"""
Hedron 3D class with color without pictures just blank

"""

import sys
import numpy as np 
import math
import os

class hedron(object):
	

	def get_points(self,totalsides, height, bottom, color = None, pictures = [], text_content=[], filled = None):
		content_center = [] #to save the content center
		newpoints = [] #save the points
		alpha = np.arctan(bottom/(2.0*height))
		toppoint = np.array([0,0])
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
			
			content_center.append((temp[0] + temp[1] + temp[2])/3)

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

		return(self.out_put(points_set, filled, pictures, text_content, content_center))



	def out_put(self, points_set, filled, pictures, text_content, content_center):
		

		string_return = ''

		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'
		
		for point in points_set:
			if filled:
				string_return += '\\filldraw[fill =' + filled + ']'
			else:
				string_return +='\draw '
			for p in point:
				string_return +='('+format(p[0],'.2f') +','+ format(p[1], '.2f')+') --'
			string_return +='(' + format(point[0][0], '.2f') + ',' + format(point[0][1], '.2f')+');' + '\n'
		if len(content_center) > 0:
			for i in range(len(content_center)):
				string_return += '\putcontent{' + format(content_center[i][0], '.2f') + '}{' + format(content_center[i][1], '.2f') + '}{'+pictures[i] + '}{'+text_content[i] + '};\n'

		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'

		return(string_return)













