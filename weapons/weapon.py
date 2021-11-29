from abc import ABC, abstractmethod
import pygame as pg
from game_config import *


class Weapon(ABC, pg.sprite.Sprite):

    def __init__(self, player, terrain):
        super().__init__()
        self.player = player
        self.terrain = terrain
        self.nb_usages = 0
        self.projectile = None
        self.image = None
        self.rect = None
        self.RIGHT = self.player.RIGHT
        self.LEFT = self.player.LEFT
        self.direction = self.RIGHT
        self.force = GameConfig.FORCE_MIN
        self.is_shot = False
        self.is_shooting = False
        self.shot_end = False


    def draw(self, window):
        if self.player.direction != self.direction and self.player.direction != self.player.NONE:
            self.image = pg.transform.flip(self.image, True, False)
            self.direction = self.player.direction
        self.projectile.draw(window)
        window.blit(self.image, self.rect.topleft)

    def advance_state(self, next_move):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
        # We check of the user is pressing the shoot button
        if next_move.shoot:
            # If yes we put it in a variable
            self.is_shooting = True

        # If the player has pressed and is not pressing the key anymore then we put in a variable that ha has shot the projectile
        if self.is_shooting and not next_move.shoot:
            self.is_shot = True

        self.projectile.advance_state(next_move)
