"""
truncated hedron class

"""

import sys
import numpy as np 
import math

class truncated_hedron(object):

	def get_points(self, totalsides, bottom, upper, height):

		outside_points = []

		sticker_points = []

		uppersticker_points = []

		#alpha is the center to bottom angle
		alpha = np.pi / totalsides

		inner_radius = bottom/(2.0 * np.sin(alpha) )

		inner_height = inner_radius * np.cos(alpha)

		out_height = inner_height + height

		sticker_radius = inner_radius + height/2.0

		beta = np.arctan(upper/(2.0 * out_height) )

		outer_radius = upper/(2 * np.sin(beta))

		current = 0
		for i in range(0, totalsides):
			

			begin = current

			point0 = np.array([inner_radius * np.cos(current), inner_radius * np.sin(current)])

			point1 = np.array([sticker_radius * np.cos(current), sticker_radius * np.sin(current)])

			current += alpha - beta

			point2 = np.array([outer_radius * np.cos(current), outer_radius * np.sin(current)])

			current += 2 * beta

			point3 = np.array([outer_radius * np.cos(current), outer_radius * np.sin(current)])

			current = begin + 2 * alpha
			point4 = np.array([inner_radius * np.cos(current), inner_radius * np.sin(current)])

			outside_points.append([point0, point2, point3, point4])
			sticker_points.append([point0, point1, point2])

		# draw the upper lid

		upperlid_radius = upper/(2* np.sin(alpha))

		upperlid2center = out_height + upperlid_radius * np.cos(alpha)

		upperlid_center = np.array([upperlid2center * np.cos(alpha), upperlid2center * np.sin(alpha)])

		upperlidset = [outside_points[0][2], outside_points[0][1]]

		center2point_upper = upperlidset[-1] - upperlid_center #first vector of upper lid

		rotate_matrix = np.array([[np.cos(2 * alpha), -1 * np.sin(2 * alpha)], [np.sin(2 * alpha), np.cos(2 * alpha)]]) #vector rotate matrix

		for i in range(0, totalsides-2):

			center2point_upper = np.matmul(rotate_matrix, center2point_upper)
			upperlidset.append(center2point_upper + upperlid_center)

		# draw upper sticker for others
		current = 3 * alpha
		sticker_length = upperlid2center - upperlid_radius * 0.4
		for pointset in outside_points[1:]:
			temp_sticker = np.array([sticker_length * np.cos(current), sticker_length * np.sin(current)])
			uppersticker_points.append([pointset[1], temp_sticker, pointset[2]])
			current += 2 * alpha

		return(self.output(outside_points, sticker_points, upperlidset, uppersticker_points))


	def output(self, outside_points, sticker_points, upperlidset, uppersticker_points):

		string_return = ''
		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'
		
		
		for pointset in outside_points:
			string_return +='\draw'
			for point in pointset:
				string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
			string_return +='cycle;\n'

		for pointset in sticker_points:
			string_return +='\draw'
			for point in pointset:
				string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
			string_return +='cycle;\n'

		for pointset in uppersticker_points:
			string_return +='\draw'
			for point in pointset:
				string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
			string_return +='cycle;\n'

		string_return +='\draw'
		for point in upperlidset:
			string_return +='(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
		string_return +='cycle;\n'

		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'
		return(string_return)


