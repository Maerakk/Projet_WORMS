import pygame as pg

from game_config import *
from move import *
from game_config import *
from game_state import *


class Projectile(pg.sprite.Sprite):
    def __init__(self, player, weapon, ground):
        # Sprite
        self.sprite_count = 0
        super().__init__()
        self.shootFinished = None

        self.image = GameConfig.BAT_IMG
        self.mask = GameConfig.BAT_MASK

        self.ground = ground

        # Position t=0
        self.x0 = player.rect.top
        self.y0 = player.rect.left
        # Speed t=0
        self.vx = 0
        self.vy = 0

        # Coefficients
        self.coeff_vx = 0
        self.coeff_vy = 0

        # Creation of the rectangle that contains the projectile
        self.rect = pg.rect.Rect(0,0,0,0)

        # Variable of the projectile
        self.weapon = weapon
        self.mass = 0.0005
        self.R = 0.01

        self.fx = 0
        self.fy = 0

        # elasticity
        self.k = 0

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def not_thrown(self):
        return self.rect.top == self.y0 and self.rect.left == self.x0

    def on_floor(self):
        return pg.sprite.collide_mask(self, self.ground)

    def advance_state(self, weapon_has_shoot):
        # Acceleration
        if not self.weapon.shootFinished:
            self.projectile_thrown(weapon_has_shoot)

    def projectile_thrown(self, projectile_thrown):
        # If the projectile is thrown then its force is equals to the force it's thrown (it is the acceleration)
        if projectile_thrown:
            self.fx = - GameConfig.FORCE_THROWN
            self.fy = GameConfig.FORCE_THROWN

        # Speed
        # If the projectile isn't thrown yet it's speed is equal to its acceleration * time derivative
        if self.not_thrown():
            self.vx = self.fx
            self.vy = self.fy
        else:
            # If the projectile is thrown then the equation of its abscissa is the same
            # The equation for its ordinate is its previous ordinate + the force given by the gravity and the time derivative
            # self.vx = self.vx - (GameConfig.DT * ((6 * self.R * GameConfig.PI)/self.mass) * self.vx)
            # self.vy = self.vy + (GameConfig.DT * (GameConfig.GRAVITY/self.mass + (((6 * self.R * GameConfig.PI)/self.mass) * self.vy)))
            self.vx = self.vx
            self.vy = self.vy + (GameConfig.DT * GameConfig.GRAVITY)
        # Position
        # x = self.rect.left
        #
        # y = self.rect.top
        # vy_max = self.rect.top - y / GameConfig.DT
        # vy_max = (arme.player.rect.top - y) / GameConfig.DT
        # arme.vy = min(arme.vy, vy_max)
        # if pg.sprite.collide_mask(self, self.ground):
        #     self.weapon.shootFinished = True
        # if self.on_floor():
        #     print("on floor")
        self.rect = self.rect.move(self.vx, self.vy)
        # If if would wand to do the things right we could add a parameter that checks the gradient of the ground to add a multiplying factor according to its degree
        if pg.sprite.collide_mask(self, self.ground):
            self.rect.bottom = self.ground.builder.lagrange(self.rect.midbottom[0]) + 15
            if abs(self.vy) > 5:
                first_point = self.ground.builder.lagrange(self.rect.midbottom[0])
                second_point = self.ground.builder.lagrange(self.rect.right + 10)
                if self.vx < 0:
                    if first_point > second_point:
                        self.fx = self.vx * self.k
                        self.fy = -self.vy * self.k
                    elif first_point < second_point:
                        self.fx = - self.vx * self.k
                        self.fy = -self.vy * self.k
                if self.vx > 0:
                    if first_point > second_point:
                        self.fx = -self.vx * self.k
                        self.fy = -self.vy * self.k
                    elif first_point < second_point:
                        self.fx = self.vx * self.k
                        self.fy = -self.vy * self.k
                elif first_point == second_point:
                    self.fx = 0
                    self.fy = 0
                if self.on_floor():
                    self.vx = self.fx
                    self.vy = self.fy
                else:
                    self.vx = self.vx
                    self.vy = self.vy + (GameConfig.DT * GameConfig.GRAVITY)
            else:
                self.weapon.shootFinished = True
