from weapons.weapon import *


class MouseControlled(Weapon):
    def init(self):
        self.shootFinished = False
