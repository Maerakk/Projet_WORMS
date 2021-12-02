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

    def __init__(self, ground_type, cat_type):
        """
        To be functioning this class need GameConfig to be instanced
        """
        # Initialisations
        self.quitting = False
        # sprites and images initialisation
        GameConfig.init()
        Explosion.init_sprites()

        # initializing a local gameState
        # it will represent the current gameState
        self.game_state = GameState(ground_type,cat_type)

    def process(self, window):
        """
        this is the game loop, as long as the user wants to play, the loops run
        :param window: the window which the game will run in
        """
        while not self.quitting and self.game_state.is_over < 0:

            # at each event we retrieve the event and analyse it
            # this is used only for quit event
            # for the movement we will use get_next_move
            for event in pg.event.get():
                # if it's a quit event (close button) then we put quit to True the we exit the loop and return
                if event.type == pg.QUIT:
                    self.quitting = True

            # on each loop we get the next move
            next_move = self.get_next_move()

            # we recalculate the game state

            self.game_state.advance_state(next_move)

            # and we redraw the game
            self.game_state.draw(window)
            pg.display.update()

        # if self.quitting is set to false it means the game stopped because someone won
        self.game_state.player = []
        self.who_won = self.game_state.is_over
        return self.quitting


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

        next_move.weapon = next_move.weapon_bazooka or \
                           next_move.weapon_grenade or \
                           next_move.weapon_sheep or \
                           next_move.weapon_sheep_controlled

        return next_move

    def displayMessage(self, window, text, fontSize, x, y, color=AppliConfig.DARK_YELLOW):
        """
        this function displays
        :param window: in a window
        :param text: a text
        :param fontSize: of size fontSize
        :param x: at coordinates x
        :param y: y
        :param color: of color color (DARK_YELLOW by default)
        took from tp1
        """
        font = pg.font.Font('assets/BradBunR.ttf', fontSize)
        img = font.render(text, True, color)
        displayRect = img.get_rect()
        displayRect.center = (x, y)
        window.blit(img, displayRect)

if __name__ == '__main__':
    """
    This part of the program allows to launch the game without seeing the welcome screen
    """
    pg.init()
    AppliConfig.init()
    pg.display.set_caption("WORMS")
    window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
    game = GameScreen(0,0)
    game.process(window)
