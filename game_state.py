import pygame as pg
from game_config import *
from player import *
from weapon import *
from ground import Terrain


class GameState:
    """
    Class that represent the state of the game at some point (player position etc.)
    """

    def __init__(self):
        """
        During the initialisation
        We place 3 attributes that will change later
        The ground
        The player (will be changed for a list of players)
        The weapons (can be removed to be only player's attribute ?)
        """
        self.ground = Terrain()
        self.player = Player(200, self.ground)
        self.arme = Weapon(self.player, self.ground)

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
        self.arme.projectile.draw(window)

    def advance_state(self, next_move, arme_thrown):
        """
        Advance state allows to calculate needed to make the game furthers
        This method call every others advance_state methods of all the objects
        :param next_move:
        :param arme_thrown:
        """
        self.player.advance_state(next_move)
        self.arme.advance_state(arme_thrown)
