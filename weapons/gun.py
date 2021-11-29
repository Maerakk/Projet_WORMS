from weapons.weapon import Weapon


class Gun(Weapon):
    def init(self):
        self.shootFinished = False
