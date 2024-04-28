
# Verificate the enter number is in the range 
def inputAccepted(selection, boardSize):
    if selection > boardSize**2 or selection < 1:
        print("Your selection is out of range. Try again")
    else:
        return True

def isFree(row, col, values):
    if values[row][col] == '  ':
        return True
    else:
        return False