# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def game_board(n, b):
    """
    creates the minesweeper board size and place mines at random on the board 
    with neighbouring cells increasing their values to 1
    """
    print("\n* Minesweeper *\n\nThe aim of the game is to dig up all cells\nwithout hitting the mines,\nGOOD LUCK!\n ")
    
    board = [[0 for row in range(n)] for column in range(n)]

    for num in range(b):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        board[y][x] = '*' # mine symbol

        if (x >= 1 and x <= n - 1) and (y >= 0 and y <= n - 1):
            if board[y][x - 1] != '*':
                board[y][x - 1] += 1 # center left        
        
        if (x >= 0 and x <= n - 2) and (y >= 0 and y <= n - 1):
            if board[y][x + 1] != '*':
                board[y][x + 1] += 1 # center right

        if (x >= 1 and x <= n - 1) and (y >= 1 and y <= n - 1):
            if board[y - 1][x - 1] != '*':
                board[y - 1][x - 1] += 1 # top left
 
        if (x >= 0 and x <= n - 2) and (y >= 1 and y <= n - 1):
            if board[y - 1][x + 1] != '*':
                board[y - 1][x + 1] += 1 # top right

        if (x >= 1 and x <= n - 1) and (y >= 0 and y <= n - 2):
            if board[y + 1][x - 1] != '*':
                board[y + 1][x - 1] += 1 # bottom left

        if (x >= 0 and x <= n - 2) and (y >= 0 and y <= n - 2):
            if board[y + 1][x + 1] != '*':
                board[y + 1][x + 1] += 1 # bottom right

        if (x >= 0 and x <= n - 1) and (y >= 1 and y <= n - 1):
            if board[y - 1][x] != '*':
                board[y - 1][x] += 1 # top center

        if (x >= 0 and x <= n - 1) and (y >= 0 and y <= n - 2):
            if board[y + 1][x] != '*':
                board[y + 1][x] += 1 # bottom center

    return board

def player_board(n):
    """
    player board to display whilst playing the game
    """
    board = [['-' for row in range(n)] for column in range(n)]

    return board

def display_map(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

def check_win(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True

def continue_game(score):
    print("Your Score:", score)
    to_continue = input("Do you want to try again? (y/n) :")
    if to_continue == 'n':
        return False
    return True

def play_game():
    status = True
    while status:
        difficulty = input("Select your difficulty (easy, normal, hard):")
        if difficulty.lower() == 'easy':
            n = 5
            b = 3
        elif difficulty.lower() == 'normal':
            n = 6
            b = 8
        elif difficulty.lower() == 'hard':
            n = 8
            b = 20        
        else:
            print("Wrong input, please try again typing either: easy, normal or hard")

        minesweeper_map = game_board(n, b)
        player_map = player_board(n)
        score = 0

        while True:
            if check_win(player_map) == False:
                print("Enter the location of your dig:")
                x = input("Column:")
                y = input("Row:")
                x = int(x) - 1
                y = int(y) - 1

                if (minesweeper_map[y][x] == '*'):
                    print("Game Over")
                    display_map(minesweeper_map)
                    status = continue_game(score)
                    break
                
                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    display_map(player_map)
                    score += 1

            else:
                display_map(player_map)
                print("You Win!")
                status = continue_game(score)
                break

if __name__ == "__main__":
    """identifies this file as the main module and runs the game"""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nEnd of the game. Thanks for playing!")