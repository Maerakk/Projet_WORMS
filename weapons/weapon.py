import pygame as pg

import game_config
from game_config import *
from projectile import *


class Weapon:

    def __init__(self, player, terrain):
        self.player = player
        self.terrain = terrain
        self.nb_usages = 0
        self.shootFinished = False
        self.projectile = None
        self.image = None
        self.rect = None

    def draw(self, window):

        window.blit(self.image, self.rect.topleft)

    def advance_state(self, weapon_used):
        # Acceleration
        if not self.shootFinished:
            self.projectile.projectile_thrown(weapon_used)
            # to place in weapon
        if next_move.shoot:
            self.projectile.x0 = self.game_state.player.rect.top
            self.projectile.y0 = self.game_state.player.rect.left
            self.draw_shoot(window)
