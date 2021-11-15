import pygame as pg
from game_config import *

class GameState:

    def draw(self, window):

        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))