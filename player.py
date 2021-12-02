import random

import pygame as pg
from game_config import GameConfig
from projectiles import Grenade
from weapons import *


class Player(pg.sprite.Sprite):
    """
    This class can represent a player
    (if there is multiple players for one user we will make child classes called "cat" or "character")
    """

    # CONSTANTES
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self, x, ground, cat_type):

        # as the player can choose his skin we have to make images part of itself
        # Player
        self.WALK_RIGHT_IMG = [
            pg.image.load(f"assets/cats/{str(cat_type)}/right_{str(i)}.png").convert_alpha()
            for i in range(1, 3)
        ]
        self.WALK_LEFT_IMG = [
            pg.image.load(f"assets/cats/{str(cat_type)}/left_{str(i)}.png").convert_alpha()
            for i in range(1, 3)
        ]
        self.STANDING_IMG = [
            pg.image.load(f"assets/cats/{str(cat_type)}/standing_{str(i)}.png").convert_alpha()
            for i in range(1, 3)
        ]

        self.WALK_RIGHT_MASKS = [
            pg.mask.from_surface(im) for im in self.WALK_RIGHT_IMG
        ]
        self.WALK_LEFT_MASKS = [
            pg.mask.from_surface(im) for im in self.WALK_LEFT_IMG
        ]
        self.STANDING_MASKS = [
            pg.mask.from_surface(im) for im in self.STANDING_IMG
        ]

        self.IMAGES = {
            Player.LEFT: self.WALK_LEFT_IMG,
            Player.RIGHT: self.WALK_RIGHT_IMG,
            Player.NONE: self.STANDING_IMG
        }

        self.MASKS = {
            Player.LEFT: self.WALK_LEFT_MASKS,
            Player.RIGHT: self.WALK_RIGHT_MASKS,
            Player.NONE: self.STANDING_MASKS
        }

        # Instantiation of the parent
        super().__init__()

        # Attributes
        # For the animations
        self.sprite_count = 0
        self.direction = Player.NONE

        # Image of the player
        self.image = self.IMAGES[self.direction][self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER]
        # Mask of the player (to manage collisions)
        self.mask = self.MASKS[self.direction][self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER]
        # The ground to manage collisions
        # We will need to put the ground somewhere else
        self.ground = ground

        y = self.ground.builder.lagrange(x) + 5
        # Location
        # We put the player on the coordinates x and y on the generate graph
        self.rect = pg.Rect(x,
                            y - GameConfig.PLAYER_H,
                            GameConfig.PLAYER_W,
                            GameConfig.PLAYER_H
                            )

        # Speed
        # At the beginning the player isn't moving
        self.vx = 0
        self.vy = 0

        # Weapons
        # the player start with no weapon in the hand
        self.weapon_available = [
            [Grenade(self, self.ground), Grenade(self, self.ground), Grenade(self, self.ground)],
            [Bazooka(self, self.ground, random.randint(0, 1)), Bazooka(self, self.ground, random.randint(0, 1)),
             Bazooka(self, self.ground, random.randint(0, 1)), Bazooka(self, self.ground, random.randint(0, 1))],
            [Mouse(self, self.ground)],
            [MouseControlled(self, self.ground)]
        ]
        self.current_weapon = None
        self.has_weapon = False
        self.has_shot = False

        # Life
        # the player starts with 100hp
        self.hp = 100

    def displayMessage(self, window, text, fontSize, x, y, color=GameConfig.BLACK):
        """
        this function displays
        :param window: in a window
        :param text: a text
        :param fontSize: of size fontSize
        :param x: at coordinates x
        :param y: y
        :param color: of color color (DARK_YELLOW by default)
        took from tp1
        """
        font = pg.font.Font('assets/BradBunR.ttf', fontSize)
        img = font.render(text, True, color)
        displayRect = img.get_rect()
        displayRect.center = (x, y)
        window.blit(img, displayRect)

    def draw(self, window):
        """
        function that draws the player
        :param window: window where the player will be drawn
        """
        window.blit(self.image, self.rect.topleft)
        self.displayMessage(window, f"{str(self.hp)} hp", 20, self.rect.left + GameConfig.PLAYER_W / 2,
                            self.rect.bottom + 5)
        # we draw the weapon only if the player has it in hand
        if self.has_weapon:
            self.current_weapon.draw(window)

    def on_ground(self):
        """
        function testing is the player is touching the ground or not
        :return: true if the player's touching the ground, false otherwise
        """
        # we use the function collide_mask allowing use masks and entities
        return pg.sprite.collide_mask(self, self.ground)

    def advance_state(self, next_move):
        """
        advance state  allows to make calculations to make the player move
        the calculations consist in searching the next position of the player depending on its initial position and
        vectors imposed on him
        :param next_move: the move choose by the user
        """
        self.has_shot = False
        # ~~~~~~~~~~~~~~~~~~~~~Weapon~~~~~~~~~~~~~~~~~~~~~
        # if the player clicks on a key associated to weapon
        if next_move.weapon:
            # if he has a weapon and this weapon is of the same type as the one he called then we get rid of his weapon
            if self.has_weapon and (
                    (next_move.weapon_grenade and isinstance(self.current_weapon, Grenade)) or \
                    (next_move.weapon_bazooka and isinstance(self.current_weapon, Bazooka)) or \
                    (next_move.weapon_sheep and isinstance(self.current_weapon, Mouse)) or \
                    (next_move.weapon_sheep_controled and isinstance(self.current_weapon, Grenade))
                                    ):
                self.current_weapon = None
                self.has_weapon = False
            # else we simply give him the weapon he wanted
            else:
                try:
                    if next_move.weapon_grenade:
                        self.current_weapon = random.choice(self.weapon_available[0])
                    if next_move.weapon_bazooka:
                        self.current_weapon = random.choice(self.weapon_available[1])
                    if next_move.weapon_sheep:
                        self.current_weapon = random.choice(self.weapon_available[2])
                    if next_move.weapon_sheep_controlled:
                        self.current_weapon = random.choice(self.weapon_available[3])
                    self.has_weapon = True
                # if there is an index error it means that the player doesnt have this weapon anymor so we simlply
                # get rid of it
                except IndexError:
                    self.current_weapon = None
                    self.has_shot = True
        # if he has a weapon, we have to wall it's advance_state method
        if self.has_weapon:
            self.current_weapon.advance_state(next_move)
            # and if the shot ended, we have to get rid of the weapon
            if self.current_weapon.shot_end:
                if isinstance(self.current_weapon, Grenade):
                    self.weapon_available[0].remove(self.current_weapon)
                if isinstance(self.current_weapon, Bazooka):
                    self.weapon_available[1].remove(self.current_weapon)
                if isinstance(self.current_weapon, Mouse):
                    self.weapon_available[2].remove(self.current_weapon)
                if isinstance(self.current_weapon, MouseControlled):
                    self.weapon_available[3].remove(self.current_weapon)
                self.current_weapon = None
                self.has_weapon = False
                self.has_shot = True
        else:
            # we authorise movement only if the player doesnt have a weapon
            # ~~~~~~~~~~~~~~~~~~~~~DÉPLACEMENT~~~~~~~~~~~~~~~~~~~~~

            # Acceleration de base a 0
            fx = 0
            fy = 0
            # Then the acceleration is handled depending next_move
            if next_move.left:
                fx = GameConfig.FORCE_LEFT
            if next_move.right:
                fx = GameConfig.FORCE_RIGHT
            if next_move.jump:
                fy = GameConfig.FORCE_JUMP

            # Basic speed at dt/dx (acceleration)
            self.vx = fx * GameConfig.DT
            # By default we imagine that the player is going down (gravity is always applied on him)
            # If he's touching the ground we remove the gravity vector
            # it avoid creating bugs like the "bounce" one making frenetically bounce the player on the ground
            self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT

            # Position, a lot of testing is done to find the right value
            # x is the left of the rectangle of the player
            x = self.rect.left
            # We define the max and min speeds on x
            vx_min = -x / GameConfig.DT
            vx_max = (GameConfig.WINDOW_W - GameConfig.PLAYER_W - x) / GameConfig.DT
            # And we find the variable :
            # either min or max if the asked value is out of the bounds
            # either the asked value
            self.vx = min(self.vx, vx_max)
            self.vx = max(self.vx, vx_min)

            # We move the rectangle with the speed found (and the time derivative)
            self.rect = self.rect.move(self.vx * GameConfig.DT / 2, self.vy * GameConfig.DT)
            # We look if its new position is touching the ground or not
            if self.on_ground():
                # If it is we check if the player is not inside the ground
                # +5 is to avoid false collisions
                self.rect.bottom = self.ground.builder.lagrange(self.rect.midbottom[0]) + 5
                # And we apply the force (fy) done by the user on the player
                # This force can be 0 or GameConfig.FORCE_JUMP if the player is jumping
                self.vy = fy * GameConfig.DT / 2  # We want it to be less speed so we divide it by 2
                # We move the rectangle one last time
                self.rect = self.rect

        # ~~~~~~~~~~~~~~~~~~~~~Sprite~~~~~~~~~~~~~~~~~~~~~
        if next_move.left:
            self.direction = Player.LEFT
        elif next_move.right:
            self.direction = Player.RIGHT
        else:
            self.direction = Player.NONE

        self.sprite_count += 1
        if self.sprite_count >= GameConfig.NB_SPRITE_FRAME_PLAYER * len(self.IMAGES[self.direction]):
            self.sprite_count = 0
        self.image = self.IMAGES[self.direction][
            self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER
            ]
        self.mask = self.MASKS[self.direction][
            self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER
            ]

        # a little delay so there is no missclick
        pg.time.delay(20)


    def loose_life(self, explosion):
        if pg.sprite.collide_mask(self, explosion):
            print(20 // (explosion.sprite_count + 1))
            self.hp -= 20 // (explosion.sprite_count + 1)
