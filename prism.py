"""
Draw the flatten figure of prism
latex template is "prism.tex with polyhedron together"
"""

import numpy as np 
import os 
import math
import sys

def get_points(totalsides, height, width):

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

	chord1 = width / 2
	r = (math.pow(chord1, 2) + 1)/2
	beta = np.arcsin((r-1)/r)

	

	#draw the arc for stick
	

	chord = height / 2
	radius = (math.pow(chord, 2) + 1)/2

	alpha = -1 * np.arccos((radius - 1)/radius)

	



	output(fourpoints, separatepoints, height, alpha, radius, beta, r )

def output(fourpoints, separatepoints, height, alpha, radius,  beta, r):

	with open("prism.txt", 'w+') as f:
		f.write('\draw')
		
		f.write('(' + format(fourpoints[0][0], '.2f') + ',' + format(fourpoints[0][1], '.2f') + ') --')
		f.write('(' + format(fourpoints[1][0], '.2f') + ',' + format(fourpoints[1][1], '.2f') + ') --')
		f.write('(' + format(fourpoints[3][0], '.2f') + ',' + format(fourpoints[3][1], '.2f') + ') --')
		f.write('(' + format(fourpoints[2][0], '.2f') + ',' + format(fourpoints[2][1], '.2f') + ') --')
		f.write('cycle;\n')

		for point in separatepoints[:-1]:
			f.write('\draw(' + format(point, '.2f') + ',' + format(height*1.0/2, '.2f') + ') --')
			f.write('(' + format(point, '.2f') + ',' + format(-1.0*height/2, '.2f') + ');\n')

		#draw the uppersticker
		for point in separatepoints:
			f.write('\draw(' + format(point, '.2f') + ',' + format(height*1.0/2, '.2f') + ') arc(')
			f.write(format(beta*180.0/np.pi) +':' + format((np.pi-beta) * 180/np.pi, '.2f') + ':' + format(r, '.2f') + ');\n')

		for point in separatepoints:
			f.write('\draw(' + format(point, '.2f') + ',' + format(-1.0* height/2, '.2f') + ') arc(')
			f.write(format(-1*beta*180.0/np.pi) +':' + format(-1*(np.pi-beta) * 180/np.pi, '.2f') + ':' + format(r, '.2f') + ');\n')

		f.write('\draw(' + format(fourpoints[-1][0], '.2f') + ',' + format(fourpoints[-1][1], '.2f') + ') arc(')
		f.write(format(alpha*180.0/np.pi) +':' + format(-1*alpha * 180.0/np.pi, '.2f') + ':' + format(radius, '.2f') + ');\n')

def content(totalsides, height, width, path, filename):
	leftmost = int(-1 * totalsides * width/2.0)
	textcontent = []

	with open(os.path.join(path, filename), 'r') as g:
		for line in g.readlines():
			line = line.strip()
			textcontent.append(line)

	textpos = []
	current = leftmost + 1.0 * width / 2
	for i in range(0, totalsides):
		current = leftmost + 1.0 * width / 2 + i * width
		textpos.append([current, height/6])

	with open("prism.txt", 'a') as f:
		for i in range(0, totalsides):
			f.write('\putcontent{' + format(width * 0.9, '.2f') + '}{' 
			 + format(textpos[i][0], '.2f') + '}{' + format(textpos[i][1], '.2f') + '}{' + textcontent[i] + '};\n')


def get_polyhedron_points(totalsides, width): #bottom
	
	points = []
	alpha =  2.0 * np.pi/totalsides
	current = 0
	for i in range(0, totalsides):
		current = i * alpha
		points.append([width * np.cos(current), width * np.sin(current)])

	output_polyhedron(points)

def output_polyhedron(points):
	with open("prism.txt", 'a') as f:
		f.write('\\null\\newpage\n')
		f.write('\draw')
		for point in points:
			f.write('(' + format(point[0], '.2f') + ',' + format(point[1], '.2f') + ') --')
		f.write('cycle;\n')


def main():
	get_points(6, 8, 4)
	content(6, 8, 4, '/Users/lxb/Documents/yyc/scripts/booksproject/ifgiveamouseacookie/', 'scenario.txt')
	get_polyhedron_points(6, 4)

if __name__ == '__main__':
	main()















