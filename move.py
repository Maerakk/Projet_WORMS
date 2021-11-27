class Move:
    """
    class permettant de définir les mouvement du joueur
    """
    def __init__(self):
        self.left = False
        self.right = False
        self.jump = False
        self.shoot = False
        self.shootFinished = False