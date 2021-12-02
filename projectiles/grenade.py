from projectiles.projectile import *


class GrenadeProjectile(Projectile):
    def __init__(self, weapon, ground, style):
        self.weapon = weapon
        self.ground = ground
        super().__init__(weapon, ground)
        self.style = style
        self.mass = 0.1
        # The bazooka's projectile explodes at impact so it does not have any bounce neither elasticity
        self.k = 0.8

        self.bounce = True
        self.rect = pg.rect.Rect(self.weapon.rect.top,
                                 self.weapon.rect.left,
                                 GameConfig.GRENADE_W,
                                 GameConfig.GRENADE_H)

        self.image = GameConfig.GRENADE_IMG[self.style]
        self.mask = GameConfig.GRENADE_MASK[self.style]



