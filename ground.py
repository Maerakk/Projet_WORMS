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
        self.image = pg.image.load("assets/ground/ground.png")
        # creating mask from image for collision
        self.mask = pg.mask.from_surface(self.image)
        self.explosion = False
        self.explosion_x = 0
        self.explosion_y = 0
        self.explosion_frame = 0

    def draw(self, window):
        window.blit(self.image, (0, 0))
        if self.explosion:
            window.blit(GameConfig.EXPLOSION_IMG, (self.explosion_x, self.explosion_y-256/2))
            self.explosion_frame += 1
        if self.explosion_frame == GameConfig.NB_FRAME_EXPLOSION:
            self.explosion = False
            self.explosion_frame = 0

    def explode(self, x, y):
        self.explosion = True
        self.explosion_x = x
        self.explosion_y = y
