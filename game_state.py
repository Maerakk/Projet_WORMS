import pygame as pg
from game_config import *
from player import *
from ground import Ground
from weapons import Bazooka
from weapons import Grenade
from weapons import Gun
from weapons import Mouse
from weapons import MouseControlled


class GameState:
    """
    Class that represent the state of the game at some point (player position etc. )
    """

    def __init__(self, ground_type, cat_type):
        """
        During the initialisation
        We place 3 attributes that will change later
        The ground
        The player (will be changed for a list of players)
        The weapons (can be removed to be only player's attribute ?)
        """
        self.ground = Ground(ground_type)
        self.player = [Player(GameConfig.WINDOW_W/10, self.ground, cat_type[0]), Player(GameConfig.WINDOW_W*9/10, self.ground,cat_type[1])]
        self.turn = 0
        self.frame_after_turn = 0

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
        self.ground.draw(window)

        # Then the player
        for player in self.player:
            player.draw(window)

    def advance_state(self, move):
        """
        Advance state allows to calculate needed variables to make the game furthers
        This method call every others advance_state methods of all the objects
        :param move:
        """
        self.ground.advance_state(self)
        self.player[self.turn].advance_state(move)
        if self.player[self.turn].has_shot:
            self.turn = (self.turn + 1) % 2
