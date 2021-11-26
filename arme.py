import pygame as pg

import game_config
from game_config import *
from projectile import *


class Arme:

    def __init__(self, player):
        self.image = GameConfig.BAT_IMG
        self.player = player

        # Vitesse
        self.vx = 0
        self.vy = 0

        self.coeff_vx = 2
        self.coeff_vy = 0.8

        self.rect = pg.Rect(player.rect.right,
                            GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H,
                            GameConfig.BAT_W,
                            GameConfig.BAT_H)

        self.nb_usages = 2
        self.shootFinished = False

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def not_thrown(self):
        return self.rect.top == GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H and self.rect.left == self.player.rect.right

    def on_floor(self):
        return self.rect.top == game_config.GameConfig.Y_PLATEFORM

    def advance_state(self, arme_thrown):
        # Acceleration

        if arme_thrown:
            projectile_thrown(self, self.not_thrown())
        if not self.shootFinished:
            projectile_thrown(self, self.not_thrown())
