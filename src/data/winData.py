
def winPlays(n):
    winList = []
    # Rows and columns
    for i in range(n): # values from 0 to n-1
        row = [(i, j) for j in range(n)]
        column = [(j, i) for j in range(n)]
        winList.append(row)
        winList.append(column)

    # Diagonals
    diagonal1 = [(i, i) for i in range(n)]
    diagonal2 = [(i, n - i - 1) for i in range(n)]
    winList.append(diagonal1)
    winList.append(diagonal2)

    return winList