import pygame as pg

import game_config
from game_config import *
from projectile import *


class Weapon:

    def __init__(self, player,terrain):
        self.player = player
        self.terrain = terrain
        self.nb_usages = 0
        self.shootFinished = False
        self.projectile = Projectile(self.player,self,self.terrain)

    def advance_state(self, weapon_used):
        # Acceleration
        if not self.shootFinished:
            self.projectile.projectile_thrown(weapon_used)
