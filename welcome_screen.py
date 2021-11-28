import pygame as pg

from appli_config import AppliConfig


class WelcomeScreen:
    """
    Class that represent the Welcome Screen
    It is on this screen that the user is when they start the application
    the next 2 variables defines value for user choice
    """
    START = 1
    CREDITS = 2

    def __init__(self):
        """
        initialisation, we put the choice at Start
        """
        self.choice = WelcomeScreen.START

    def draw(self, window):
        """
       this function draws the window
       :param window: window which we should draw in
       """

        # background in a first place
        window.blit(AppliConfig.BACKGROUND_IMG, (0, 0))
        # text then
        self.displayMessage(window, "Tout Cat-sser", 150, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 5)
        self.displayMessage(window, "-Start-", 100, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 2)
        self.displayMessage(window, "-Credits-", 100, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H * 2 / 3)
        # and, given the user choice, the arrow on START or CREDITS
        if self.choice == WelcomeScreen.START:
            self.choose_start(window)
        else:
            self.choose_credits(window)
        # without forgetting to update the display
        pg.display.update()

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

    def choose_start(self, window):
        """
        this function (like the next one) should put the arrow in front of the good word
        :param window: la fenetre dans la quelle afficher
        """
        window.blit(AppliConfig.ARROW_RIGHT_IMG,
                    (AppliConfig.WINDOW_W / 2 - 220, AppliConfig.WINDOW_H / 2 - 20))

    def choose_credits(self, window):
        window.blit(AppliConfig.ARROW_RIGHT_IMG,
                    (AppliConfig.WINDOW_W / 2 - 250, AppliConfig.WINDOW_H * 2 / 3 - 20))

    def get_next_move(self):
        """
        Recongnize every next move to be make according to the entries of the user
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_DOWN]:
            if self.choice == WelcomeScreen.START:
                self.choice = WelcomeScreen.CREDITS
            else:
                self.choice = WelcomeScreen.START

    def process(self, window):
        """
        The process equals the execution of the window and its contents
        We will call next move and draw
        :param window: window where the settingScreen will display
        """
        quitting = False
        while not quitting:
            # at each event we retrieve the event and analyse it
            # this is used only for quit event
            # for the movement we will use get_next_move
            for event in pg.event.get():
                # if it's a quit event (close button) then we put quit to True the we exit the loop and return
                if event.type == pg.QUIT:
                    quitting = True
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    return self.choice
            self.get_next_move()
            self.draw(window)
            pg.time.delay(60)
