# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def game(n, b):
    """
    creates the minesweeper board size and place mines at random on the board 
    with neighbouring cells increasing their values to 1
    """
    print("\nMinesweeper\n")
    
    board = [[0 for row in range(n)] for column in range(n)]

    for num in range(b):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        board[y][x] = '*'

        if (x >= 0 and x <= n - 2) and (y >= 0 and y <= n - 1):
            if board[y][x + 1] != '*':
                board[y][x + 1] += 1 # center right

        if (x >= 1 and x <= n - 1) and (y >= 0 and y <= n - 1):
            if board[y][x - 1] != '*':
                board[y][x - 1] += 1 # center left

        if (x >= 1 and x <= n - 1) and (y >= 1 and y <= n - 1):
            if board[y - 1][x - 1] != '*':
                board[y - 1][x - 1] += 1 # top left
 
        if (x >= 0 and x <= n - 2) and (y >= 1 and y <= n - 1):
            if board[y - 1][x + 1] != '*':
                board[y - 1][x + 1] += 1 # top right

        if (x >= 0 and x <= n - 1) and (y >= 1 and y <= n - 1):
            if board[y - 1][x] != '*':
                board[y - 1][x] += 1 # top center

        if (x >= 0 and x <= n - 2) and (y >= 0 and y <= n - 2):
            if board[y + 1][x + 1] != '*':
                board[y + 1][x + 1] += 1 # bottom right

        if (x >= 1 and x <= n - 1) and (y >= 0 and y <= n - 2):
            if board[y + 1][x - 1] != '*':
                board[y + 1][x - 1] += 1 # bottom left

        if (x >= 0 and x <= n - 1) and (y >= 0 and y <= n - 2):
            if board[y + 1][x] != '*':
                board[y + 1][x] += 1 # bottom center

    for row in board:
        print("\t".join(str(cell) for cell in row))
        print("")


if __name__ == "__main__":
    """identifies this file as the main module and runs the game"""
    game(5, 3) # Easy
