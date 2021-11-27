class Move:
    """
    Class allowing to define the movements chosen by the user
    """
    def __init__(self):
        self.left = False
        self.right = False
        self.jump = False
        self.shoot = False
        self.shootFinished = False