import pygame as pg
from game_state import *
from game_config import *
from move import *


def game_loop(window):
    """
    this is the game loop, as long as the user wants to play, the loops run
    :param window: the window which the game will run in
    """

    # initializing a local gameState
    # it will represent the current gameState
    game_state = GameState()
    # we draw the window the game is initialized
    game_state.draw(window)
    # the window isn't refreshed for now
    # it will be at the end of each while loop

    quitting = False

    arme_thrown_1_Time = False
    shoot = False
    # this is really the game loop
    while not quitting:

        # at each event we retrieve the event and analyse it
        # this is used only for quit event
        # for the movement we will use get_next_move
        for event in pg.event.get():
            # if it's a quit event (close button) then we put quit to True the we exit the loop and return
            if event.type == pg.QUIT:
                quitting = True

        # on each loop we get the next move
        next_move = get_next_move()
        # we recalculate the game state

        game_state.advance_state(next_move, next_move.shoot)

        # and we redraw the game
        game_state.draw(window)
        game_state.player.draw(window)
        game_state.arme.draw(window)
        pg.display.update()

        # tick
        pg.time.delay(20)


def get_next_move():
    next_move = Move()
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        next_move.right = True
    if keys[pg.K_LEFT]:
        next_move.left = True
    if keys[pg.K_UP]:
        next_move.jump = True

    if keys[pg.K_LCTRL]:
        next_move.shoot = True

    return next_move





def main():
    # Initialisations
    pg.init()
    GameConfig.init()
    play = True

    # Fenêtre
    pg.display.set_caption("WORMS")

    while play:
        window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
        game_loop(window)
        play = False

    pg.quit()
    quit()


main()
