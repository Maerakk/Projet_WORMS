import pygame as pg
import random
from game_config import *
from player import *

class GameState:

    def draw(self, window):
        self.player = Player(20)

        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))

    def advance_state(self, next_move):
        self.player.advance_state(next_move)
