from game_config import *
import numpy as np
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
        #Position
        self.x = self.x0
        self.y = self.y0
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
        self.R = 25

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
            self.weapon.force += -1
            self.x0 = self.weapon.rect.top
            self.y0 = self.weapon.rect.left
            self.x = self.x0
            self.y = self.y0

        # If the player drops the shot button then the weapon is charged and ready to shoot the projectile
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

            self.vx = self.vx
            self.vy = self.vy + (GameConfig.DT * GameConfig.GRAVITY)

            # Position
            # We move the rectangle given that the new x and y are the vx and vy
            old_rect = self.rect.copy()
            self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)
            # If we would want to do the things right we could add a parameter that checks the gradient of the ground to add a multiplycng factor according to its degree
            # TODO parameter to check the gradient of the ground

            # We check if the projectile as touch the ground
            if pg.sprite.collide_mask(self, self.ground):
                collisionx, collisiony = pg.sprite.collide_mask(self,self.ground)
                collisionx = collisionx + self.rect.left
                collisiony = collisiony + self.rect.top
                # print (collisionx)
                # print (collisiony)
                # If yes we put the projectile on the top of the ground at the same abscissa (to avoid the projectile IN the ground)
                self.rect.bottom = self.ground.builder.lagrange(self.rect.midbottom[0]) + 15
                if self.ground.type == 5:
                    if self.vy >5:
                        print (self.vx, self.vy)
                        self.vy = -self.vy * self.k
                        self.vx = self.vx * self.k
                        # self.fx = self.vx * self.k
                        # self.fy = self.vy * self.k
                        self.is_shot = True
                elif self.bounce:
                    # If the speed is higher than 5 then we do a bounce
                    # BOUNCE EXPLANATION :
                    # We juste take the same vector (vx and vy) that the projectile has when it arrives on the floor and take the symmetrical from the floor
                    # So if the vector v = (a, b) is the one of the projectile before the bounce v' = (a, -b) is the one after the bounce
                    # To create the effect of the energy taken by the bounce on the floor we apply a constant (k, the elasticity)
                    # So in reality the new vector is v' = k * (a, -b)




                    if abs(self.vy) > 5:
                        # We consider the impact point is the bottom middle of the projectile for the moment
                        # the impact point will be i (xc, yc)
                        # We take 2 points that will be at the same pixel apart from the middle of the projectile
                        # We will approach the equation of the tangent by a straight line that go through 2 points : a and b
                        # When we find it we will find the parallel line that goes through the middle point of the projectile
                        xa = collisionx - 2
                        ya = self.ground.builder.lagrange(xa)
                        xb = collisionx + 2
                        yb = self.ground.builder.lagrange(xb)
                        xc = collisionx
                        yc = collisiony


                        # THE TANGENT
                        # With a vector v = (-b,a), the equation of the tangent is " delta : a(x - xc) + b(y - yc) = 0"
                        # The vector v that is determined by the 2 points (a and b) is : v = (xb-xa, - (yb-ya))
                        v = np.array([[xb - xa], [yb - ya]])
                        b = - v[0][0]
                        a = v[1][0]
                        # So now we have the equation of the tangent with a = v[0] and b = v[1], t : a(x-xc) + b(y-yc) = 0

                        # NORMAL VECTOR OF THE TANGENT
                        # The normal vector of the tangent is u(a,b)
                        u = np.array([[a], [b]])
                        # So the equation of t' is t' : -b(x - xc) + a(y-yc) = 0

                        # THE VECTOR THAT ARRIVES TO THE GROUND
                        # We need to find the equation of the vector that arrives to the ground
                        # The vector is w = (self.vx, self.vy)
                        # If we take a point d from the straight line created by w the point here is to find and equation
                        # that as the symmetrical point of d from t'

                        # For the point d we can do : xd = -w + (xc,yc)
                        # So xd = xc - w[0] and yd = yc - w[1]
                        w = np.array([[self.vx], [self.vy]])
                        print(self.vx)
                        print(self.vy)
                        xd = xc - w[0][0] * 2
                        yd = yc - w[1][0] * 2

                        # We need to find w'
                        # We admit that w = (xd-xc, yd-yc)
                        #                 = alpha(a,b) + beta(-b,a)
                        #                 =  (alpha*a - beta*b, alpha*b + beta*a)
                        # So w' = alpha(a,b) - beta(-b,a)
                        alpha = 0
                        beta = 0
                        # RESOLVE THE EQUATION TO FIND ALPHA AND BETA
                        # We have a system of 2 equations here :
                        # { alpha * a - beta * b = xd - xc
                        # { beta*a + alpha * b) = yd - yc
                        # this is equal to the equation of matrices :
                        # (a -b) (alpha) = (xd-xc)
                        # (b a) (beta) = (yd - ya)
                        # If we divide by the matrix ( [[a,-b] [b,a]]) we will have the equation for the matrix ([[alpha][beta]])
                        # The opposite of this matrix is i / (a² * b²) :
                        #       Verification of the opposite of the matrix
                        #       1/(a² + b²) * [[a,b][-b, a]] * [[a,-b][b,a]]
                        #      = 1/(a² + b²) * [[a²+b², 0][0, a² + b²] = [[0,1][1,0]]
                        # So at the end, [[alpha][beta]] = 1/(a² + b²) * [[a,b][-b,a]] * [[xd - xc][yd - yc]]
                        alpha_beta = np.array([[alpha],[beta]])
                        first_matrix = np.array([[a,b],[-b,a]])
                        second_matrix = np.array([[xd-xc],[yd-yc]])
                        alpha_beta = (1/(pow(a,2) + pow(b,2))) * first_matrix * second_matrix

                        # w' = alpha(a,b) - beta(-b,a)
                        ab_matrix = np.array([[a],[b]])
                        minus_ba_matrix = np.array([[-b],[a]])
                        w_prime = (alpha_beta[0][0] * ab_matrix) - (alpha_beta[1][0] * minus_ba_matrix)
                            # print(w_prime[0][0])
                            # print(w_prime[1][0])
                        if ya != 0 and yb != 0:
                            # if ya > yb:
                            #     self.fx = -w_prime[0][0] * self.k
                            # else :
                            #     self.fx = w_prime[0][0] * self.k
                            self.fx = w_prime[0][0] * self.k
                            self.fy = - w_prime[1][0] * self.k
                            self.is_shot = True
                        # elif ya == yb:
                        #     # If it is a flat ground then is stops
                        #     self.fx = 0
                        #     self.fy = 0
                        # print (w)
                        # print (v)
                        if (v[0][0]-2 < w[0][0] and w[0][0] > v[0][0]+2) and (v[1][0]-2 < w[1][0] and w[1][0] > v[1][0]+2):
                            # print(v[0][0]-2)
                            # print(w[0][0])
                            # print(v[0][0]+2)
                            # print(v[1][0]-2)
                            # print(w[1][0])
                            # print(v[1][0]+2)
                            # print("f
                            # inish")
                            self.shootFinished = True
                            self.rect.bottom = self.ground.builder.lagrange(self.rect.midbottom[0]) + 15

                            self.ground.explode(self.rect.x, self.ground.builder.lagrange(self.rect.midbottom[0]) + 15)
                            self.weapon.shot_end = True

                        if self.on_floor():
                            # if the projectile is on the floor then  we give its speed the force that the ground has given to it after the bounce (fx and fy that have changed)
                            self.vx = self.fx
                            self.vy = self.fy
                            # self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)
                        else:
                            # Else we apply the same scenario than before the first bounce with the gravity and the DT
                            self.vx = self.vx
                            self.vy = self.vy + (GameConfig.DT * GameConfig.GRAVITY)
                            self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)
                    else:
                        # If the speed of the projectile is too low we stop it from bouncing
                        self.shootFinished = True
                        self.ground.explode(self.rect.x, self.rect.y)
                        # pass
                        self.weapon.shot_end = True
                else:
                    self.shootFinished = True
                    self.ground.explode(self.rect.x, self.rect.y) 
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

        # after all that, we look whether the projectile is over the window or not
        # if yes, we say that the shoot is finnished to the weapon
        if self.rect.top > GameConfig.WINDOW_H:
            self.shootFinished = True
            self.ground.explode(self.rect.x, self.rect.y)
            self.weapon.shot_end = True