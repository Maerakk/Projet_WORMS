import pygame as pg
from game_state import *
from game_config import *




def main():
    #Initialisations
    pg.init()

    GameConfig.init()
    play = True


    while play:
        window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
        game_loop(window)


def game_loop(window):
    quitting = False
    gameState = GameState()
    while not quitting:
        gameState.draw(window)
        pg.display.update()

main()