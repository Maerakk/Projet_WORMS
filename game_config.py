import pygame as pg


class GameConfig:
    WINDOW_H = 800
    WINDOW_W = 1400

    Y_PLATEFORM = 716

    PLAYER_W = 64
    PLAYER_H = 64

    DT = 0.7
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT

    FORCE_THROWN = -100

    #Jump
    GRAVITY = 9.81
    FORCE_JUMP = -100

    BAT_H = 32
    BAT_W = 32

    @staticmethod
    def init():
        GameConfig.BACKGROUND_IMG = pg.image.load('assets/samoyed.png')
        GameConfig.STANDING_IMG = pg.image.load('assets/standing.png')
        GameConfig.BAT_IMG = pg.image.load('assets/bat1.png')
