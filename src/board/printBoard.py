import numpy as np

def getValues(size):
    values = []
    numValues = size**2

    # Get the values 
    for i in range(numValues):
        if i < 9:
            values.append(f"{i+1} ")
        else:
            values.append(i+1)
    
    values = np.array(values)
    valuesMatrix = values.reshape(-1,size)

    #print(valuesMatrix)
    return valuesMatrix

def print_Board(size, values):
    print("\n")
    
    for i in range(size):
        # First row and secuences
        if i != size-1:
            print()
            for j in range(size-1):
                print("\t      |", end="")
            print()
            for j in range(size):
                if j == size-1:
                    print("\t {}".format(values[i,j]), end="")
                else:
                    print("\t  {}  |".format(values[i,j]), end="")
            print()
            for j in range(size-1):
                if j == 0:
                    print("\t _ _ _|", end="")
                if j == size-2:
                    print("_ _ _", end="")    
                else:
                    print("_ _ _ _|", end="")
        # Last row
        else:
            print()
            for j in range(size-1):
                print("\t      |", end="")
            print()
            for j in range(size):
                if j == size-1:
                    print("\t {}".format(values[i,j]), end="")
                else:
                    print("\t  {}  |".format(values[i,j]), end="")
            print()
            for j in range(size-1):
                print("\t      |", end="")
            print("\n")

def getBoard(size):
    #matrix = matrixCreate(size)
    values = getValues(size)
    print_Board(size, values)
    #return matrix
#getMatrix(5)
