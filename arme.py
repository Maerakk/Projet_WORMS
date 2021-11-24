import pygame as pg
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
                            player.rect.top,
                            GameConfig.BAT_W,
                            GameConfig.BAT_H)

        self.nb_usages = 2

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def not_thrown(self):
        return self.rect.top == self.player.rect.top

    def advance_state(self, arme_thrown):
        # Acceleration
        if arme_thrown and self.nb_usages != 0:
            print("ok")
            projectile_thrown(self, arme_thrown)
            self.nb_usages -= 1
