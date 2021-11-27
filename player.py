import pygame as pg
from game_config import GameConfig


class Player(pg.sprite.Sprite):
    """
    Cette classe représente un joueur
    (dans le cas d'ajout de plusieurs personnages pour un joueur nous appellerons cette classe personnage
    ou chat)
    """

    # CONSTANTES
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self, x, terrain):

        # instantiation du parent
        super().__init__()

        # Attributs
        # pour la geston des animation (inutile pour l'instant)
        self.sprite_count = 0
        self.direction = Player.NONE

        # Image du joueur
        self.image = GameConfig.STANDING_IMG
        # mask du joueur (pour gérer les collisions)
        self.mask = GameConfig.STANDING_MASK
        # le terrain afin de pouvoir gérer les collisions
        # il faudra essayer de mettre le terrain autre part afin de ne pas l'intégrer au joueur
        self.terrain = terrain

        y = self.terrain.builder.lagrange(x)
        # Emplacement
        # on place le joueur a une coordonnée x et au y sur le graph généré
        self.rect = pg.Rect(x,
                            y - GameConfig.PLAYER_H,
                            GameConfig.PLAYER_W,
                            GameConfig.PLAYER_H
                            )

        # Vitesse
        # au départ le joueur de bouge pas
        self.vx = 0
        self.vy = 0

        # Sprite
        # pg.sprite.Sprite.__init__(self)

    def draw(self, window):
        """
        fonction dessinant le joueur
        :param window: fenetre sur laquelle dessiner le joueur
        """
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):
        """
        fonction testant si le joueur touche le sol ou pas
        :return: true si le joueur touche le sol false sinon
        """
        # on utilise ici la fonction collide_mask permettant d'utiliser les mask des entitées
        return pg.sprite.collide_mask(self, self.terrain)

    def advance_state(self, next_move):
        """
        advance state permet d'effectuer les calculs permettant au jeu d'avancer
        les calculs consitent en la recherche de la prochaine position du joueur en fonction
        de sa position initiale et des vecteurs qui lui sont imposés
        :param next_move: le mouvement choisi par l'utilisateur
        """
        # Acceleration de base a 0
        fx = 0
        fy = 0
        # puis, l'accélération est gérer en fonction de next_move
        if next_move.left:
            fx = GameConfig.FORCE_LEFT
        if next_move.right:
            fx = GameConfig.FORCE_RIGHT
        if next_move.jump:
            fy = GameConfig.FORCE_JUMP
            print("if next_move")

        # Vitesse de base a dt/dx(accélération)
        self.vx = fx * GameConfig.DT
        # par défaut on imagine que le joueur descend (la gravité lui est toujours appliqué,
        # on la lui imputera ensuite si il touche le sol
        # cela évite des bugs d'affichage et de "bounce" faisant rebondir frénétiquement le joueur sur le sol
        self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT

        # Position beaucoup de tests sont effectués
        # le x de base correspond a la gauche du rectangle du joueur
        x = self.rect.left
        # on définit les vitesses min et max en x
        vx_min = -x / GameConfig.DT
        vx_max = (GameConfig.WINDOW_W - GameConfig.PLAYER_W - x) / GameConfig.DT
        # et on trouve la variable soit min soit max si la valeur demandé est hors des bornes
        # soit la valeur demandé
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)

        # on bouge le rectangle comme si de rien était (il n'est pas afficher
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)
        # et on regarde si sa nouvelle position touche le sol ou pas
        if self.on_ground():
            # si ou, on vérifie qu'il n'est pas dans le sol (+5 pour éviter les fausses colisions)
            self.rect.bottom = self.terrain.builder.lagrange(self.rect.midbottom[0]) + 5
            # et on applique la force appliqué par le joueur sur le personnage
            # cette force pouvant etre 0 ou GameConfig.FORCE_JUMP
            self.vy = fy * GameConfig.DT
            # on rebouge le rectangle en y uniquement
            self.rect = self.rect.move(0, self.vy * GameConfig.DT)

        # if next_move.left:
        # self.direction = Player.LEFT
        # elif next_move.right:
        # self.direction = Player.RIGHT
        # else:
        # self.direction = Player.NONE

        # self.sprite_count += 1
        # if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER*len(Player.IMAGES[self.direction]):
        #     self.sprite_count = 0
        # self.image = Player.IMAGES[self.direction][
        #     self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        #     ]
        # self.mask = Player.MASKS[self.direction][
        #     self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
        #     ]
