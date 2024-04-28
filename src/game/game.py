import math
from itertools import combinations
from data.playersData import getData
from game.startGame import start
from board.printBoard import print_Board
from game.rules import isFree
from data.playerInfo import player
from game.rules import inputAccepted


def nextSelection(nextPlayer, boardSize):
    while True:
            try:
                selection = int(input (nextPlayer.name + ": "))
                if inputAccepted(selection, boardSize):
                    return selection
            except ValueError:
                print("Only numbers! Try again")
def checkWin( moves, winList):
    # Generate all combinations of 3 moves
    move_combinations = combinations(moves, 3)

    print(move_combinations)
    # Check if any combination is in the list of winning combinations
    for move_comb in move_combinations:
        if set(move_comb) in winList:
            return True
        
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
    
def gameOver (values, player, moves,  winList, sizeWinner):
    if len(moves) < 3:
        print(len(moves))
        return False
    else:
        if checkWin( moves, winList):
            print("Congratulations " + player.name + "you won!")
            return True
        elif isFull(values, sizeWinner):
            print("No one won, it´s a tie")
            return True
        return False
    
#from Data import player
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
    

def game(boardSize, winList, player1, player2):
    global values
    print("\n\t    LET´S START\n")
    # Determinate who starts the game
    selection, values, player = start(boardSize, player1, player2)
    putPiece(boardSize, selection, values, player) # Put the first piece in the board
    print(player.name + " you chose ", selection)
    print_Board(boardSize, values) 

    # Determinate the next player
    if player == player1: # The first player is the player 1
        player1.moves.append(selection) # Add the selection of current player
        moves = player1.moves # Save the moves 
        nextPlayer = player2 # Change the current plauer
    else: # The first player is the player 2
        player2.moves.append(selection)
        nextPlayer = player1
        moves = player2.moves
        
    print(" Next player: " + nextPlayer.name  )
    #turn (boardSize, player)

    while not gameOver(values, player, moves, winList, boardSize):
        print("player " + player.nplayer + " moves: ", player.moves)
        print("player " + nextPlayer.nplayer + " moves: ", nextPlayer.moves)

        selection = nextSelection(nextPlayer, boardSize) # Get the next selection
        print(nextPlayer.name + " you chose ", selection)

        if not putPiece(boardSize, selection, values, nextPlayer):
            print("Place already filled. Try again")
        else:
            print_Board(boardSize, values)

            # Add the move to the player's list of moves
            if nextPlayer == player1:
                player = player1
                player1.moves.append(selection)
                nextPlayer = player2
            else:
                player = player2
                player2.moves.append(selection)
                nextPlayer = player1

        



