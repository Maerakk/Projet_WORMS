from game_config import *

from abc import ABC, abstractmethod


class Projectile(ABC, pg.sprite.Sprite):
    def __init__(self, weapon, ground):
        # Sprite
        super().__init__()
        self.shootFinished = None
        self.is_shot = False

        self.image = None
        self.mask = None

        self.bounce = False

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

        # If the player press the shoot button (CTRL) we need to initiate some variables :

        if next_move.shoot and not self.weapon.is_shot:
            # If the player continues to press the button without any interruption (weapon.is_shot represent it)
            print("ok")
            self.weapon.force += -1
            self.x0 = self.weapon.rect.top
            self.y0 = self.weapon.rect.left

        # If the player drop the shot button then the weapon is charged and ready to shoot the projectile
        if not self.is_shot and self.weapon.is_shot:
            # First, before the projectile is thrown we need to initialize the variables
            # We tell the program that the shoot is shot
            self.is_shot = True

            # We give the projectile a force that is equal for x and y for the moment
            # TODO while the player is holding the shoot button they can press the left and right button to shoot where they want it to be shot
            if self.weapon.direction == self.weapon.RIGHT:
                self.fx = - self.weapon.force
                self.fy = self.weapon.force
            if self.weapon.direction == self.weapon.LEFT:
                self.fx = self.weapon.force
                self.fy = self.weapon.force
            # Speed
            # We give the projectile the correct speed that is equal to the force, given that the time derivative is equal to 0
            self.vx = self.fx
            self.vy = self.fy


        # if the shot has started and is not ended we draw the trajectories
        elif self.is_shot and not self.shootFinished:
            # For the vector V = (vx, vy, x, y) it will be added the time derivate + a vector
            # DT is the time derivate and the vector is (0,-g/m, vx, vy)
            # So it will be V + DT* [0,-g/m, vx, vy]
            # We decided to do all the variables one by one so we won't have any vector or array here

            # If the projectile is already thrown then the equation of its abscisse is the same (DT * 0 = 0)
            # The equation for its ordinate is its previous ordinate + the force given by the gravity and the time derivative
            # We decided to put a mass at 1 for every projectile

            # Next comment is a try for the friction
            # self.vx = self.vx - (GameConfig.DT * ((6 * self.R * GameConfig.PI)/self.mass) * self.vx)
            # self.vy = self.vy + (GameConfig.DT * (GameConfig.GRAVITY/self.mass + (((6 * self.R * GameConfig.PI)/self.mass) * self.vy)))

            self.vx = self.vx
            self.vy = self.vy + (GameConfig.DT * GameConfig.GRAVITY)


            # Position
            # We move the rectangle given that the new x and y are the vx and vy
            self.rect = self.rect.move(self.vx, self.vy)
            # If we would want to do the things right we could add a parameter that checks the gradient of the ground to add a multiplying factor according to its degree
            # TODO parameter to check the gradient of the ground

            # We check if the projectile as touch the ground
            if pg.sprite.collide_mask(self, self.ground):

                # If yes we put the projectile on the top of the ground at the same abscissa (to avoid the projectile IN the ground)
                self.rect.bottom = self.ground.builder.lagrange(self.rect.midbottom[0]) + 15

                if self.bounce :
                    # If the speed is higher than 5 then we do a bounce
                    # BOUNCE EXPLANATION :
                    # We juste take the same vector (vx and vy) that the projectile has when it arrives on the floor and take the symmetrical from the floor
                    # So if the vector v = (a, b) is the one of the projectile before the bounce v' = (a, -b) is the one after the bounce
                    # To create the effect of the energy taken by the bounce on the floor we apply a constant (k, the elasticity)
                    # So in reality the new vector is v' = k * (a, -b)
                    if abs(self.vy) > 5:

                        # We take 2 points that will be the middle of the projectile and another one 10 pixel apart the right of the projectile
                        first_point = self.ground.builder.lagrange(self.rect.midbottom[0])
                        second_point = self.ground.builder.lagrange(self.rect.right + 10)


                        if self.vx < 0:
                            # If the projectile goes to the right
                            if first_point > second_point:
                                # If the ground goes down then the projectile will be going on the right
                                self.fx = self.vx * self.k
                                self.fy = -self.vy * self.k
                            elif first_point < second_point:
                                # If the ground goes up then the projectile will be going on the left
                                self.fx = - self.vx * self.k
                                self.fy = -self.vy * self.k
                        if self.vx > 0:
                            # If the projectile goes to the left
                            if first_point > second_point:
                                # If the ground goes down then the projectile will be going on the left
                                self.fx = -self.vx * self.k
                                self.fy = -self.vy * self.k
                            elif first_point < second_point:
                                # If the ground goes up then the projectile will be going on the right
                                self.fx = self.vx * self.k
                                self.fy = -self.vy * self.k
                        elif first_point == second_point:
                            # If it is a flat ground then is stops
                            self.fx = 0
                            self.fy = 0
                        if self.on_floor():
                            # if the projectile is on the floor then  we give its speed the force that the ground has given to it after the bounce (fx and fy that have changed)
                            self.vx = self.fx
                            self.vy = self.fy
                        else:
                            # Else we apply the same scenario than before the first bounce with the gravity and the DT
                            self.vx = self.vx
                            self.vy = self.vy + (GameConfig.DT * GameConfig.GRAVITY)
                    else:
                        # If the speed of the projectile is too low we stop it from bouncing
                        self.shootFinished = True
                        print("finished")
                else :
                    self.shootFinished = True
                    self.ground.explode(self.rect.x,self.rect.y)
                    # pass
                    self.weapon.shot_end = True
        elif self.shootFinished:
            pass
        # Here it means that the projectile isn't on the screen but we still move it given the weapon position
        # so it can appears right on the weapon when the user press the shot button
        else:
            if self.weapon.direction == self.weapon.RIGHT:
                self.x0 = self.weapon.rect.right
            else:
                self.x0 = self.weapon.rect.left
            self.y0 = self.weapon.rect.top
            self.rect.x = self.x0
            self.rect.y = self.y0
