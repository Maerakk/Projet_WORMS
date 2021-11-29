from weapons.weapon import Weapon


class Grenade(Weapon):
    def init(self, player, ground):
        super().__init__(player, ground)
        self.shootFinished = False
