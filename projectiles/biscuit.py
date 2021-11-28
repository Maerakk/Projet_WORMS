from projectile import *


class Biscuit(Projectile):
    def init(self):
        self.mass = 0.0005

        self.image = GameConfig.FISH_1_IMG