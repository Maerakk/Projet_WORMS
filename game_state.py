import pygame as pg
import random
from game_config import *
from player import *
from arme import *


class GameState:
    player = None
    arme = None

    def __init__(self):
        self.player = Player(200)
        self.arme = Arme(self.player)

    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))

    def advance_state(self, next_move,arme_thrown):
        self.player.advance_state(next_move)
        self.arme.advance_state(arme_thrown)

