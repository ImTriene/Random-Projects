'''
Sudoku rules:
    - Uses numbers 1-9, 0 represents an empty square
    - Only allowed 1 of each digit in each row, column and 3x3 box. 
Need to utilize lists to create the playing game for the computer to 
read. Using a "list of lists" or a 2D array basically.

Need to use a back tracking algorithm to brute force it's way
through the puzzle that utilizes recursion. 

The back tracking algorithm follows steps of:
1. finding an empty square
2. trying all possible values
3. moving onto the next square
4. Repeat
5. Back track - go back and fix numbers such that it finds a new possible solution. it will continue back tracking until a line is correct and move on.
'''

import numpy as np

# Define the board as board - 9x9 array. 0's represent empty spaces
# Empy for reference [0, 0, 0, 0, 0, 0, 0, 0, 0],
# Current puzzle labeled "Expert"

board = [[0, 0, 7, 9, 3, 0, 0, 0, 8],
[6, 8, 0, 0, 0, 5, 0, 9, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 4, 0, 0, 0, 8, 0],
[5, 0, 0, 1, 0, 6, 0, 3, 0],
[0, 6, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 5, 4, 0, 0, 0],
[0, 0, 9, 7, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 7, 0]]

# We can use numpy to make the board look better when output
# print(np.matrix(board))

# Need to define a function that determines whether or not a number can be input. It needs to go throughout the board and input a number 1-9
# Therefore it should have 3 parameters - x, y, n
# Need to remember that python index starts at 0, so the board runs from 0 to 8

def rules(x, y, n):
    global board # States that board is allowed everywhere
    for i in range(len(board)):
        if board[x][i] == n: # Setting up the rules for the game. This says as you go through x, if the input value equals a value in the list, it's wrong
            return False
    for i in range(len(board)):
        if board[i][y] == n: # Same thing as previously, but now for y values.
            return False
    # Now we need to define it for the 3x3 square
    x_0 = (x // 3)*3
    y_0 = (y // 3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[x_0 + i][j + y_0] == n:
                return False
    return True

# Writing the backtracking algorithm
def backtrack():
    global board
    for x in range(9): # For x values of 0 to 8
        for y in range(9): # For y values of 0 to 8
            if board[x][y] == 0: # If the value at position (x,y) is zero then for our number from 1-9 see if any of the numbers work.
                for n in range(1, 10): 
                    if rules(x, y, n): # Includes the rules component of the puzzle
                        board[x][y] = n
                        backtrack() # Calls the function again
                        board[x][y] = 0
                return # Takes it back and runs it again
    print(np.matrix(board))
    input('Try Another?')
print(backtrack())












