import pygame as pg

from appli_config import AppliConfig


class GameConfig:
    """
    Define several variables or constants needed for the proper functioning of the game so we do not need to define them
    everytime we use them and void errors
    The definition of the images is done in a function because they only need to be defined after the initialisation of
    pygame
    """
    WINDOW_W = AppliConfig.WINDOW_W
    WINDOW_H = AppliConfig.WINDOW_H

    Y_PLATEFORM = 716

    PLAYER_W = 64
    PLAYER_H = 64

    DT = 1
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT

    FORCE_THROWN = -5

    #Jump
    GRAVITY = 9.81
    FORCE_JUMP = -80

    BAT_H = 32
    BAT_W = 32

    PI = 3.14

    @staticmethod
    def init():
        # Initialisations of all the images needed
        AppliConfig.init()
        #Background
        GameConfig.BACKGROUND_IMG = AppliConfig.BACKGROUND_IMG

        # Players
        GameConfig.STANDING_IMG = pg.image.load('assets/standing.png')
        GameConfig.STANDING_MASK = pg.mask.from_surface(GameConfig.STANDING_IMG)
        #Weapons
        GameConfig.BAT_IMG = pg.image.load('assets/bat1.png')
        GameConfig.BAT_MASK = pg.mask.from_surface(GameConfig.BAT_IMG)

        GameConfig.FISH_1_IMG = pg.image.load('assets/fish_1.png')
        GameConfig.FISH_1_MASK = pg.mask.from_surface(GameConfig.FISH_1_IMG)
        GameConfig.FISH_2_IMG = pg.image.load('assets/fish_2.png')
        GameConfig.FISH_2_MASK = pg.mask.from_surface(GameConfig.FISH_2_IMG)

