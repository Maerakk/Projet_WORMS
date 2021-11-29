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

    # Color
    BLACK = (0,0,0)
    DARK_YELLOW = AppliConfig.DARK_YELLOW

    PLAYER_W = 47
    PLAYER_H = 47
    NB_SPRITE_FRAME_PLAYER = 2

    DT = 1
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT

    FORCE_MIN = -10
    FORCE_MAX = -60

    # Jump
    GRAVITY = 9.81
    FORCE_JUMP = -80

    BAT_H = 32
    BAT_W = 32

    PI = 3.14

    # Weapons
    BAZOOKA_H = 23
    BAZOOKA_W = 66

    FISH_H = 18
    FISH_W = 38

    # Explosion
    EXPLOSION_W = 256
    EXPLOSION_H = 256
    NB_SPRITE_FRAME_EXPLOSION = 5

    @staticmethod
    def init():
        # Initialisations of all the images needed
        AppliConfig.init()
        # Background
        GameConfig.BACKGROUND_IMG = AppliConfig.BACKGROUND_IMG



        # Weapons

        # Bazooka Weapon
        GameConfig.BAZOOKA_IMG = []
        GameConfig.BAZOOKA_IMG.append(pg.image.load("assets/weapons/bazooka_1.png"))
        GameConfig.BAZOOKA_IMG.append(pg.image.load("assets/weapons/bazooka_2.png"))
        GameConfig.BAZOOKA_MASK = []
        GameConfig.BAZOOKA_MASK.append(pg.mask.from_surface(GameConfig.BAZOOKA_IMG[0]))
        GameConfig.BAZOOKA_MASK.append(pg.mask.from_surface(GameConfig.BAZOOKA_IMG[1]))

        # Bazooka Projectiles
        GameConfig.FISHES_IMG = []
        GameConfig.FISHES_MASK = []
        GameConfig.FISHES_IMG.append(pg.image.load('assets/weapons/fish_1.png'))
        GameConfig.FISHES_IMG.append(pg.image.load('assets/weapons/fish_2.png'))
        GameConfig.FISHES_MASK.append(pg.mask.from_surface(GameConfig.FISHES_IMG[0]))
        GameConfig.FISHES_MASK.append(pg.mask.from_surface(GameConfig.FISHES_IMG[1]))

        # Explosion
        GameConfig.EXPLOSION_IMG = [
            pg.image.load(f"assets/explosions/explosion_{str(i)}.png").convert_alpha()
            for i in range(1, 6)
        ]
        GameConfig.EXPLOSION_MASK = [
            pg.mask.from_surface(im) for im in GameConfig.EXPLOSION_IMG
        ]
