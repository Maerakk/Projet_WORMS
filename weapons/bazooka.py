from game_config import *
from random import randint
from projectiles import *
from weapons.weapon import Weapon


class Bazooka(Weapon):
    def __init__(self, player, ground,style):
        super().__init__(player, ground)
        self.style = style
        self.image = GameConfig.BAZOOKA_IMG[self.style]
        self.rect = pg.rect.Rect(self.player.rect.top,
                                 self.player.rect.left,
                                 GameConfig.BAZOOKA_W,
                                 GameConfig.BAZOOKA_H)
        self.projectile = BazookaProjectile(self, ground, self.style)

    def draw(self, window):
        super().draw(window)

    def advance_state(self, next_move):
        super().advance_state(next_move)
