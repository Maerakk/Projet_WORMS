import pygame as pg
from game_config import GameConfig

class Player(pg.sprite.Sprite):

    #CONSTANTES
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self,x):

        # Attributs

        self.sprite_count = 0
        self.direction = Player.NONE

        #Image du joueur
        self.image = GameConfig.STANDING_IMG


        #Emplacement
        self.rect = pg.Rect(x,
                            GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H,
                            GameConfig.PLAYER_W,
                            GameConfig.PLAYER_H
                            )

        #Vitesse
        self.vx = 0
        self.vy = 0

        #Sprite
        # pg.sprite.Sprite.__init__(self)

    def draw(self,window):
        window.blit(self.image,self.rect.topleft)

    def on_ground(self):
        return self.rect.bottom == GameConfig.Y_PLATEFORM

    def advance_state(self, next_move):

        # Acceleration
        fx = 0
        fy = 0
        if next_move.left:
            fx = GameConfig.FORCE_LEFT
        if next_move.right:
            fx = GameConfig.FORCE_RIGHT
        if next_move.jump:
            fy = GameConfig.FORCE_JUMP
            print("if next_move")

        # Vitesse
        self.vx = fx * GameConfig.DT
        if self.on_ground():
            self.vy = fy * GameConfig.DT
        else:
            self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT

        # Position
        x = self.rect.left
        vx_min = -x / GameConfig.DT
        vx_max = (GameConfig.WINDOW_W - GameConfig.PLAYER_W - x) / GameConfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)

        y = self.rect.top
        vy_max = (GameConfig.Y_PLATEFORM - GameConfig.PLAYER_H-y) / GameConfig.DT
        self.vy = min(self.vy, vy_max)

        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)

        if next_move.left:
            self.direction = Player.LEFT
        elif next_move.right:
            self.direction = Player.RIGHT
        else:
            self.direction = Player.NONE

        # self.sprite_count += 1
        # if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[self.direction]):
        #     self.sprite_count = 0
        # self.image = Player.IMAGES[self.direction][
        #     self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        #     ]
        # self.mask = Player.MASKS[self.direction][
        #     self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        #     ]