"""
cylinder class

"""

import numpy as np 
import math


class cylinder(object):

	def get_points(self, height, radius):
		sides = []
		tops = []
		teetch = []

		width = 2 * np.pi * radius
		sides.append((0, 0))
		sides.append((width, 0))
		sides.append((width, height))
		sides.append((0, height))

		sticker = []
		sticker.append((width,0))
		sticker.append((width+1, 1))
		sticker.append((width+1, height-1))
		sticker.append((width, height))

		# number is the total of teetch for sticker

		number = 10
		alpha = 2 * np.pi/number
		out_radius = radius + 1

		half = alpha/2.0
		current = alpha
		tops.append(alpha)
		teetch.append([current-half, current+half])
		for i in range(1, number):
			current += alpha
			tops.append(current)
			teetch.append([current-half, current+half])
		#print(teetch)
		centers = []
			
		centers.append([radius+1, height+radius + 1])

		centers.append([radius*4 + 1, height+radius + 1])

		circle_one = []

		circle_two = []

		for i in range(0, len(tops)):
			temp_one = []
			temp_one.append(np.array([out_radius * np.cos(tops[i]), out_radius * np.sin(tops[i])]) + np.array(centers[0]))
			temp_one.append(np.array([radius * np.cos(teetch[i][0]), radius * np.sin(teetch[i][0])]) + np.array(centers[0]))
			temp_one.append(np.array([radius * np.cos(teetch[i][1]), radius * np.sin(teetch[i][1])]) + np.array(centers[0]))
			circle_one.append(temp_one)

			temp_two = []
			temp_two.append(np.array([out_radius * np.cos(tops[i]), out_radius * np.sin(tops[i])]) + np.array(centers[1]))
			temp_two.append(np.array([radius * np.cos(teetch[i][0]), radius * np.sin(teetch[i][0])])+ np.array(centers[1])) 
			temp_two.append(np.array([radius * np.cos(teetch[i][1]), radius * np.sin(teetch[i][1])]) + np.array(centers[1]))
			
			circle_two.append(temp_two)

		return(self.output_points(sides,sticker, circle_one, circle_two, centers, radius))






	def output_points(self, sides, sticker, circle_one, circle_two, centers, radius):

		string_return = ''

		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'
		#draw the tops
		
		string_return +='\draw'
		for point in sides:
			string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
		string_return +='cycle;\n'
			# draw sticker
		string_return +='\draw'
		for point in sticker:
			string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
		string_return +='cycle;\n'


			# draw circle_one
		string_return +='\draw(' + format(centers[0][0], '.2f') + ',' + format(centers[0][1], '.2f') + ') circle (' + str(radius) + ');\n'
			
		for point in circle_one:
			string_return +='\draw'
			string_return +='(' + format(point[1][0], '.2f') + ',' + format(point[1][1], '.2f') + ') --'
			string_return +='(' + format(point[0][0], '.2f') + ',' + format(point[0][1], '.2f') + ') --'
			string_return +='(' + format(point[2][0], '.2f') + ',' + format(point[2][1], '.2f') + ');\n'
				
			# draw circle_two
		string_return +='\draw(' + format(centers[1][0], '.2f') + ',' + format(centers[1][1], '.2f') + ') circle (' + str(radius) + ');\n'
			
		for point in circle_two:
			string_return +='\draw'
			string_return +='(' + format(point[1][0], '.2f') + ',' + format(point[1][1], '.2f') + ') --'
			string_return +='(' + format(point[0][0], '.2f') + ',' + format(point[0][1], '.2f') + ') --'
			string_return +='(' + format(point[2][0], '.2f') + ',' + format(point[2][1], '.2f') + ');\n'
		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'

		return(string_return)







