
# Verificate the input is allow
def getBoardSize():
    while True:
        try:
            size = int(input("\nWrite the board size (min 3): "))
            if size >= 3:    
                return size
            print("The minimum is 3. Try again\n")
        except ValueError:
            print("That´s not allowed! Try again")
