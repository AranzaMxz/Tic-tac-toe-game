
def winPlays(n):
    winList = []
    # Rows and columns
    for i in range(n): # values from 0 to n-1
        row = [n * i + j + 1  for j in range(n)]
        column = [n * j + i + 1 for j in range(n)]
        winList.append(row)
        winList.append(column)

    # Diagonals
    diagonal1 = [n * i +  i + 1 for i in range(n)]
    diagonal2 = [n * i + (n - i) for i in range(n)]
    winList.append(diagonal1)
    winList.append(diagonal2)

    return winList