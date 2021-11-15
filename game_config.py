import pygame as pg


class GameConfig:
    WINDOW_H = 800
    WINDOW_W = 1000

    @staticmethod
    def init():
        GameConfig.BACKGROUND_IMG = pg.image.load('assets/samoyed.png')
