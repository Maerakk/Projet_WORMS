import pygame as pg

from AppliConfig import AppliConfig


class GameConfig:

    WINDOW_W = AppliConfig.WINDOW_W
    WINDOW_H = AppliConfig.WINDOW_H

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
        GameConfig.BACKGROUND_IMG = AppliConfig.BACKGROUND_IMG
        GameConfig.STANDING_IMG = pg.image.load('assets/standing.png')
        GameConfig.BAT_IMG = pg.image.load('assets/bat1.png')
