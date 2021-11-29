from random import randint

import pygame as pg

from game_config import GameConfig
from ground_builder import GroundBuilder


class Ground(pg.sprite.Sprite):
    """
    this class defines a ground and calls a GroundBuilder to be built
    it inherits from the Sprite class to generate mask and compute collisions
    """

    def __init__(self, ground_type):
        # parents initiation
        super().__init__()
        # rect creation (the whole window)
        self.rect = (0, 0, GameConfig.WINDOW_W, GameConfig.WINDOW_H)
        # building the ground given a ground_type
        self.builder = GroundBuilder(ground_type)
        self.builder.build()
        # loading the image and storing it
        self.image = pg.image.load("assets/ground.png")
        # creating mask from image for collision
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (0, 0))
