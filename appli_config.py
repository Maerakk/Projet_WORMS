import pygame as pg


class AppliConfig:

    """
    Define several variables or constants needed for the proper functioning of the game so we do not need to define them
    everytime we use them and void errors
    The definition of the images is done in a function because they only need to be defined after the initialisation of
    pygame
    """

    WINDOW_W = 1400
    WINDOW_H = 800
    DARK_YELLOW = (181, 145, 0)

    @staticmethod
    def init():
        AppliConfig.BACKGROUND_IMG = pg.image.load("assets/background.png")
        AppliConfig.ARROW_IMG = pg.image.load("assets/menu_arrow.png")