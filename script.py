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