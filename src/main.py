from game.game import game
from board.printBoard import getBoard
from getInfo import info

# Get information to start the game
boardSize, winList, player1, player2 = info()

# Print the board
board = getBoard(boardSize)


game()

