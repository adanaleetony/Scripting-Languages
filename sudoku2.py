def isValid(board, row, col, num):
    # Satırı kontrol et
    for x in range(9):
        if board[row][x] == num:
            return False

    # Sütunu kontrol et
    for x in range(9):
        if board[x][col] == num:
            return False

    # 3x3 kutuyu kontrol et
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solveSudoku(board):
    emptySpot = findEmptySpot(board)
    if not emptySpot:
        return True
    else:
        row, col = emptySpot

    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num

            if solveSudoku(board):
                return True

            board[row][col] = 0

    return False

def findEmptySpot(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def printBoard(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Sudoku örneği
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solveSudoku(board):
    print("Çözüm:")
    printBoard(board)
else:
    print("Bu Sudoku çözülemez.")
