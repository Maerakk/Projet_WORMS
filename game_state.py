import pygame as pg
from game_config import *
from player import *
from weapon import *
from ground import Terrain


class GameState:
    """
    la classe GameState représente l'état du jeu a un moment précis (la position des joueurs, et autres)
    """

    def __init__(self):
        """
        lors de l'initialisation,
        on place 3 attributs (ils changeront plus tard)
        le terrain
        le joueur (changera en liste de joueur ou deux joueurs)
        les armes (peut etres enlever pour laisser uniquement en attribut de joueur ?)
        """
        self.terrain = Terrain()
        self.player = Player(200,self.terrain)
        self.arme = Weapon(self.player, self.terrain)

    def draw(self, window):
        """
        cette fonction est appelé pour dessiner l'état du jeu
        elle appelle la fonction draw de tout ses attributs
        :param window: la fenetre dans laquelle dessiner
        """
        # on empile les images donc le background en premier
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        # puis l'eau
        # puis le terrain
        window.blit(self.terrain.image,(0,0))
        # puis le joueur
        self.player.draw(window)
        # puis les armes
    def draw_shoot(self,window):
        self.arme.projectile.draw(window)
    def advance_state(self, next_move,arme_thrown):
        """
        advance state permet d'effectuer les calculs pour faire avancer le jeu
        cette méthode fait appel aux méthodes advance state des différent objets
        :param next_move:
        :param arme_thrown:
        :return:
        """
        self.player.advance_state(next_move)
        self.arme.advance_state(arme_thrown)

