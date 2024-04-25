from Data import getData
#from Data import player

def game():
    # Get players information
    player1,player2 = getData() 
    player1.showData()
    player2.showData()

