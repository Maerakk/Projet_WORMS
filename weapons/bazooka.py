from weapon import *
from game_config import *


class Bazooka(Weapon):
    def __init__(self, player, terrain):
        super().__init__(player, terrain)
        self.image = GameConfig.BAZOOKA_IMG
        self.projectile.image = GameConfig.BAZOOKA_IMG
