from projectile import *
from random import randint
from game_config import *


class BazookaProjectile(Projectile):
    def __init__(self, weapon, ground, style):
        self.weapon = weapon
        self.ground = ground
        super().__init__(weapon, ground)
        self.style = style
        self.mass = 0.0005
        self.rect = pg.rect.Rect(self.weapon.rect.top,
                                 self.weapon.rect.left,
                                 GameConfig.FISH_W,
                                 GameConfig.FISH_H)

        self.image = GameConfig.FISHES_IMG[self.style]
        self.mask = GameConfig.FISHES_MASK[self.style]



