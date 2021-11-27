from random import randint

import pygame as pg

from game_config import GameConfig
from ground_builder import TerrainBuilder


class Terrain(pg.sprite.Sprite):
    """
    cette classe définit un terrain et fait appel a un TerrainBuilder pour etre construite
    elle hérite de la classe Sprite afin de gérer les collisions
    """
    def __init__(self):
        # on initialise le parent
        super().__init__()
        # on crée le réctangle (toute la fenetre)
        self.rect = (0,0,GameConfig.WINDOW_W,GameConfig.WINDOW_H)
        # on construit le terrain en fonction du mode choisi (aléatoire pour l'instant)
        self.builder = TerrainBuilder(randint(0,5))
        self.builder.build()
        # on load l'image et le mask pour les collisions
        self.image = pg.image.load("assets/terrain.png")
        self.mask = pg.mask.from_surface(self.image)
