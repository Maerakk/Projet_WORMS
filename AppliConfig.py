import pygame as pg


class AppliConfig:

    """
    Définis plusieurs variable nécessaire au bon fonctionnement du jeu afin de ne pas les redéfinir a chaque fois et éviter des erreurs
    Les dimensions de la fenetre, les couleurs, les images
    On notera que la définition des images se fait dans une fonction a part puisqu'elle doivent etre définis après l'initialisation de pygame
    De plus, on notera la présence d'un fichier game_config ne concernant la configuration que pour la game screen
    """

    WINDOW_W = 1400
    WINDOW_H = 800
    DARK_YELLOW = (181, 145, 0)

    @staticmethod
    def init():
        AppliConfig.BACKGROUND_IMG = pg.image.load("assets/background.png")
        AppliConfig.ARROW_IMG = pg.image.load("assets/menu_arrow.png")