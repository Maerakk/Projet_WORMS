import pygame as pg
from game_state import *
from game_config import *
from move import *
from ground import *


class GameScreen:
    """
    Class that represent the window of the game in itself
    It is on this window that the user is when they open the game
    """

    def __init__(self,ground_type,cat_type):
        """
        To be functioning this class need GameConfig to be instanced
        """
        # Initialisations
        self.quitting = False
        GameConfig.init(cat_type)
        Player.init_sprites(cat_type)
        self.game_state = GameState(ground_type)

    def process(self, window):
        """
        The process equals the execution of the window and its contents
        We will call game_loop in this function
        :param window: window where the game will play
        """
        play = True
        while play:
            self.game_loop(window)
            play = False
        return self.quitting

    def game_loop(self, window):
        """
        this is the game loop, as long as the user wants to play, the loops run
        :param window: the window which the game will run in
        """

        # initializing a local gameState
        # it will represent the current gameState

        # we draw the window the game is initialized
        self.game_state.draw(window)
        # the window isn't refreshed for now
        # it will be at the end of each while loop

        arme_thrown_1_Time = False
        shoot = False
        weapon_used = False
        # this is really the game loop
        while not self.quitting:

            # at each event we retrieve the event and analyse it
            # this is used only for quit event
            # for the movement we will use get_next_move
            for event in pg.event.get():
                # if it's a quit event (close button) then we put quit to True the we exit the loop and return
                if event.type == pg.QUIT:
                    self.quitting = True

            # on each loop we get the next move
            next_move = self.get_next_move()
            if next_move.weapon_grenade == True or next_move.weapon_bazooka == True or next_move.weapon_sheep == True or next_move.weapon_sheep_controlled ==True:
                weapon_used = True
            if next_move.shoot:
                shoot = True

            # we recalculate the game state

            self.game_state.advance_state(next_move, next_move.shoot)

            # and we redraw the game
            self.game_state.draw(window)

            if shoot:
                self.game_state.weapon.projectile.x0 = self.game_state.player.rect.top
                self.game_state.weapon.projectile.y0 = self.game_state.player.rect.left
                self.game_state.draw_shoot(window)
            if weapon_used:
                self.game_state.draw_weapon(window,next_move)
            pg.display.update()

    def get_next_move(self):
        """
        Recongnize every next move to be make according to the entries of the user
        :return: Move type object whose attributes equals the actions asked by the user
        """
        next_move = Move()
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            next_move.right = True
        if keys[pg.K_LEFT]:
            next_move.left = True
        if keys[pg.K_UP]:
            next_move.jump = True
        if keys[pg.K_1]:
            next_move.weapon_grenade = True
        if keys[pg.K_2]:
            next_move.weapon_bazooka = True
        if keys[pg.K_3]:
            next_move.weapon_sheep = True
        if keys[pg.K_4]:
            next_move.weapon_sheep_controlled = True
        if keys[pg.K_LCTRL]:
            next_move.shoot = True

        return next_move


if __name__ == '__main__':
    """
    This part of the program allows to launch the game without seeing the welcome screen
    """
    pg.init()
    AppliConfig.init()
    pg.display.set_caption("WORMS")
    window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
    game = GameScreen(0)
    game.process(window)
