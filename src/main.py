from game.game import game
from board.printBoard import getBoard
from getInfo import info
from game.rules import isNumber

print("---------------------------------------------------")
print("\n\t             TIC TAC TOE  \n")
print("---------------------------------------------------")
print("Choose the game mode")
print("1. Player vs player\n2. Player vs computer\n")
mode = isNumber()

print("\t         Instructions")
print("1. Enter the board size")
print("2. Enter the names players")
print("3. Player 1 chooses him piece")
print("4. Choose the number where you wanna put your piece")
print("5. Starts the player who chose X")
print("6. THE PLAYER WHO COMPLETES n PIECES TOGETHER WINS")

# Get information to start the game
boardSize, winningList, player1, player2 = info(mode)

# Print the board reference
board = getBoard(boardSize)

# Start the game
game(boardSize,winningList, player1, player2)

