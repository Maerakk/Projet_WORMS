import pygame as pg
from game_config import *
from player import *
from weapon import *
from ground import Ground
from weapon import Weapon
from weapons import Bazooka
from weapons import Grenade
from weapons import Gun
from weapons import Sheep
from weapons import SheepControlled


class GameState:
    """
    Class that represent the state of the game at some point (player position etc. )
    """

    def __init__(self,ground_type):
        """
        During the initialisation
        We place 3 attributes that will change later
        The ground
        The player (will be changed for a list of players)
        The weapons (can be removed to be only player's attribute ?)
        """
        self.ground = Ground(ground_type)
        self.player = Player(200,self.ground)
        self.weapon = Weapon(self.player, self.ground)
        self.bazooka = Bazooka(self.player,self.ground)
        self.grenade = Grenade(self.player,self.ground)
        self.sheep = Sheep(self.player, self.ground)
        self.sheep_controlled = SheepControlled(self.player, self.ground)

    def draw(self, window):
        """
        Called to draw the state of the game
        Call every draw functions
        :param window: the window where it's gonna be drawn
        """
        # We pile the images so the background first
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        # Then water
        # Then the ground
        window.blit(self.ground.image, (0, 0))
        # Then the player
        self.player.draw(window)

    # We need an alone function to draw the weapons because they aren't always on screen
    def draw_shoot(self, window):
        self.weapon.projectile.draw(window)

    def draw_weapon(self, window,move):
        if move.weapon_grenade:
            self.grenade.draw(window)
        if move.weapon_bazooka:
            self.bazooka.draw(window)
        if move.weapon_sheep:
            self.sheep.draw(window)
        if move.weapon_sheep_controlled:
            self.sheep_controlled.draw(window)

    def advance_state(self, next_move, arme_thrown):
        """
        Advance state allows to calculate needed variables to make the game furthers
        This method call every others advance_state methods of all the objects
        :param next_move:
        :param arme_thrown:
        """
        self.player.advance_state(next_move)

