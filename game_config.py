import pygame as pg


class GameConfig:
    WINDOW_H = 800
    WINDOW_W = 1000

    Y_PLATEFORM = 716

    PLAYER_W = 64
    PLAYER_H = 64

    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT

    #Jump
    GRAVITY = 9.81
    FORCE_JUMP = -100


    @staticmethod
    def init():
        GameConfig.BACKGROUND_IMG = pg.image.load('assets/samoyed.png')
        GameConfig.STANDING_IMG = pg.image.load('assets/standing.png')
