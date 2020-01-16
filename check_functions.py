"""

"check" functions

Given a sudoku board and an new number placement, these functions check if any rules have been broken.

***
the datatype Board is a 2D list of Int

the datatype Coord is an List[Int, Int] where List[0] is the row number and List[1] is the column number.
***

"""


"""
checkRow(board, coordinate, number)

Checks if the given number being placed at the given coordinate results in a valid row.

Contract:
checkRow: Board Coord Int -> Bool
"""

def checkRow(board, coordinate, number):
    for i in range(0, len(board)):
        if i != coordinate[1] and board[coordinate[0]][i] == number:
            return False
    else:
        return True

"""
checkColumn(board, coordinate, number)

Checks if the given number being placed at the given coordinate results in a valid column.

Contract:
checkColumn: Board Coord Int -> Bool
"""

def checkColumn(board, coordinate, number):
    for i in range(0, len(board)):
        if i != coordinate[1] and board[i][coordinate[1]] == number:
            return False
    else:
        return True

"""
getBox(board, coordinate)

This function creates a list of all of the numbers within the box of a given coordinate.

Contract:
getBox: Board Coord -> List[Int]
"""

def getBox(board, coordinate):
    box_X = coordinate[1] // 3
    box_Y = coordinate[0] // 3
    boxNumbers = []

    for i in range(box_X * 3, box_Y + 3):
        for j in range(box_Y * 3, box_X + 3):
            boxNumbers.append(board[i][j])
    return boxNumbers

"""
checkBox(board, coordinate, number)

Checks if the given number being placed at the given coordinate results in a valid box.

Contract:
checkBox: Board Coord Int -> Bool
"""

def checkBox(boxNumbers, number):
    for i in range(0, len(boxNumbers)):
        if boxNumbers[i] == number:
            return False
    else:
        return True

