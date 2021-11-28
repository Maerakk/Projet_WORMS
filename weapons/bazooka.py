from weapon import *
from game_config import *
from random import randint
from projectiles import *


class Bazooka(Weapon):
    def __init__(self, player, ground):
        super().__init__(player, ground)
        number = randint(0, 1)
        self.projectile = BazookaProjectile(player, self, ground, number)
        self.image = GameConfig.BAZOOKA_IMG[randint(0, 1)]
        self.projectile.image = GameConfig.FISHES_IMG[randint(0, 1)]
        self.rect = pg.rect.Rect(self.player.rect.top,
                                 self.player.rect.left,
                                 GameConfig.BAZOOKA_W,
                                 GameConfig.BAZOOKA_H)
