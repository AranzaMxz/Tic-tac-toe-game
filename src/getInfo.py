from board.board_info import getBoardSize
from data.winningData import winningPlays
from data.playersData import getData


def info():
    # Determinate the board size
    boardSize = getBoardSize()

    # Determinate the plays winners
    winningList = winningPlays(boardSize)

    # Get players information
    player1,player2 = getData() 
    print()
    player1.showData()
    player2.showData()

    return boardSize, winningList, player1, player2
