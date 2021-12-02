from game_config import GameConfig
from weapons.weapon import Weapon
from projectiles.grenade import GrenadeProjectile
import pygame as pg


class Grenade(Weapon):

    def __init__(self, player, ground, style):
        super().__init__(player, ground)
        self.style = style
        self.image = GameConfig.GRENADE_IMG[self.style]
        self.rect = pg.rect.Rect(self.player.rect.top,
                                 self.player.rect.left,
                                 GameConfig.GRENADE_W,
                                 GameConfig.GRENADE_H)
        self.projectile = GrenadeProjectile(self, ground, self.style)

    def draw(self, window):
        super().draw(window)

    def advance_state(self, next_move):
        super().advance_state(next_move)
