import numpy as np
from board.printBoard import print_Board
from game.rules import inputAccepted


def getValues(size):
    values = []
    numValues = size**2

    # List where we will have the pieces
    for i in range(numValues):
        values.append('  ') # Starts in blank
    
    values = np.array(values)
    valuesMatrix = values.reshape(-1,size) # We made it a matrix

    #print(valuesMatrix)
    return valuesMatrix


def start(boardSize, player1, player2):
    values = getValues(boardSize)
    print_Board(boardSize, values)
    # We start with the player who chose X
    if player1.piece == "X":
        while True:
            try:
                selection = int(input (player1.name + ": "))
                if inputAccepted(selection, boardSize):
                    return selection,values, player1
            except ValueError:
                print("Only numbers! Try again")

    else:
        while True:
            try:
                selection = int(input (player2.name + ": "))
                if inputAccepted(selection, boardSize):
                    return selection, values, player2
            except ValueError:
                print("Only numbers! Try again")