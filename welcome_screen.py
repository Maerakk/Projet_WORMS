import pygame as pg

from AppliConfig import AppliConfig


class WelcomeScreen:

    START = 1
    CREDITS = 2


    def __init__(self):
        self.choice = WelcomeScreen.START

    def draw(self, window):
        window.blit(AppliConfig.BACKGROUND_IMG, (0, 0))
        self.displayMessage(window, "Tout Cat-sser", 150, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 5)
        self.displayMessage(window, "-Start-", 100, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H /2)
        self.displayMessage(window, "-Credits-", 100, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H * 2/3)
        if self.choice == WelcomeScreen.START:
            self.choose_start(window)
        else:
            self.choose_credits(window)
        pg.display.update()

    def displayMessage(self, window, text, fontSize, x, y, color=AppliConfig.DARK_YELLOW):
        font = pg.font.Font('assets/BradBunR.ttf', fontSize)
        img = font.render(text, True, color)
        displayRect = img.get_rect()
        displayRect.center = (x, y)
        window.blit(img, displayRect)

    def choose_start(self,window):
        window.blit(AppliConfig.ARROW_IMG,
                    (AppliConfig.WINDOW_W / 2 - 220, AppliConfig.WINDOW_H / 2 - 20))

    def choose_credits(self,window):
        window.blit(AppliConfig.ARROW_IMG,
                    (AppliConfig.WINDOW_W / 2 - 250, AppliConfig.WINDOW_H *2 / 3 - 20))

    def get_next_move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_DOWN]:
            if self.choice == WelcomeScreen.START:
                return WelcomeScreen.CREDITS
            else:
                return WelcomeScreen.START
        return self.choice

    def process(self,window):
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
