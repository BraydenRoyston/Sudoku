import check_functions
import board_functions
import main

board = [[0 for i in range(0, 9)] for i in range(0, 9)]

test_board = [[1, 0, 0, 8, 0, 3, 0, 5, 0],
              [0, 3, 0, 6, 0, 0, 4, 0, 2],
              [0, 0, 2, 0, 0, 0, 0, 3, 0],
              [8, 0, 5, 0, 0, 1, 0, 7, 0],
              [0, 0, 6, 0, 7, 0, 5, 0, 8],
              [0, 0, 7, 0, 0, 0, 0, 6, 0],
              [0, 0, 0, 0, 0, 4, 0, 0, 0],
              [9, 4, 1, 0, 6, 3, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 4]]


def printBoard(board):
    w = 0
    z = 0

    for i in range(0, 9):
        print("------------------------")
        w += 1
        for j in range(0, 9):
            if j == 8:
                print(str(board[i][j]) + " |", end = ' ')
            else:
                if z % 3 == 0:
                    z += 1
                    print("| " + str(board[i][j]), end = ' ')
                else:
                    z += 1
                    print(board[i][j], end = ' ')


# print(printBoard(test_board))

# print(check_functions.checkRow(board, [1, 1], 7))
# print(check_functions.checkColumn(board, [1, 1], 7))
# print(check_functions.getBox(board, [1, 1]))
# print(check_functions.checkBox(check_functions.getBox(board, [1, 1]), [1, 1]))
# print(board_functions.locateEmpty(test_board))

# print(main.solve(test_board))

print(printBoard(test_board))
print(printBoard(main.solve(test_board)))
