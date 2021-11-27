import time

from appli_config import AppliConfig
from game_screen import *
from welcome_screen import *

"""
This is the main application
This is by this program that we will launch the game
This program will show by turns and according to our needs the welcome screen, setting screen, main game screen
"""


def main():
    # Pygame Initialisation
    pg.init()
    # AppliConfig needs to declare some variables after pygame initialisation (for instance the images)
    AppliConfig.init()
    # We give our window a caption
    pg.display.set_caption("Tout Cat-sser")
    # We create the window (pg.display type)
    window = pg.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))

    again = True
    while again:
        # We start by the welcome screen
        current_screen = WelcomeScreen()
        # We draw the first state of welcome screen
        current_screen.draw(window)
        # And we process the window
        next_screen = current_screen.process(window)

        '''
        Once the process is done (the user pushed entree or quite) we look the return value to see the choice done
        This is the app that do the link between Welcome Screen and Game_Preparation_Screen
        The link is not direct 
        '''
        if next_screen == WelcomeScreen.START:
            # We change the curren_screen
            current_screen = GameScreen()
            # And we process it again
            again = not current_screen.process(window)


        elif next_screen == WelcomeScreen.CREDITS:
            window.blit(AppliConfig.BACKGROUND_IMG, (0, 0))
            current_screen.displayMessage(window, "ooops, c'est pas encore dévelloper sorry", 50,
                                          AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 2 - 50)
            pg.display.update()
            keys = pg.key.get_pressed()
            quitting = False
            time.sleep(1)
            current_screen.displayMessage(window, "(appuie sur entrer pour revenir au menu précédent)", 50,
                                          AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 2 + 50)
            pg.display.update()
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
        else:
            again = False

    # At the end of the execution we quit pygame and the program
    pg.quit()
    quit()


if __name__ == '__main__':
    main()
