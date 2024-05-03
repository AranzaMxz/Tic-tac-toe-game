from data.playerInfo import player

# Get what piece gonna choose each player
def getPiece(name1):
    figureP1 = input("\n"+ name1 + " choose X or O:")
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
    
def getNames(mode):
    # Get the names of players
    print("\n\t    Player 1")
    while True:
        name1 = input("Enter your name (max 10 characters, no spacing):")
        if len(name1) > 10:
            print("Too long! Try again")
        elif not name1.isalpha(): # vefify names contains only a-z chars
            print("Invalid input! Please, enter a valid name")
        else:
            print("\n\t    Player 2")
            while True:
                if mode == 1:
                    name2 = input("Enter your name (max 10 characters, no spacing):")  
                    if len(name2) > 10:
                        print("Too long! Try again")
                    elif not name2.isalpha():
                        print("Invalid input! Please, enter a valid name")
                    else:
                        break
                elif mode == 2:
                    name2 = "Computer"
                    print("Player's 2 name: ", name2)
                    break
            return name1,name2

def getData(mode):
    name1, name2 = getNames(mode)
    pieceP1,pieceP2 = getPiece(name1)

    player1 = player("1", name1, pieceP1)
    #player1.showData()

    player2 = player("2", name2, pieceP2)
    #player2.showData()

    return player1,player2

