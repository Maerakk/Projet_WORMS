import pygame as pg

from appli_config import AppliConfig


class SettingScreen:
    """
    Cette classe représente la fenetre de choix avant le jeu
    6 variables staiques représentants les valeurs associés aux choix des terrains
    """

    TERRAIN0 = 0
    TERRAIN1 = 1
    TERRAIN2 = 2
    TERRAIN3 = 3
    TERRAIN4 = 4
    TERRAIN5 = 5

    def __init__(self):
        """
        lors de l'instanciation on met le choix a TERRAIN0
        """
        self.terrain_choice = SettingScreen.TERRAIN0

    def draw(self, window):
        """
        cette fonction permet de dessiner la fenetre
        :param window: la fenetre dans laquelle dessiner le settingScreen
        """
        window.blit(AppliConfig.BACKGROUND_IMG,(0,0))
        self.displayMessage(window, "Tout Cat-sser", 150, AppliConfig.WINDOW_W / 2, AppliConfig.WINDOW_H / 5)
        self.choose(window)
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

    def choose(self, window):
        if self.terrain_choice == SettingScreen.TERRAIN0:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.terrain_choice == SettingScreen.TERRAIN1:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*10/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.terrain_choice == SettingScreen.TERRAIN2:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*20/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.terrain_choice == SettingScreen.TERRAIN3:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*30/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.terrain_choice == SettingScreen.TERRAIN4:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*40/60-5, AppliConfig.WINDOW_H*8/10-4))
        elif self.terrain_choice == SettingScreen.TERRAIN5:
            window.blit(AppliConfig.TERRAIN_CHOICE_IMG, (AppliConfig.WINDOW_W*50/60-5, AppliConfig.WINDOW_H*8/10-4))

        window.blit(AppliConfig.LIST_TERRAIN_IMG[0], (AppliConfig.WINDOW_W/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[1], (AppliConfig.WINDOW_W*10/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[2], (AppliConfig.WINDOW_W*20/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[3], (AppliConfig.WINDOW_W*30/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[4], (AppliConfig.WINDOW_W*40/60, AppliConfig.WINDOW_H*8/10))
        window.blit(AppliConfig.LIST_TERRAIN_IMG[5], (AppliConfig.WINDOW_W*50/60, AppliConfig.WINDOW_H*8/10))

    def get_next_move(self):
        """
        cette fonction permet d'analyser les entrées de l'utilisateurs
        :return: un choix si l'entrée est prise en compte par la fenetre
        """
        keys = pg.key.get_pressed()
        print(keys[pg.K_LEFT])
        print(keys[pg.K_RIGHT])
        if keys[pg.K_LEFT]:
            self.terrain_choice -= 1
        if keys[pg.K_RIGHT]:
            self.terrain_choice += 1

        if self.terrain_choice < 0:
            self.terrain_choice = SettingScreen.TERRAIN5
        if self.terrain_choice > 5:
            self.terrain_choice = SettingScreen.TERRAIN0

    def process(self,window):
        """
        le process correspond à l'execution de la fenetre et du contenu
        dans cette fonction on va donc appeler next move et dessiner la fenetre
        :param window: la fenetre dans la quelle le settingScreen doit s'executer
        """
        quitting = False
        while not quitting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quitting = True
                    self.terrain_choice = 6
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    return self.terrain_choice
            self.get_next_move()
            print(self.terrain_choice)
            self.draw(window)
            pg.time.delay(40)
