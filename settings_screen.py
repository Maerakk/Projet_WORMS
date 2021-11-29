import pygame as pg

from appli_config import AppliConfig


class SettingScreen:
    """
    Class that represent the Setting Screen
    It is on this window that the user is when they click on start
    the next 6 variables defines value for type of ground
    """

    GROUND0 = 0
    GROUND1 = 1
    GROUND2 = 2
    GROUND3 = 3
    GROUND4 = 4
    GROUND5 = 5

    def __init__(self):
        """
        initialisation we put ground choice to 0
        """
        self.ground_choice = SettingScreen.GROUND0
        self.cat_choice = [0,0]
        self.is_choosing = 0

    def draw(self, window):
        """
        this function draws the window
        :param window: window which we should draw in
        """
        window.blit(AppliConfig.BACKGROUND_IMG,(0,0))
        self.displayMessage(window, "Tout Cat-sser", 150, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 5)
        self.displayMessage(window,"Player 1",50,AppliConfig.WINDOW_W/8,AppliConfig.WINDOW_H/3)
        self.displayMessage(window,"Player 2",50,AppliConfig.WINDOW_W*7/8,AppliConfig.WINDOW_H/3)
        self.choose_ground(window)
        self.choose_cat(window)
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

    def choose_cat(self,window):
        """
        this function must handle the display of the cat choosen by the user
        :param window:
        """
        window.blit(AppliConfig.ARROW_UP_IMG,(AppliConfig.WINDOW_W/10,AppliConfig.WINDOW_H/2-47+5))
        window.blit(AppliConfig.LIST_CAT_IMG[self.cat_choice[0]],(AppliConfig.WINDOW_W/10,AppliConfig.WINDOW_H/2))
        window.blit(AppliConfig.ARROW_DOWN_IMG,(AppliConfig.WINDOW_W/10,AppliConfig.WINDOW_H/2+47+10))

        window.blit(AppliConfig.ARROW_UP_IMG,(AppliConfig.WINDOW_W*7/8,AppliConfig.WINDOW_H/2-47+5))
        window.blit(AppliConfig.LIST_CAT_IMG[self.cat_choice[1]],(AppliConfig.WINDOW_W*7/8,AppliConfig.WINDOW_H/2))
        window.blit(AppliConfig.ARROW_DOWN_IMG,(AppliConfig.WINDOW_W*7/8,AppliConfig.WINDOW_H/2+47+10))


    def choose_ground(self, window):
        """
        this function has for job to put the black square behind the right ground type
        :param window:
        """
        if self.ground_choice == SettingScreen.GROUND0:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.ground_choice == SettingScreen.GROUND1:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*11/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.ground_choice == SettingScreen.GROUND2:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*21/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.ground_choice == SettingScreen.GROUND3:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*31/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.ground_choice == SettingScreen.GROUND4:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*41/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.ground_choice == SettingScreen.GROUND5:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*51/60-5, AppliConfig.WINDOW_H*8/10-4))

        window.blit(AppliConfig.LIST_TERRAIN_IMG[0], (AppliConfig.WINDOW_W/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[1], (AppliConfig.WINDOW_W*11/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[2], (AppliConfig.WINDOW_W*21/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[3], (AppliConfig.WINDOW_W*31/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[4], (AppliConfig.WINDOW_W*41/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[5], (AppliConfig.WINDOW_W*51/60, AppliConfig.WINDOW_H*8/10))

    def get_next_move(self):
        """
        Recongnize every next move to be make according to the entries of the user
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.ground_choice -= 1
        if keys[pg.K_RIGHT]:
            self.ground_choice += 1

        if self.ground_choice < 0:
            self.ground_choice = SettingScreen.GROUND5
        if self.ground_choice > 5:
            self.ground_choice = SettingScreen.GROUND0

        if keys[pg.K_UP]:
            self.cat_choice[self.is_choosing] += 1
        if keys[pg.K_DOWN]:
            self.cat_choice[self.is_choosing] -= 1

        if self.cat_choice[self.is_choosing] < 0:
            self.cat_choice[self.is_choosing] = 2
        if self.cat_choice[self.is_choosing] > 2:
            self.cat_choice[self.is_choosing] = 0

    def process(self,window):
        """
        The process equals the execution of the window and its contents
        We will call next move and draw
        :param window: window where the settingScreen will display
        """
        quitting = False
        while not quitting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quitting = True
                    self.ground_choice = 6
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    if self.is_choosing == 0:
                        self.is_choosing = 1
                    else :
                        return self.ground_choice, self.cat_choice
            self.get_next_move()
            self.draw(window)
            pg.time.delay(60)
