import os

# Colour Pallette + RESET
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m' # called to return to standard terminal text color

# Connect Four board dimensions
columns = 7
rows = 6
connect_four_board = [[0 for _ in range(columns)] for _ in range(rows)]

def index_to_checker(board, row, column):
    if board[row][column] == 0:
        return ' '
    elif board[row][column] == 1:
        return RED+'X'+RESET
    elif board[row][column] == 2:
        return BLUE+'O'+RESET

def print_board(board):
    # Print the board from the top row to the bottom row
    for row in range(rows):
        for column in range(columns):
            x = index_to_checker(board, row, column)
            print(GREEN+" [ "+RESET+x+GREEN+" ] "+RESET, end='')
        print()
    print("   1      2      3      4      5      6      7\n")

def get_input():
    print("Choose the column number where you would like to place your checker (1-7):")
    while True:
        try:
            player_move = int(input("> "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if player_move < 1 or player_move > 7:
            print("Move is out of bounds, please enter a number between 1 and 7.")
            continue
        else:
            return player_move - 1