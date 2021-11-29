from projectiles.projectile import *


class BazookaProjectile(Projectile):
    def __init__(self, weapon, ground, style):
        self.weapon = weapon
        self.ground = ground
        super().__init__(weapon, ground)
        self.style = style
        self.mass = 0.1
        # The bazooka's projectile explodes at impact so it does not have any bounce neither elasticity
        self.k = 0
        self.bounce = False
        self.rect = pg.rect.Rect(self.weapon.rect.top,
                                 self.weapon.rect.left,
                                 GameConfig.FISH_W,
                                 GameConfig.FISH_H)

        self.image = GameConfig.FISHES_IMG[self.style]
        self.mask = GameConfig.FISHES_MASK[self.style]



