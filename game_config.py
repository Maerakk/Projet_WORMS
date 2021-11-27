import pygame as pg

from appli_config import AppliConfig


class GameConfig:
    """
    Définis plusieurs variable nécessaire au bon fonctionnement du jeu afin de ne pas les redéfinir a chaque fois et éviter des erreurs
    Les dimensions de la fenetre, les couleurs, les images
    On notera que la définition des images se fait dans une fonction a part puisqu'elle doivent etre définis après l'initialisation de pygame
    """
    WINDOW_W = AppliConfig.WINDOW_W
    WINDOW_H = AppliConfig.WINDOW_H

    Y_PLATEFORM = 716

    PLAYER_W = 64
    PLAYER_H = 64

    DT = 1
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT

    FORCE_THROWN = -100

    #Jump
    GRAVITY = 9.81
    FORCE_JUMP = -80

    BAT_H = 32
    BAT_W = 32

    @staticmethod
    def init():
        AppliConfig.init()
        GameConfig.BACKGROUND_IMG = AppliConfig.BACKGROUND_IMG
        GameConfig.STANDING_IMG = pg.image.load('assets/standing.png')
        GameConfig.STANDING_MASK = pg.mask.from_surface(GameConfig.STANDING_IMG)
        GameConfig.BAT_IMG = pg.image.load('assets/bat1.png')
        GameConfig.BAT_MASK = pg.mask.from_surface(GameConfig.BAT_IMG)
