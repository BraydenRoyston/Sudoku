"""
Sudoku by Brayden Royston

Sudoku is classically a game where a 9 x 9 grid is split up into 9 equal boxes of 9
squares. To complete the puzzle, the number 1-9 must appear once in every row,
column, and box.

***
the datatype Board is a 2D list of Int
***
"""

import board_functions
import check_functions

"""
solve(board)

This function utilizes the function from "board_functions" as well as "check_functions"
to traverse and solve a Sudoku board using backtracking recursion.

Contract
solve: Board -> Board
"""


def solve(board):
    next_coord = board_functions.locateEmpty(board)
    if next_coord:
        row, column = next_coord
    else:
        return True

    for i in range(1, 10):
        if check_functions.checkBox(check_functions.getBox(board, [row, column]), i) and \
                check_functions.checkRow(board, [row, column], i) and \
                check_functions.checkColumn(board, [row, column], i):
            board[row][column] = i

            if solve(board):
                return board

            else:
                board[row][column] = 0

    return False


