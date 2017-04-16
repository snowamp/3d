"""
cylinder class

"""

import numpy as np 
import math
import os

class cone(object):

	def get_points(self, radius, alpha):
		#alpha is degree
		number = 10
		sect = alpha * 0.5/number
		

		out_radius = radius + 1
		angle = -90

		points = []
		i = 0
		while angle <= alpha - 90:
			temp = []
			if i % 2 == 0:
				points.append([radius * np.cos(angle * np.pi/180), radius * np.sin(angle * np.pi/180)])
			elif i % 2 == 1:
				points.append([out_radius * np.cos(angle * np.pi/180), out_radius * np.sin(angle * np.pi/180)])

			angle += sect
			i += 1

		bottom_radius = radius * alpha * 1.0/ 360

		sticker = []

		sticker_alpha = 15

		angle = alpha - 90
		sticker.append([0,0])
		sticker.append([radius * np.cos(angle * np.pi/180), radius * np.sin(angle * np.pi/180) ])

		angle += sticker_alpha
		sticker.append([(radius -1) * np.cos(angle * np.pi/180), (radius -1 ) * np.sin(angle * np.pi/180)])

		angle += sticker_alpha
		sticker.append([1 * np.cos(angle * np.pi/180), 1 * np.sin(angle * np.pi/180)])

		return(self.output_points(radius, alpha, bottom_radius, points, sticker))

	def output_points(self, radius, alpha, bottom_radius, points,  sticker):
		string_return = ''
		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'
		
		string_return +='\draw(0,0) --(' + str(0) + ',' + str(-1*radius) + ');\n'
		string_return +='\draw (0,0) --(' + format(points[-1][0], '.2f') + ',' + format(points[-1][1], '.2f') + ');\n'
		string_return +='\draw(0,' + str(-1*radius) + ') arc(-90:' + str(alpha - 90) + ':' + str(radius) + ');\n'
		string_return +='\draw '
		for point in sticker:
			string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
		string_return +='cycle;\n'

		string_return +='\draw'
		for point in points[:-1]:
			string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'

		string_return +='(' + format(points[-1][0], '.2f') + ',' + format(points[-1][1], '.2f') + ');\n'

		center = [bottom_radius * 2, radius + bottom_radius * 1.5]

		string_return +='\draw (' + format(-1*center[0], '.2f') + ',' + format(-1*center[1], '.2f') + ') circle (' + format(bottom_radius, '.2f') + ');\n'
		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'

		return(string_return)

	