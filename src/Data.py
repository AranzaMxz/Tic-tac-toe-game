from playerInfo import player

# Get what piece gonna hace each player
def getPiece(name1):
    figureP1 = input(name1 + " choose X or O:")
    figureP2 = None
    if figureP1 == "X" or figureP1 == "O":
        if figureP1 == "X":
            figureP2 = "O"
        else:
            figureP2 = "X"
    else:
        print("That´s not a choice " + name1 + ", try again")
        return getPiece(name1) # Return the result of recursive call

    return figureP1,figureP2
    
def getData():
    # Get the names of players
    name1 = input("Enter name of player 1:")
    name2 = input("Enter name of player 2:")   

    pieceP1,pieceP2 = getPiece(name1)

    player1 = player("1", name1, pieceP1)
    #player1.showData()

    player2 = player("2", name2, pieceP2)
    #player2.showData()

    return player1,player2

