import numpy as np
import random

#Allow user input for board
val = input ("How many rows/columns? ")
board =  [[0]*val for i in range(val)]
for row in range (val):
    for col in range (val):
        board[row][col] = input("What number is in row " + row + " and column " + col + "? If the space is empty, enter 0. ")

def check_valid(board, value, index):

    #Check down column
    for row in range(board.shape[0]):
        if value == board[row][index[1]]:
            return False
    
    #Check across row
    for col in range(board.shape[1]):
        if value == board[index[0]][col]:
            return False
    
    # check in 3x3 grid
    if board.shape[0] == 9 and board.shape[1] == 9:
        #Only do this check for 9x9 boards
        if index[0] <= 2 and index[1] <=2:
            for row in range(0,3):
                for col in range(0,3):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 2 and index[0] <=5) and index[1] <=2:
            print(index, 'Test')
            for row in range(3,6):
                for col in range(0,3):
                    if board[row][col] == value:
                        print('false')
                        return False

        elif (index[0] > 5 and index[0] <=8) and index[1] <=2:
            for row in range(6,9):
                for col in range(0,3):
                    if board[row][col] == value:
                        return False

        elif index[0] <= 2 and (index[1] >2 and index[1] <= 5):
            for row in range(0,3):
                for col in range(3,6):
                    if board[row][col] == value:
                        return False

        elif index[0] <= 2 and (index[1] >5 and index[1] <= 8):
            for row in range(0,3):
                for col in range(6,9):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 2 and index[0]<=5 ) and (index[1] >2 and index[1] <= 5):
            for row in range(3,6):
                for col in range(3,6):
                    if board[row][col] == value:
                        return False
        
        elif (index[0] > 2 and index[0]<=5 ) and (index[1] >5 and index[1] <= 8):
            for row in range(3,6):
                for col in range(6,9):
                    if board[row][col] == value:
                        return False

        elif (index[0] > 5 and index[0]<=8 ) and (index[1] >2 and index[1] <= 5):
            for row in range(6,9):
                for col in range(3,6):
                    if board[row][col] == value:
                        return False
        
        elif (index[0] > 5 and index[0]<=8 ) and (index[1] >5 and index[1] <= 8):
            for row in range(6,9):
                for col in range(6,9):
                    if board[row][col] == value:
                        return False
    return True

def solve(board):
    #Check for empty blocks
    empty = False

    for row in range(board.shape[0]):
        if empty == True:
            break
        for col in range(board.shape[1]):
            if board[row][col] == 0:
                empty = True
                index = [row,col]
                break

    if empty == False:
        return True

    for n in range(1, board.shape[0] + 1):
        if check_valid(board, n, index):
            board[index[0]][index[1]] = n
            if solve(board):
                #Backtracking
                return True
            board[index[0]][index[1]] = 0
            
    return False

solve(board)
print(board)
