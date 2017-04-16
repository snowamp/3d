"""
prism class

"""

import numpy as np 
import os 
import math
import sys

class prism(object):

	def get_points(self, totalsides, height, width, pictures=[], text_content=[]):


		content_center = [] #save the content:picture and text position. The position need be adjusted in latex

		string_return = ''

		total_length = totalsides * width 

		leftmost = int(-1 * total_length/2.0) #very important variable, used by content too

		fourpoints = []

		fourpoints.append([leftmost, height*1.0/2])
		fourpoints.append([leftmost, -1.0*height/2])
		fourpoints.append([leftmost + total_length, height*1.0/2])
		fourpoints.append([leftmost + total_length, -1.0*height/2])

		separatepoints = []

		for i in range(1, totalsides + 1):
			currentx = leftmost +  i * width
			separatepoints.append(currentx)
			content_center_x = currentx - width/2.0
			content_center.append([content_center_x, 0])

		chord1 = width / 2
		r = (math.pow(chord1, 2) + 1)/2
		beta = np.arcsin((r-1)/r)

		

		#draw the arc for stick
		

		chord = height / 2
		radius = (math.pow(chord, 2) + 1)/2

		alpha = -1 * np.arccos((radius - 1)/radius)


		# draw lids
		upper_lids_points = []
		lower_lids_points = []
		p_alpha = np.pi/totalsides
		p_radius = width / (2 * np.sin(p_alpha))

		uppercenter = np.array([leftmost + width/2.0, height/2.0 + p_radius * np.cos(p_alpha)])
		lowercenter = np.array([leftmost + width/2.0, -1 * height/2.0 - p_radius * np.cos(p_alpha)])

		current = -1 * p_alpha - np.pi/2

		for i in range(0, totalsides):
			upper_lids_points.append(uppercenter + np.array([p_radius * np.cos(current), p_radius * np.sin(current)]))
			current += 2 * p_alpha

		current = np.pi/2 - p_alpha

		for i in range(0, totalsides):
			lower_lids_points.append(lowercenter + np.array([p_radius * np.cos(current), p_radius * np.sin(current)]))
			current += 2 * p_alpha




		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'
		
		
		string_return += self.output(fourpoints, separatepoints, height, alpha, radius, beta, r, upper_lids_points, lower_lids_points, pictures, text_content, content_center, filled=True )

		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'
		return(string_return)

	def output(self, fourpoints, separatepoints, height, alpha, radius,  beta, r, upper_lids_points, lower_lids_points, pictures, text_content, content_center, filled=False):

		string_r = ''
		
		string_r +='\draw'

		if filled:
			string_r += '\\filldraw[fill=green!10]'
		else:
			string_r += '\draw'
			
		string_r +='(' + format(fourpoints[0][0], '.2f') + ',' + format(fourpoints[0][1], '.2f') + ') --'
		string_r +='(' + format(fourpoints[1][0], '.2f') + ',' + format(fourpoints[1][1], '.2f') + ') --'
		string_r +='(' + format(fourpoints[3][0], '.2f') + ',' + format(fourpoints[3][1], '.2f') + ') --'
		string_r +='(' + format(fourpoints[2][0], '.2f') + ',' + format(fourpoints[2][1], '.2f') + ') --'
		string_r +='cycle;\n'

		for point in separatepoints[:-1]:
			string_r +='\draw(' + format(point, '.2f') + ',' + format(height*1.0/2, '.2f') + ') --'
			string_r +='(' + format(point, '.2f') + ',' + format(-1.0*height/2, '.2f') + ');\n'

			#draw the uppersticker
		for point in separatepoints[2:]:
			string_r +='\draw(' + format(point, '.2f') + ',' + format(height*1.0/2, '.2f') + ') arc('
			string_r += format(beta*180.0/np.pi) +':' + format((np.pi-beta) * 180/np.pi, '.2f') + ':' + format(r, '.2f') + ');\n'

		for point in separatepoints[2:]:
			string_r +='\draw(' + format(point, '.2f') + ',' + format(-1.0* height/2, '.2f') + ') arc('
			string_r +=format(-1*beta*180.0/np.pi) +':' + format(-1*(np.pi-beta) * 180/np.pi, '.2f') + ':' + format(r, '.2f') + ');\n'

		string_r +='\draw(' + format(fourpoints[-1][0], '.2f') + ',' + format(fourpoints[-1][1], '.2f') + ') arc('
		string_r +=format(alpha*180.0/np.pi) +':' + format(-1*alpha * 180.0/np.pi, '.2f') + ':' + format(radius, '.2f') + ');\n'

		string_r += '\draw'
		for point in upper_lids_points:
			string_r +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
		string_r += 'cycle;\n'

		string_r += '\draw'
		for point in lower_lids_points:
			string_r +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
		string_r += 'cycle;\n'


		if len(text_content) > 0:
			c = 0
			for i in range(len(content_center)):
				string_r += '\putcontent{' + format(content_center[i][0], '.2f') + '}{' + format(content_center[i][1], '.2f') + '}{'+text_content[c] + '};\n'
				c += 1
				if c == len(content_center):
					c = 0

		if len(pictures) > 0:
			c = 0
			for i in range(len(content_center)):
				string_r += '\putpicture{' + format(content_center[i][0], '.2f') + '}{' + format(content_center[i][1], '.2f') + '}{'+pictures[c] + '};\n'
				c += 1
				if c == len(pictures):
					c = 0
		return(string_r)











	
