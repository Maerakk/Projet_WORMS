import time

from AppliConfig import AppliConfig
from game_screen import *
from welcome_screen import *

"""
Ceci correspond à l'application principale,
c'est par ce programme qu'on lancera le jeu
Ce programme apellera tour a tout et selon les besoins l'écran d'arrivée, de préparation du jeu et du jeu
"""


def main():

    # on initialise pygame
    pg.init()
    # AppliConfig a besoin de déclarer certaines variables après l'initialisation de pygame (les images)
    AppliConfig.init()
    # on met un titre a la fenetre
    pg.display.set_caption("Tout Cat-sser")
    # on creer la fenetre (de type pg.display)
    window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))

    again = True
    while again:
        # et on démare par le Welcome screen
        current_screen = WelcomeScreen()
        # on dessine le premier état du Welcome Screen
        current_screen.draw(window)
        # et on process la fenetre ( on effectue les actions en fonction des entrées de l'utilisateur
        next_screen = current_screen.process(window)

        # une fois le process finis (l'utilisateur a appuyé sur entrée ou a quitté)
        # on regarde la valeur de retour pour voir le choix effectuer par l'utilisateur
        # c'est l'application qui fait le lien entre le Welcome Screen et le Game_Preparation_Screen
        # le lien n'est pas direct
        if next_screen == WelcomeScreen.START:
            # on change le current_screen
            current_screen = GameScreen()
            # et a nouveau on le process
            current_screen.process(window)

        elif next_screen == WelcomeScreen.CREDITS:
            window.blit(AppliConfig.BACKGROUND_IMG,(0,0))
            current_screen.displayMessage(window,"ooops, c'est pas encore dévelloper sorry",50,AppliConfig.WINDOW_W/2,AppliConfig.WINDOW_H/2-50);
            pg.display.update()
            keys = pg.key.get_pressed()
            quitting = False
            time.sleep(1)
            current_screen.displayMessage(window,"(appuie sur entrer pour revenir au menu précédent)",50,AppliConfig.WINDOW_W/2,AppliConfig.WINDOW_H/2+50)
            pg.display.update()
            print("yeeee")
            while not quitting:
                # at each event we retrieve the event and analyse it
                # this is used only for quit event
                # for the movement we will use get_next_move
                for event in pg.event.get():
                    # if it's a quit event (close button) then we put quit to True the we exit the loop and return
                    if event.type == pg.QUIT:
                        quitting = True
                        again = False
                    if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                        quitting = True
        else :
            again = False

    # a la fin de l'execution on quite pygame et le programme
    pg.quit()
    quit()


if __name__ == '__main__':
    main()
