import pygame as pg

from game_config import GameConfig


class Explosion(pg.sprite.Sprite):

    @staticmethod
    def init_sprites():
        Explosion.IMAGES = GameConfig.EXPLOSION_IMG
        Explosion.MASKS = GameConfig.EXPLOSION_MASK

    def __init__(self, x, y):
        super().__init__()

        self.sprite_count = 0
        self.rect = pg.Rect(
            x,
            y,
            0,
            0
        )
        self.image = Explosion.IMAGES[self.sprite_count//GameConfig.NB_SPRITE_FRAME_EXPLOSION]
        self.mask = Explosion.MASKS[self.sprite_count//GameConfig.NB_SPRITE_FRAME_EXPLOSION]

        self.on_screen = True

    def advance_state(self,game_state):
        if self.on_screen:
            self.sprite_count += 1
            if self.sprite_count >= GameConfig.NB_SPRITE_FRAME_EXPLOSION * len(Explosion.IMAGES)-1:
                self.on_screen = False
            self.image = Explosion.IMAGES[self.sprite_count // GameConfig.NB_SPRITE_FRAME_EXPLOSION]
            self.mask = Explosion.MASKS[self.sprite_count // GameConfig.NB_SPRITE_FRAME_EXPLOSION]

            for player in game_state.player:
                player.loose_life(self)

    def draw(self, window):
        if self.on_screen:
            window.blit(self.image, self.rect.topleft)
