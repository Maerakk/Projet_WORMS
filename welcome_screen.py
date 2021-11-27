import pygame as pg

from appli_config import AppliConfig


class WelcomeScreen:
    """
    Cette classe représente la fenetre de départ de l'application, c'est la première fenetre afichée
    Deux variables statics sont déclaré correspondant a la valeur des choix Start ou Credits
    """
    START = 1
    CREDITS = 2

    def __init__(self):
        """
        lors de l'instantiation on met le choit a Start
        c'est en effet le choix par défaut
        """
        self.choice = WelcomeScreen.START

    def draw(self, window):
        """
        cette fonction permet de dessiner la fenetre
        :param window: la fenetre dans laquelle dessiner le welcomeScreen
        """
        # on place dans un premier temps l'arrière plan
        window.blit(AppliConfig.BACKGROUND_IMG, (0, 0))
        # puis on affiche le texte
        self.displayMessage(window, "Tout Cat-sser", 150, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 5)
        self.displayMessage(window, "-Start-", 100, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 2)
        self.displayMessage(window, "-Credits-", 100, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H * 2 / 3)
        # et selon le choix, on met la fleche sur start ou sur credits
        if self.choice == WelcomeScreen.START:
            self.choose_start(window)
        else:
            self.choose_credits(window)
        # on oublie pas d'update le display
        pg.display.update()

    def displayMessage(self, window, text, fontSize, x, y, color=AppliConfig.DARK_YELLOW):
        """
        cette fonction permet d'afficher
        :param window: dans la fenetre windown
        :param text: un text text
        :param fontSize: de taille fontSize
        :param x: au coordonnées x
        :param y: y
        :param color: et de couleur color (DARK_YELLOW par défaut)
        cette fonction est récupérée du tp1
        """
        font = pg.font.Font('assets/BradBunR.ttf', fontSize)
        img = font.render(text, True, color)
        displayRect = img.get_rect()
        displayRect.center = (x, y)
        window.blit(img, displayRect)

    def choose_start(self, window):
        """
        cette fonction comme la suivante permettent d'afficher la fleche au bon endroit selon le choix
        :param window: la fenetre dans la quelle afficher
        """
        window.blit(AppliConfig.ARROW_IMG,
                    (AppliConfig.WINDOW_W / 2 - 220, AppliConfig.WINDOW_H / 2 - 20))

    def choose_credits(self, window):
        window.blit(AppliConfig.ARROW_IMG,
                    (AppliConfig.WINDOW_W / 2 - 250, AppliConfig.WINDOW_H * 2 / 3 - 20))

    def get_next_move(self):
        """
        cette fonction permet d'analyser les entrées de l'utilisateurs
        :return: un choix si l'entrée est prise en compte par la fenetre
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_DOWN]:
            if self.choice == WelcomeScreen.START:
                return WelcomeScreen.CREDITS
            else:
                return WelcomeScreen.START
        return self.choice

    def process(self, window):
        keys = pg.key.get_pressed()
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
            self.choice = self.get_next_move()
            self.draw(window)
            pg.time.delay(60)
