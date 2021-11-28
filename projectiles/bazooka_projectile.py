from projectile import *
from random import randint
from game_config import *


class BazookaProjectile(Projectile):
    def __init__(self, player, weapon, ground, number):
        super().__init__(player, weapon, ground)
        self.mass = 0.0005
        self.image = GameConfig.FISHES_IMG[number]



