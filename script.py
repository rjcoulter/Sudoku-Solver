# function to print the board on to the console
def printBoard(board):
    print("*********************")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*********************")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("*", end=" ")
            print(board[x][y], end=" ")
        print()
    print("*********************")

# A function that will check to see if the board is full
# 0 denotes an empty space, so it will return false if an empty space is
# found and true if there are no empty spaces
def isFull(board):
    for x in range(0, 9):
        for y in range(0, 9):
            if board[x][y] == 0:
                return False
    return True

# A function which finds all of the possible numbers that can be
# put at a specific location by checking the horizontal and 
# vertical entries, and the 3x3 square the entry is inside.
# An key that maps to value 0 in the dict will be a possible value.
def possibleEntries(board, i, j):
    possibleArray = {}

    # Maps numbers 1-9 to have a value of 0 intially
    for x in range(1, 10):
        possibleArray[x] = 0

    # Horizontal Entries
    for y in range(0, 9):
        if not board[i][y] == 0:
            possibleArray[board[i][y]] = 1

    # Vertical Entries
    for x in range(0, 9):
        if not board[x][j] == 0:
            possibleArray[board[x][j]] = 1
    
    # For each 3x3 square, starts at top left
    k = 0
    l = 0

    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6

    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6

    for x in range(k, k + 3):
        for y in range(l, l + 3):
            if not board[x][y] == 0:
                possibleArray[board[x][y]] = 1

    for x in range(1, 10):
        if possibleArray[x] == 0:
            possibleArray[x] = x
        else:
            possibleArray[x] = 0

    return possibleArray


# A function that solves to puzzle recursively and then 
# prints it
def solver(board):
    i = 0
    j = 0

    possibilities = {}

    # Base case
    if isFull(board):
        print("The puzzle has been solved")
        printBoard(board)
        return
    else:
        # Find first vacant spot
        for x in range(0, 9):
            for y in range(0, 9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
                else:
                    continue
                break
        
        # Get all the possibilities for i and j
        possibilities = possibleEntries(board, i, j)

        # Iterate through the possibilites and keep calling the function
        for x in range(1, 10):
            if not possibilities[x] == 0:
                board[i][j] = possibilities[x]
                solver(board)
        board[i][j] = 0

# Manually intantiate the 2D array that acts as the board
def driver():
    SudokuBoard = [[0 for x in range(9)] for x in range(9)] 
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0
    SudokuBoard[0][3] = 3
    SudokuBoard[0][4] = 0
    SudokuBoard[0][5] = 0
    SudokuBoard[0][6] = 2
    SudokuBoard[0][7] = 0
    SudokuBoard[0][8] = 0
    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 0
    SudokuBoard[1][2] = 0
    SudokuBoard[1][3] = 0
    SudokuBoard[1][4] = 0
    SudokuBoard[1][5] = 8
    SudokuBoard[1][6] = 0
    SudokuBoard[1][7] = 0
    SudokuBoard[1][8] = 0
    SudokuBoard[2][0] = 0
    SudokuBoard[2][1] = 7
    SudokuBoard[2][2] = 8
    SudokuBoard[2][3] = 0
    SudokuBoard[2][4] = 6
    SudokuBoard[2][5] = 0
    SudokuBoard[2][6] = 3
    SudokuBoard[2][7] = 4
    SudokuBoard[2][8] = 0
    SudokuBoard[3][0] = 0
    SudokuBoard[3][1] = 4
    SudokuBoard[3][2] = 2
    SudokuBoard[3][3] = 5
    SudokuBoard[3][4] = 1
    SudokuBoard[3][5] = 0
    SudokuBoard[3][6] = 0
    SudokuBoard[3][7] = 0
    SudokuBoard[3][8] = 0
    SudokuBoard[4][0] = 1
    SudokuBoard[4][1] = 0
    SudokuBoard[4][2] = 6
    SudokuBoard[4][3] = 0
    SudokuBoard[4][4] = 0
    SudokuBoard[4][5] = 0
    SudokuBoard[4][6] = 4
    SudokuBoard[4][7] = 0
    SudokuBoard[4][8] = 9
    SudokuBoard[5][0] = 0
    SudokuBoard[5][1] = 0
    SudokuBoard[5][2] = 0
    SudokuBoard[5][3] = 0
    SudokuBoard[5][4] = 8
    SudokuBoard[5][5] = 6
    SudokuBoard[5][6] = 1
    SudokuBoard[5][7] = 5
    SudokuBoard[5][8] = 0
    SudokuBoard[6][0] = 0
    SudokuBoard[6][1] = 3
    SudokuBoard[6][2] = 5
    SudokuBoard[6][3] = 0
    SudokuBoard[6][4] = 9
    SudokuBoard[6][5] = 0
    SudokuBoard[6][6] = 7
    SudokuBoard[6][7] = 6
    SudokuBoard[6][8] = 0
    SudokuBoard[7][0] = 0
    SudokuBoard[7][1] = 0
    SudokuBoard[7][2] = 0
    SudokuBoard[7][3] = 7
    SudokuBoard[7][4] = 0
    SudokuBoard[7][5] = 0
    SudokuBoard[7][6] = 0
    SudokuBoard[7][7] = 0
    SudokuBoard[7][8] = 0
    SudokuBoard[8][0] = 0
    SudokuBoard[8][1] = 0
    SudokuBoard[8][2] = 9
    SudokuBoard[8][3] = 0
    SudokuBoard[8][4] = 0
    SudokuBoard[8][5] = 5
    SudokuBoard[8][6] = 0
    SudokuBoard[8][7] = 0
    SudokuBoard[8][8] = 0
    printBoard(SudokuBoard)
    solver(SudokuBoard)


driver()