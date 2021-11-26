from PIL import Image, ImageFilter
from random import uniform, randint
import numpy as np
import pygame as pg


class TerrainBuilder:

	def __init__(self,window,choice):
		self.window = window
		list_point = []
		if(choice <= 2):
			#all choice under 2 have left and right border in the sea
			#adding down left corner point
			list_point.append([0,uniform(HEIGHT,HEIGHT+100)])
			#adding down right corner point
			list_point.append([WIDTH,uniform(HEIGHT,HEIGHT+100)])
		else:
			#all choice over 2 have left and right border above the sea
			list_point.append([0,uniform(HEIGHT*3/5,HEIGHT*9/10)])
			list_point.append([WIDTH,uniform(HEIGHT*3/5,HEIGHT*9/10)])

		if(choice == 0):
			# choice 0 is a simple dome
			#adding one point somewhere in the middle to have a n=2 polynomial
			list_point.append([WIDTH/2,uniform(HEIGHT/4,(HEIGHT*9)/10)])
		elif(choice == 1):
			# choice 1 is a 2 spike terrain with water in the middle and on the sides
			list_point.append([WIDTH/4,uniform(HEIGHT*2/5,HEIGHT/2)])
			list_point.append([WIDTH/2,uniform(HEIGHT,HEIGHT+50)])
			list_point.append([WIDTH*3/4,uniform(HEIGHT*2/5,HEIGHT/2)])
		elif(choice == 2):
			# choice 2 is a two spike terrain with no water in the middle but water on the sides
			list_point.append([WIDTH/4,uniform(HEIGHT/4,HEIGHT/2)])
			list_point.append([WIDTH/2,uniform(HEIGHT*2/5,HEIGHT*9/10)])
			list_point.append([WIDTH*3/4,uniform(HEIGHT/4,HEIGHT/2)])
		elif(choice == 3):
			# choice 3 is an inverted dome
			list_point.append([WIDTH/2,uniform(HEIGHT,HEIGHT+50)])
		elif(choice == 4):
			# choice 4 is a 3 spike terrain with water between the spikes but not on the sides
			list_point.append([WIDTH/4,HEIGHT])
			list_point.append([WIDTH/2,uniform(HEIGHT/4,HEIGHT/2)])
			list_point.append([WIDTH*3/4,uniform(HEIGHT,HEIGHT+10)])
		elif(choice == 5):
			# choice 5 is a 3 spike terrain without any water
			list_point.append([WIDTH*2/5,uniform(HEIGHT*2/5,HEIGHT*9/10)])
			list_point.append([WIDTH/2,uniform(list_point[1][1],list_point[1][1]+100)])
			list_point.append([WIDTH*4/5,list_point[1][1]])

		self.list_point = list_point

	def func(self,x):
		"""
		this function calculates f(x) such as f is a function that passes by all list_point
		we use lagrange polynome for this
		:param x: the x value
		:param list_point: the list of point to pass by
		:return: f(x)
		"""

		result = 0
		for terms in self.list_point:
			#as this is a multiplication, numerator and denominator shall be initialized to 1
			numerator = 1
			denominator = 1
			for factor in self.list_point:
				if terms != factor:
					numerator*=x-factor[0]
					denominator*=terms[0]-factor[0]
			result+=terms[1]*numerator/denominator

		return result


	def build(self):

		WIDTH = 1920
		HEIGHT = 1080

		terrain = Image.new(mode='RGBA',size=(WIDTH,HEIGHT),color=(0,0,0,0))

		for pixel_x in range(WIDTH):
			for pixel_y in range(HEIGHT):
					if(pixel_y>self.func(pixel_x)):
						terrain.putpixel((pixel_x,pixel_y),(0,0,0))
		terrain.save('./assets/terrain.png',format='png')


if __name__ == '__main__':
	pg.init()

	WIDTH = 1920
	HEIGHT = 1080

	window = pg.display.set_mode((WIDTH, HEIGHT))
	choice = randint(0,5)
	print(choice)
	builder = TerrainBuilder(window,choice);
	builder.build()
	to_blit = pg.image.load('terrain.png')
	window.blit(pg.image.load('background.png'),(0,0))
	window.blit(pg.image.load('sea.png'),(0,0))
	window.blit(to_blit,(0, 0))
	pg.display.update()
	input("press enter to finish")


#choice 2 down it all
#choice 3 down is too down
#choixce 4 down is too down up is too up