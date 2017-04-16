"""
 hedron class

 template is hedron_temp.tex

 Had better not to put text on hedron, very hard to adjust

"""

import sys
import numpy as np 
import math

class hedron(object):

	def get_points(self, totalsides, bottom, height, pictures = [], text_content = [], filled = None):

		outside_points = []

		sticker_points = []

		
		#alpha is the center to bottom angle
		alpha = np.pi / totalsides

		inner_radius = bottom/(2.0 * np.sin(alpha) )

		inner_height = inner_radius * np.cos(alpha)

		out_radius = inner_height + height

		sticker_radius = inner_radius + height/2.0

		rotation_angles = []

		rotation_centers = []

		current = -1 * np.pi/2

		polygon = []

		correction = []

		for i in range(0, totalsides):
			
			point0 = np.array([out_radius * np.cos(current), out_radius * np.sin(current)])

			point1 = np.array([inner_radius * np.cos(current + alpha), inner_radius * np.sin(current + alpha)])

			point2 = np.array([inner_radius * np.cos(current - alpha), inner_radius * np.sin(current - alpha)])

			point3 = np.array([sticker_radius * np.cos(current + alpha), sticker_radius * np.sin(current + alpha)])

			correction.append(np.array([np.cos(current), np.sin(current)]))

			rotationCenter = (point0 + point1 + point2)/3.0

			rotationAngle = current * 180 / np.pi  - 90

			outside_points.append([point0, point1, point2])

			sticker_points.append([point0, point3, point1])

			rotation_angles.append(rotationAngle)

			rotation_centers.append(rotationCenter)

			polygon.append(point1)

			current += 2 * alpha

		outside_points.append(polygon)

		return(self.output(outside_points, sticker_points, rotation_centers, rotation_angles, correction, pictures, text_content, filled='green!10'))


	def output(self, outside_points, sticker_points, rotation_centers, rotation_angles, correction, pictures, text_content, filled):

		string_return = ''
		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'
		
		
		for pointset in outside_points:
			if filled:
				string_return +='\\filldraw[fill=' + filled + ']'
			else:
				string_return +='\draw'
			for point in pointset:
				string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
			string_return +='cycle;\n'

		for pointset in sticker_points:
			string_return +='\draw'
			for point in pointset:
				string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
			string_return +='cycle;\n'

		

		text_correction = 1

		picture_correction = 0





		if len(pictures) > 0:
			c = 0
			for i in range(len(rotation_centers)):
				string_return += '\putpicture{' + format(rotation_centers[i][0] + picture_correction * correction[i][0], '.2f') + '}{' + format(rotation_centers[i][1] + picture_correction * correction[i][1], '.2f') + '}{' + format(rotation_angles[i], '.2f') + '}{' + pictures[c] + '}\n'
				c += 1
				if i == len(pictures):
					c = 0
		if len(text_content) > 0:
			c = 0
			for i in range(len(rotation_centers)):
				string_return += '\putcontent{' + format(rotation_centers[i][0] + text_correction * correction[i][0], '.2f') + '}{' + format(rotation_centers[i][1] + text_correction * correction[i][1], '.2f') + '}{' + format(rotation_angles[i], '.2f') + '}{' + text_content[c] + '}\n'
				c += 1
				if i == len(text_content):
					c = 0

		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'
		return(string_return)


