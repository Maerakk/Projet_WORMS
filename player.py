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

    @staticmethod
    def init_sprites():

        Player.IMAGES = {
            Player.LEFT: GameConfig.WALK_LEFT_IMG,
            Player.RIGHT: GameConfig.WALK_RIGHT_IMG,
            Player.NONE: GameConfig.STANDING_IMG
        }

        Player.MASKS = {
            Player.LEFT: GameConfig.WALK_LEFT_MASKS,
            Player.RIGHT: GameConfig.WALK_RIGHT_MASKS,
            Player.NONE: GameConfig.STANDING_MASKS
        }

    def __init__(self, x, ground):

        # Instantiation of the parent
        super().__init__()

        # Attributes
        # For the animations
        self.sprite_count = 0
        self.direction = Player.NONE

        # Image of the player
        self.image = Player.IMAGES[self.direction][self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER]
        # Mask of the player (to manage collisions)
        self.mask = Player.MASKS[self.direction][self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER]
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
            [Bazooka(self, self.ground, random.randint(0, 1)), Bazooka(self, self.ground, random.randint(0, 1))],
            [Mouse(self, self.ground)],
            [MouseControlled(self, self.ground)]
        ]
        self.current_weapon = None
        self.has_weapon = False


    def draw(self, window):
        """
        function that draws the player
        :param window: window where the player will be drawn
        """
        window.blit(self.image, self.rect.topleft)
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
            self.rect = self.rect.move(0, self.vy)

        # ~~~~~~~~~~~~~~~~~~~~~Sprite~~~~~~~~~~~~~~~~~~~~~
        if next_move.left:
            self.direction = Player.LEFT
        elif next_move.right:
            self.direction = Player.RIGHT
        else:
            self.direction = Player.NONE

        self.sprite_count += 1
        if self.sprite_count >= GameConfig.NB_SPRITE_FRAME_PLAYER * len(Player.IMAGES[self.direction]):
            self.sprite_count = 0
        self.image = Player.IMAGES[self.direction][
            self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER
            ]
        self.mask = Player.MASKS[self.direction][
            self.sprite_count // GameConfig.NB_SPRITE_FRAME_PLAYER
            ]

        # ~~~~~~~~~~~~~~~~~~~~~Weapon~~~~~~~~~~~~~~~~~~~~~

        if next_move.weapon:
            if next_move.weapon_grenade:
                self.current_weapon = random.choice(self.weapon_available[0])
            if next_move.weapon_bazooka:
                self.current_weapon = random.choice(self.weapon_available[1])
            if next_move.weapon_sheep:
                self.current_weapon = random.choice(self.weapon_available[2])
            if next_move.weapon_sheep_controlled:
                self.current_weapon = random.choice(self.weapon_available[3])
            self.has_weapon = True
        if self.has_weapon:
            self.current_weapon.advance_state(next_move)
