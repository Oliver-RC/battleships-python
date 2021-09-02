# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def game(n):
    """
    create the minesweeper board size
    """
    board = [[0 for row in range(n)] for column in range(n)]
    for row in board:
        print(" ".join(str(cell) for cell in row))
        print("")

if __name__ == "__main__":
    """identifies this file as the main module"""
    game(5)