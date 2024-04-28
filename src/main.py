from game.game import game
from board.printBoard import getBoard
from getInfo import info

print("\n\t       TIC TAC TOE\n")
# Get information to start the game
boardSize, winningList, player1, player2 = info()

# Print the board reference
print("\tIntructions")
print("Choose the number where you wanna put your piece")
print("Starts the player who chose X")
board = getBoard(boardSize)
#print(winningList)
game(boardSize,winningList, player1, player2)

