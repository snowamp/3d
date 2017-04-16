# draw a house with pictures and color

from prism_3d import prism
from update_hedron_3d import hedron
import os
import sys


def read_picturs_text():
	path = '/Users/lxb/Documents/yyc/pictures/spring/'
	pictures = []
	for filename in os.listdir(path):
		if 'jpg' in filename or 'jpeg' in filename or 'png' in filename:
			pictures.append(os.path.join(path, filename))

	text_content = ['Hello Spring\n Welcom', 'It is beautiful', 'Flower is in blossom', 'Bird is sing', 'Grass turns green', 'Sun is warm']

	
	newhedron = hedron()
	sys.stdout.write(newhedron.get_points(6, 4, 4, pictures=pictures, text_content=text_content, filled='green!10'))


read_picturs_text()







