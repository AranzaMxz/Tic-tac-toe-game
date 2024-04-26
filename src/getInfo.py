from board.board_info import getBoardSize
from data.winData import winPlays
from data.playersData import getData


def info():
    # Determinate the board size
    boardSize = getBoardSize()

    # Determinate the plays winners
    winList = winPlays(boardSize)

    # Get players information
    player1,player2 = getData() 
    print()
    player1.showData()
    player2.showData()

    return boardSize, winList, player1, player2
