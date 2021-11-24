import pygame as pg
from game_config import GameConfig

class Player(pg.sprite.Sprite):
    def __init__(self,x):
        self.rect = pg.RECT(x,GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H,
                            GameConfig.PLAYER_W,
                            GameConfig.PLAYER_H
                            )
        pg.sprite.Sprite.__init__(self)