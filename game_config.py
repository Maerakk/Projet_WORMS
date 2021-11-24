import pygame as pg


class GameConfig:
    WINDOW_H = 800
    WINDOW_W = 1000

    Y_PLATEFORM = 716

    PLAYER_W = 64
    PLAYER_H = 64


    @staticmethod
    def init():
        GameConfig.BACKGROUND_IMG = pg.image.load('assets/samoyed.png')
