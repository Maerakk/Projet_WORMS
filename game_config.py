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

    NB_FRAME_EXPLOSION = 10

    @staticmethod
    def init(cat_type):
        # Initialisations of all the images needed
        AppliConfig.init()
        # Background
        GameConfig.BACKGROUND_IMG = AppliConfig.BACKGROUND_IMG

        # Player
        GameConfig.WALK_RIGHT_IMG = [
            pg.image.load(f"assets/cats/{str(cat_type)}/right_{str(i)}.png").convert_alpha()
            for i in range(1, 3)
        ]
        GameConfig.WALK_LEFT_IMG = [
            pg.image.load(f"assets/cats/{str(cat_type)}/left_{str(i)}.png").convert_alpha()
            for i in range(1, 3)
        ]
        GameConfig.STANDING_IMG = [
            pg.image.load(f"assets/cats/{str(cat_type)}/standing_{str(i)}.png").convert_alpha()
            for i in range(1, 3)
        ]

        GameConfig.WALK_RIGHT_MASKS = [
            pg.mask.from_surface(im) for im in GameConfig.WALK_RIGHT_IMG
        ]
        GameConfig.WALK_LEFT_MASKS = [
            pg.mask.from_surface(im) for im in GameConfig.WALK_LEFT_IMG
        ]
        GameConfig.STANDING_MASKS = [
            pg.mask.from_surface(im) for im in GameConfig.STANDING_IMG
        ]

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

        GameConfig.EXPLOSION_IMG = pg.image.load("assets/explosions.png")
