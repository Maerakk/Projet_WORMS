import pygame as pg

from game_config import *
from move import *
from game_config import *


class Projectile(pg.sprite.Sprite):
    def __init__(self, player, arme, terrain):
        # Sprite
        self.sprite_count = 0
        super().__init__()

        self.image = GameConfig.BAT_IMG
        self.mask = GameConfig.BAT_MASK

        self.terrain = terrain

        # Position t=0
        self.x0 = 50
        self.y0 = 50
        # Speed t=0
        self.vx = 0
        self.vy = 0

        # Coefficients
        self.coeff_vx = 2
        self.coeff_vy = 0.8

        # Creation of the rectangle that contains the projectile
        self.rect = pg.Rect(self.x0,
                            self.y0,
                            GameConfig.BAT_W,
                            GameConfig.BAT_H)

        # Variable of the
        self.arme = arme

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def not_thrown(self):
        return self.rect.top == self.y0 and self.rect.left == self.x0

    def on_floor(self):
        return pg.sprite.collide_mask(self, self.terrain)

    def advance_state(self, arme_thrown):
        # Acceleration
        if not self.shootFinished:
            self.projectile_thrown(self, arme_thrown)

    def projectile_thrown(self, projectile_thrown):
        # Force of the projectile before it's thrown
        fx = 0
        fy = 0
        # If the projectile is thrown then its force is equals to the force it's thrown (it is the acceleration)
        if projectile_thrown:
            fy = GameConfig.FORCE_THROWN

        # Speed
        # If the projectile isn't thrown yet it's speed is equal to its acceleration * time derivative
        if self.not_thrown():
            self.vy = fy * GameConfig.DT * self.coeff_vy
            self.vx = fx * GameConfig.DT * self.coeff_vx
        else:
            # If the projectile is thrown then the equation of its abscissa is the same
            # The equation for its ordinate is its previous ordinate + the force given by the gravity and the time derivative
            self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT
            self.vx = fx + GameConfig.GRAVITY * GameConfig.DT * self.coeff_vx

        # Position
        x = self.rect.left
        vx_max = 200
        # vx_max = (arme.player.rect.left + x) / GameConfig.DT
        self.vx = min(self.vx, vx_max)

        y = self.rect.top
        vy_max = self.rect.top - y / GameConfig.DT
        # vy_max = (arme.player.rect.top - y) / GameConfig.DT
        # arme.vy = min(arme.vy, vy_max)
        if pg.sprite.collide_mask(self, self.terrain):
            self.arme.shootFinished = True
        # if self.on_floor():
        #     print("on floor")
        self.rect = self.rect.move(self.vx * GameConfig.DT / 10, self.vy * GameConfig.DT / 10)
