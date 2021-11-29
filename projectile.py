import pygame as pg

from game_config import *
from move import *
from abc import ABC, abstractmethod


class Projectile(pg.sprite.Sprite):
    def __init__(self, weapon, ground):
        # Sprite
        super().__init__()
        self.shootFinished = None
        self.is_shot = False

        self.image = None
        self.mask = None

        self.ground = ground

        # Position t=0
        self.x0 = self.weapon.rect.right
        self.y0 = self.weapon.rect.top
        # Speed t=0
        self.vx = 0
        self.vy = 0

        # Coefficients
        self.coeff_vx = 0
        self.coeff_vy = 0

        # Creation of the rectangle that contains the projectile
        self.rect = pg.rect.Rect(self.x0, self.y0, 0, 0)

        # Variable of the projectile
        self.weapon = weapon
        self.mass = 0.0005
        self.R = 0.01

        self.fx = 0
        self.fy = 0

        # elasticity
        self.k = 0

    def draw(self, window):
        # we draw the projectile only if it's shot
        if self.is_shot:
            window.blit(self.image, self.rect.topleft)

    def not_thrown(self):
        return self.rect.top == self.y0 and self.rect.left == self.x0

    def on_floor(self):
        return pg.sprite.collide_mask(self, self.ground)

    def advance_state(self, next_move):

        # if the next move is to shoot and it wasnt shot before, we have to start the shot
        if next_move.shoot and not self.is_shot:
            self.x0 = self.weapon.rect.top
            self.y0 = self.weapon.rect.left

            self.is_shot = True

            self.fx = - GameConfig.FORCE_THROWN
            self.fy = GameConfig.FORCE_THROWN

            # Speed
            self.vx = self.fx
            self.vy = self.fy

        # if the shot has started and is not ended we draw the trajectories
        elif self.is_shot and not self.shootFinished :
            # If the projectile is already thrown then the equation of its abscisse is the same
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
            # If if would want to do the things right we could add a parameter that checks the gradient of the ground to add a multiplying factor according to its degree
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
                    self.shootFinished = True
        # else it means that the projectile isn't on the screen but we still move it given the weapon position
        else :
            if self.weapon.direction == self.weapon.RIGHT:
                self.x0 = self.weapon.rect.right
            else:
                self.x0 = self.weapon.rect.left
            self.y0 = self.weapon.rect.top
            self.rect.x = self.x0
            self.rect.y = self.y0