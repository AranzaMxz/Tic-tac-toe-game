from game.game import game
from matrix import getMatrix

boardSize = int(input("Write the board size: "))
board = getMatrix(boardSize)

game()

