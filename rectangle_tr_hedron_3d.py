"""
rectangle truncate hedron

"""

import numpy as np 
import math 

class rectangle_tr_hedron(object):
	def get_points(self, length , width, height, u_length):

		facets = []
		face_1 = []
		face_2 = []
		face_3 = []
		face_4 = []
		face_5 = []
		face_6 = []
		sticker_1 = []
		sticker_2 = []
		sticker_3 = []
		sticker_4 = []
		sticker_5 = []
		total_length = 2 * height + length

		u_width = width * u_length/length

		diff = (width - u_width) / 2

		face_1.append( np.array([-1 * total_length/2.0, width / 2.0 - diff]) )
		face_1.append( np.array([-1 * total_length/2.0, -1 * width/2.0 + diff]))
		face_1.append(np.array([-1 * length/2.0, -1 * width/2.0]))
		face_1.append(np.array([-1 * length/2.0, width/2.0]))

		face_2.append(np.array([-1 * length/2.0, width/2.0]))
		face_2.append(np.array([-1 * length/2.0, -1*width/2.0]))
		face_2.append(np.array([length/2.0, -1 * width/2.0]))
		face_2.append(np.array([length/2.0, width/2.0]))

		face_3.append( np.array([total_length/2.0, width / 2.0 - diff]) )
		face_3.append( np.array([total_length/2.0, -1 * width/2.0 + diff]))
		face_3.append(np.array([length/2.0, -1 * width/2.0]))
		face_3.append(np.array([length/2.0, width/2.0]))

		diff_1 = (length - u_length)/2
		total_width = width + 2 * height

		face_4.append( np.array([-1 * length/2.0, width / 2.0]) )
		face_4.append( np.array([-1 * length/2.0 + diff_1, total_width/2.0]))
		face_4.append(np.array([length/2.0 - diff_1, total_width/2.0]))
		face_4.append(np.array([length/2.0, width/2.0]))

		face_5.append( np.array([-1 * length/2.0, -1 * width / 2.0]) )
		face_5.append( np.array([-1 * length/2.0 + diff_1, -1 * total_width/2.0]))
		face_5.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0]))
		face_5.append(np.array([length/2.0, -1 * width/2.0]))

		face_6.append( np.array([-1 * length/2.0 + diff_1, -1 * total_width / 2.0]) )
		face_6.append( np.array([-1 * length/2.0 + diff_1, -1 * total_width/2.0 - u_width]))
		face_6.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0 - u_width]))
		face_6.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0 ]))

		sticker_height = -1 * height/2.0 - width/2.0

		sticker_1.append(np.array([-1 * length/2.0, sticker_height]))
		sticker_1.append(np.array([-1 * length/2.0, -1* width/2.0]))
		sticker_1.append(np.array([-1 * length/2.0 + diff_1, -1 * total_width/2.0]))

		sticker_2.append(np.array([length/2.0, sticker_height]))
		sticker_2.append(np.array([length/2.0, -1 * width/2.0]))
		sticker_2.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0]))

		sticker_3.append( np.array([-1 * length/2.0 + diff_1, -1 * total_width / 2.0]) )
		sticker_3.append( np.array([-1 * length/2.0 + diff_1, -1 * total_width/2.0 - u_width]))	
		sticker_3.append(np.array([-1 * length/2.0 + diff_1 - 1, -1 * total_width/2.0 - u_width/2.0]))	


		sticker_4.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0 - u_width]))
		sticker_4.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0 ]))
		sticker_4.append(np.array([length/2.0 - diff_1 + 1, -1 * total_width/2.0 - u_width/2.0]))


		sticker_5.append( np.array([-1 * length/2.0 + diff_1, -1 * total_width/2.0 - u_width]))
		sticker_5.append(np.array([length/2.0 - diff_1, -1 * total_width/2.0 - u_width]))
		sticker_5.append(np.array([0, -1 * total_width/2.0 - u_width - 1]))

		facets.append(face_1)
		facets.append(face_2)
		facets.append(face_3)
		facets.append(face_4)
		facets.append(face_5)
		facets.append(face_6)

		facets.append(sticker_1)
		facets.append(sticker_2)
		facets.append(sticker_3)
		facets.append(sticker_4)
		facets.append(sticker_5)

		return(self.output(facets))


	def output(self, facets):
		string_return = ''

		string_return += '\\textblockorigin{0cm}{0cm}\n'
		string_return += '\\begin{textblock*}{20cm}(3cm, 3cm)\n'
		string_return += '\\thispagestyle{empty}\n'
		string_return += '\\begin{tikzpicture}\n'

		for points in facets:
			string_return += '\draw'
			for point in points:
				string_return += '(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --'
			string_return += 'cycle;\n'

		string_return += '\end{tikzpicture}\n'
		string_return += '\end{textblock*}\n'
		string_return += '\\null\\newpage\n'

		return(string_return)



