from itertools import permutations

# Verificate the enter number is in the range 
def inputAccepted(selection, boardSize):
    if selection > boardSize**2 or selection < 1:
        print("Your selection is out of range. Try again")
        return False
    else:
        return True

# Check if the space is free
def isFree(row, col, values):
    if values[row][col] == '  ':
        return True
    else:
        return False

# Check if the board is full
def isFull(values, sizeWinner):
    cont = 0 
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i][j] != '  ':
                cont += 1
    
    if cont == sizeWinner ** 2: # The board is full
        return True
    else:
        return False
    
# Conditions to win
def checkWin( moves, winningList, sizeWinner):
    # Generate all permutations of 3 moves
    move_permutations = permutations(moves, sizeWinner)

    # Check if any permutation is in the list of winning plays
    for move_perm in move_permutations:
        #print("Movements: ", move_perm)
        if list(move_perm) in winningList:
            #print("Movement found: ", move_perm)
            return True
    return False

# Game over conditions        
def gameOver (values, player, moves,  winningList, sizeWinner):
    if len(moves) < sizeWinner:
        return False
    else:
        if checkWin(moves, winningList, sizeWinner):
            print("Congratulations " + player.name + ", you won!")
            return True
        elif isFull(values, sizeWinner):
            print("No one won, it´s a tie")
            return True
        return False