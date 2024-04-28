from game.startGame import start
from board.printBoard import print_Board
from game.rules import gameOver
from game.inputs import putPiece
from game.inputs import nextSelection

    
def game(boardSize, winningList, player1, player2):
    global values
    print("\n\t    LET´S START\n")
    
    # Determinate who starts the game
    selection, values, player = start(boardSize, player1, player2)

    # Put the first piece in the board
    putPiece(boardSize, selection, values, player)
    
    # Print the board with the first piece
    print_Board(boardSize, values) 

    # Determinate the next player
    if player == player1: # The first player is the player 1
        player1.moves.append(selection) # Add the selection of current player
        moves = player1.moves # Save the moves of current player 
        nextPlayer = player2 # Change the current player
    else: # The first player is the player 2
        player2.moves.append(selection)
        nextPlayer = player1
        moves = player2.moves
    
    # Cicle of the game until game over is False
    while not gameOver(values, player, moves, winningList, boardSize):
        
        # Get the next selection
        selection = nextSelection(nextPlayer, boardSize) 
        #print(nextPlayer.name + " you chose ", selection)

        if not putPiece(boardSize, selection, values, nextPlayer):
            print("Place already filled. Try again")
        else:
            print_Board(boardSize, values)

            # Add the move to the player's list of moves
            if nextPlayer == player1:
                player1.moves.append(selection)
                moves = player1.moves
                player = player1
                nextPlayer = player2
            else:
                player2.moves.append(selection)
                moves = player2.moves
                player = player2
                nextPlayer = player1
                
    
    playAgain = input("\nWanna play again? y/n: ")
    while True:
        try:
            if playAgain == "y" or playAgain == "Y":
                player1.moves = []
                player2.moves = []
                game(boardSize, winningList, player1, player2)
            elif playAgain == "n" or playAgain == "N":
                print("Thanks for play!")
                break
            else:
                print("That´s not allow. Try again")
        except ValueError:
            print("That´s not allow! try again")

        



