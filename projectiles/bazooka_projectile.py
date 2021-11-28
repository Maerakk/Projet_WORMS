from projectile import *
from random import randint
from game_config import *


class BazookaProjectile(Projectile):
    def __init__(self, player, weapon, ground, number):
        super().__init__(player, weapon, ground)
        self.player = player
        self.weapon = weapon
        self.ground = ground
        self.number = number
    def init(self):
        self.mass = 0.0005
        self.rect = pg.rect.Rect(self.weapon.rect.top,
                                 self.weapon.rect.left,
                                 GameConfig.FISH_W,
                                 GameConfig.FISH_H)
        self.image = GameConfig.FISHES_IMG[self.number]
        self.madk = GameConfig.FISHES_MASK[self.number]



