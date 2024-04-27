from data.playersData import getData
from game.startGame import start
#from Data import player

def game(boardSize, winList, player1, player2):
    print("\n\t LET´S START\n")
    selection, player = start(boardSize, player1, player2)
    print(player.name + " you chose ", selection)

    




