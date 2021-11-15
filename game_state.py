import pygame as pg

class GameState:

    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))