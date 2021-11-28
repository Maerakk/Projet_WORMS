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
        AppliConfig.ARROW_RIGHT_IMG = pg.image.load("assets/right_arrow.png")
        # AppliConfig.ARROW_UP_IMG = pg.image.load("assets/up_arrow.png")
        # AppliConfig.ARROW_DOWN_IMG = pg.image.load("assets/down_arrow.png")

        AppliConfig.LIST_TERRAIN_IMG = []
        for i in range(6):
            AppliConfig.LIST_TERRAIN_IMG.append(pg.image.load(f"assets/terrains_type/terrain{str(i)}.png"))
        AppliConfig.TERRAIN_CHOICE_IMG = pg.image.load("assets/stage_selection.png")

        AppliConfig.LIST_CAT_IMG = []
        for i in range(3):
            AppliConfig.LIST_CAT_IMG.append(pg.image.load(f"assets/cats/{str(i)}/standing_0.png"))
