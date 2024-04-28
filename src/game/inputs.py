from game.rules import isFree
from game.rules import inputAccepted

# Verificate the input
def nextSelection(nextPlayer, boardSize):
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