
# Verificate the enter number is in the range 
def verificateSelection(selection, boardSize):
    if selection > boardSize**2:
        print("Your selection is out of range. Try again")
    else:
        return True