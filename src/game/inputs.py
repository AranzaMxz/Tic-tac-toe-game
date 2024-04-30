import random
from game.rules import isFree
from game.rules import inputAccepted

# Verify the input
def nextSelection(nextPlayer, boardSize):
    # If you are playing against a computer, it will fetch the board size and return a random number of integers 
    # depending on the size in order to choose its next move
    if nextPlayer.name == "COMPUTER":
        total_cells = boardSize * boardSize
        return random.randint(1, total_cells)
    else:
        while True:
                try:
                    selection = int(input (nextPlayer.name + ": "))
                    if inputAccepted(selection, boardSize):
                        return selection
                except ValueError:
                    print("Only numbers! Try again")
    
# Put piece in the selected place
def putPiece(boardSize, selection, values, player):
    row = (selection - 1) // boardSize # module
    col = (selection - 1) % boardSize # round down
    #print("row: ", row, " col: ", col)
    if isFree(row, col, values):
        values[row][col] = player.piece + " "
        #print(values)
        return True
    else:
        return False