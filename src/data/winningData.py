
def winningPlays(n):
    winningList = []
    # Rows and columns
    for i in range(n): # values from 0 to n-1
        row = [n * i + j + 1  for j in range(n)]
        column = [n * j + i + 1 for j in range(n)]
        winningList.append(row)
        winningList.append(column)

    # Diagonals
    diagonal1 = [n * i +  i + 1 for i in range(n)]
    diagonal2 = [n * i + (n - i) for i in range(n)]
    winningList.append(diagonal1)
    winningList.append(diagonal2)

    return winningList