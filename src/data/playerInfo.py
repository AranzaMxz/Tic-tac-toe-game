
class player:
    def __init__(self, nplayer, name, piece):
        self.nplayer = nplayer
        self.name = name
        self.piece = piece
        self.moves = []
        self.playswon = 0
    def showData(self):
        print("Player " + self.nplayer +": " + self.name + " your piece is " + self.piece)
