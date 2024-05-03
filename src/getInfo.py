from board.board_info import getBoardSize
from data.winningData import winningPlays
from data.playersData import getData


def info(mode):
    # Determinate the board size
    boardSize = getBoardSize()

    # Determinate the winners plays
    winningList = winningPlays(boardSize)

    # Get players information
    player1,player2 = getData(mode) 
    print()
    player1.showData()
    player2.showData()

    return boardSize, winningList, player1, player2
