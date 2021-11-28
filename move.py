class Move:
    """
    Class allowing to define the movements chosen by the user
    """

    def __init__(self):
        self.left = False
        self.right = False
        self.jump = False
        self.shoot = False
        self.weapon_bazooka = False
        self.weapon_grenade = False
        self.weapon_sheep = False
        self.weapon_sheep_controlled = False
        self.weapon = self.weapon_bazooka or \
                      self.weapon_grenade or \
                      self.weapon_sheep or \
                      self.weapon_sheep_controlled
        self.shoot = False
        self.shootFinished = False
