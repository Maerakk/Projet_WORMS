import pygame as pg

import game_config
from game_config import *
from projectile import *


class Arme:

    def __init__(self, player,terrain):
        self.player = player
        self.terrain = terrain
        # Vitesse

        self.nb_usages = 2
        self.shootFinished = False
        self.projectile = Projectile(self.player,self,self.terrain)

    def advance_state(self, arme_thrown):
        # Acceleration
        if not self.shootFinished:
            self.projectile.projectile_thrown(self)
