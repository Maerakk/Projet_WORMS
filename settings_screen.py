import pygame as pg

from appli_config import AppliConfig


class SettingScreen:
    """
    Cette classe représente la fenetre de choix avant le jeu
    6 variables staiques représentants les valeurs associés aux choix des terrains
    """

    TERRAIN0 = 0
    TERRAIN1 = 1
    TERRAIN2 = 2
    TERRAIN3 = 3
    TERRAIN4 = 4
    TERRAIN5 = 5

    def __init__(self):
        """
        lors de l'instanciation on met le choix a TERRAIN1
        """
        self.terrain_choice = SettingScreen.TERRAIN1


