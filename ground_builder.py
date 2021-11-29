from PIL import Image
from random import uniform, randint
import pygame as pg

from game_config import GameConfig


class GroundBuilder:

	def __init__(self, terrain_type):
		list_point = []

		if terrain_type <= 2:
			# all choice under 2 have left and right border in the sea
			# adding down left corner point
			list_point.append([0, uniform(GameConfig.WINDOW_H, GameConfig.WINDOW_H + 100)])
			# adding down right corner point
			list_point.append([GameConfig.WINDOW_W, uniform(GameConfig.WINDOW_H, GameConfig.WINDOW_H + 100)])
		else:
			# all choice over 2 have left and right border above the sea
			list_point.append([0, uniform(GameConfig.WINDOW_H * 3 / 5, GameConfig.WINDOW_H * 9 / 10)])
			list_point.append([GameConfig.WINDOW_W, uniform(GameConfig.WINDOW_H * 3 / 5, GameConfig.WINDOW_H * 9 / 10)])

		if terrain_type == 0:
			# choice 0 is a simple dome
			# adding one point somewhere in the middle to have a n=2 polynomial
			list_point.append([GameConfig.WINDOW_W / 2, uniform(GameConfig.WINDOW_H / 4, (GameConfig.WINDOW_H * 9) / 10)])
		elif terrain_type == 1:
			# choice 1 is a 2 spike terrain with water in the middle and on the sides
			list_point.append([GameConfig.WINDOW_W / 4, uniform(GameConfig.WINDOW_H * 2 / 5, GameConfig.WINDOW_H / 2)])
			list_point.append([GameConfig.WINDOW_W / 2, uniform(GameConfig.WINDOW_H, GameConfig.WINDOW_H + 50)])
			list_point.append([GameConfig.WINDOW_W * 3 / 4, uniform(GameConfig.WINDOW_H * 2 / 5, GameConfig.WINDOW_H / 2)])
		elif terrain_type == 2:
			# choice 2 is a two spike terrain with no water in the middle but water on the sides
			list_point.append([GameConfig.WINDOW_W / 4, uniform(GameConfig.WINDOW_H / 4, GameConfig.WINDOW_H / 2)])
			list_point.append([GameConfig.WINDOW_W / 2, uniform(GameConfig.WINDOW_H * 2 / 5, GameConfig.WINDOW_H * 9 / 10)])
			list_point.append([GameConfig.WINDOW_W * 3 / 4, uniform(GameConfig.WINDOW_H / 4, GameConfig.WINDOW_H / 2)])
		elif terrain_type == 3:
			# choice 3 is an inverted dome
			list_point.append([GameConfig.WINDOW_W / 2, uniform(GameConfig.WINDOW_H, GameConfig.WINDOW_H + 50)])
		elif terrain_type == 4:
			# choice 4 is a 3 spike terrain with water between the spikes but not on the sides
			list_point.append([GameConfig.WINDOW_W / 4, GameConfig.WINDOW_H])
			list_point.append([GameConfig.WINDOW_W / 2, uniform(GameConfig.WINDOW_H / 4, GameConfig.WINDOW_H / 2)])
			list_point.append([GameConfig.WINDOW_W * 3 / 4, uniform(GameConfig.WINDOW_H, GameConfig.WINDOW_H + 10)])
		elif terrain_type == 5:
			# choice 5 is a 3 spike terrain without any water
			list_point.append([GameConfig.WINDOW_W * 2 / 5, uniform(GameConfig.WINDOW_H * 2 / 5, GameConfig.WINDOW_H * 9 / 10)])
			list_point.append([GameConfig.WINDOW_W / 2, uniform(list_point[1][1], list_point[1][1] + 100)])
			list_point.append([GameConfig.WINDOW_W * 4 / 5, list_point[1][1]])

		self.list_point = list_point

	def lagrange(self, x):
		"""
		this function calculates f(x) such as f is a function that passes by all list_point
		we use lagrange polynomial for this
		:param x: the x value
		:return: f(x)
		"""

		result = 0
		for terms in self.list_point:
			# as this is a multiplication, numerator and denominator shall be initialized to 1
			numerator = 1
			denominator = 1
			for factor in self.list_point:
				if terms != factor:
					numerator *= x - factor[0]
					denominator *= terms[0] - factor[0]
			result += terms[1] * numerator / denominator

		return result

	def build(self):

		# we are going to build a mask to put on top of a dirt and a grass image to construct the ground
		mask_grass = Image.new(mode='RGBA', size=(GameConfig.WINDOW_W, GameConfig.WINDOW_H), color=(0, 0, 0, 0))
		mask_dirt = Image.new(mode='RGBA', size=(GameConfig.WINDOW_W, GameConfig.WINDOW_H), color=(0, 0, 0, 0))
		# this mask is a graph constructed from the lagrange func
		# we will color each pixel one by one whether or not they are under the graph
		for pixel_x in range(GameConfig.WINDOW_W):
			# as we travel from columns to columns, we can generate the graph for each column instead of for each pixel
			y_graph = self.lagrange(pixel_x)
			for pixel_y in range(GameConfig.WINDOW_H):
				# as the positives are going towards the bottom we look if pixel_y is greater than y_graph
				if pixel_y > y_graph:
					mask_grass.putpixel((pixel_x, pixel_y), (255, 255, 255))
				if pixel_y > y_graph+10:
					mask_dirt.putpixel((pixel_x, pixel_y), (255, 255, 255))

		# we create a new image which will be the final ground
		ground = Image.new(mode='RGBA', size=(GameConfig.WINDOW_W, GameConfig.WINDOW_H), color=(0, 0, 0, 0))

		# then we create the grass py pasting a grass pictures and applying the grass mask
		grass = Image.open("assets/ground/grass.png")
		ground.paste(grass, (0, 0), mask_grass)

		# and create the dirt the same way
		dirt = Image.open("assets/ground/dirt.png")
		ground.paste(dirt, (0, 0), mask_dirt)

		# finally we save the image
		ground.save('./assets/ground/ground.png', format='png')


if __name__ == '__main__':
	pg.init()
	GameConfig.init()

	WIDTH = GameConfig.WINDOW_W
	HEIGHT = GameConfig.WINDOW_H

	window = pg.display.set_mode((WIDTH, HEIGHT))
	choice = randint(0, 5)
	print(choice)
	builder = GroundBuilder(choice);
	builder.build()
	to_blit = pg.image.load('assets/ground/ground.png')
	window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
	window.blit(to_blit, (0, 0))
	pg.display.update()
	input("press enter to finish")

# choice 2 down it all
# choice 3 down is too down
# choixce 4 down is too down up is too up
