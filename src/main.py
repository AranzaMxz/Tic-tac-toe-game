from game.game import game
from board.printBoard import getBoard
from getInfo import info

print("---------------------------------------------------")
print("\n\t             TIC TAC TOE  \n")
print("---------------------------------------------------")
print("\t         Instructions")
print("1. Enter the board size")
print("2. Enter the players' name")
print("3. Player 1 chooses his piece")
print("4. Choose the number where you wanna put your piece")
print("5. Starts the player who chose X")
print("6. THE PLAYER WHO COMPLETES n PIECES TOGETHER WINS")
print("----- If you want to play against the computer, type COMPUTER on the second player's name -----")

# Get information to start the game
boardSize, winningList, player1, player2 = info()

# Print the board reference
board = getBoard(boardSize)

# Start the game
game(boardSize,winningList, player1, player2)

