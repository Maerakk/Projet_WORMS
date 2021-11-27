import pygame as pg
from game_state import *
from game_config import *
from move import *
from ground import *


class GameScreen:
    """
    cette classe représente la fenetre du jeu en lui même,
    c'est sur cette fenetre que le joueur arrive au début du jeu
    """

    def __init__(self):
        """
        pour fonctionner, la classe a besoin d'initier GameConfig
        """
        # Initialisations
        GameConfig.init()

    def process(self, window):
        """
        le process correspond à l'execution de la fenetre et du contenu
        dans cette fonction on va donc appeler la game loop
        :param window: la fenetre dans la quelle le jeu doit s'executer
        """
        play = True
        while play:
            self.game_loop(window)
            play = False

    def game_loop(self, window):
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
            next_move = self.get_next_move()
            if next_move.shoot:
                shoot = True

            # we recalculate the game state

            game_state.advance_state(next_move, next_move.shoot)

            # and we redraw the game
            game_state.draw(window)
            if shoot:
                game_state.draw_shoot(window)
            pg.display.update()

    def get_next_move(self):
        """
        cette fonction permet de connaitre le prochain moumevment a effectuer selon les entrées de l'utilisateur
        :return: un objet de type Move dont les attributs correspondent aux actions demandés par le joueur
        """
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


if __name__ == '__main__':
    """
    cette partie du programme permet de lancer directement le jeu sans passer par les écrans d'acceuil et autres
    """
    pg.init()
    AppliConfig.init()
    pg.display.set_caption("WORMS")
    window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
    game = GameScreen()
    game.process(window)
