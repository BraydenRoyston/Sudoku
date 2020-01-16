import random

"""
createBoard(size)

This function takes an input of a board size and then outputs the board.

***
the datatype Board is a 2D list of Int

the datatype Coord is an List[Int, Int] where List[0] is the row number and List[1] is the column number.
***

"""



"""
locateEmpty(board)

This function takes an input of a board and searches it for an empty square. Searches an entire row
before moving onto the next row.

Contract
locateEmpty: Board -> Coord
"""

def locateEmpty(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    else:
        return None


"""
printBoard(board)

This function takes an input of a Board and outputs it in a fashion that is easier to read.

"""




def printBoard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            print(board[i][j], end=' ')
        print()


"""
createRandomBoard(difficulty)

This function takes an input of a difficulty and then creates a new sudoku board regarding
that specified difficulty.

Contract
createRandomBoard: Int -> Board
"""





def createRandomBoard(difficulty):
    # The number of numbers given based on difficulty
    numbersGiverPerRow1 = 3
    numbersGiven_2 = 2
    numbersGiven_3 = 1
    board = []
    
    if difficulty == 1:
        for i in range(0, 9):
            numPos_1 = [random.randint(1, 3), random.randint(0, 8)]
            numPos_2 = [random.randint(4, 6), random.randint(0, 8)]
            numPos_3 = [random.randint(7, 9), random.randint(0, 8)]
            for i in range(0, 9):
                if i == numPos_1[1]:
                    return numPos_1[0]
                elif i == numPos_2[1]:
                    return numPos_2[0]
                elif i == numPos_3[1]:
                    return numPos_3[0]
                else:
                    return i
        return board


