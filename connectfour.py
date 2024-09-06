import os

# Colour Pallette + RESET
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m' # called to return to standard terminal text color

player_one_wins = RED+"""
 __                 ___  __      __        ___                 __     
|__) |     /\  \ / |__  |__)    /  \ |\ | |__     |  | | |\ | /__`    
|    |___ /~~\  |  |___ |  \    \__/ | \| |___    |/\| | | \| .__/                                                                      
"""+RESET

player_two_wins = BLUE+"""
 __                 ___  __     ___       __                  __     
|__) |     /\  \ / |__  |__)     |  |  | /  \    |  | | |\ | /__`    
|    |___ /~~\  |  |___ |  \     |  |/\| \__/    |/\| | | \| .__/                                                                         
"""+RESET

# Victory bool
connect_four_victory = False

# Connect Four board dimensions
columns = 7
rows = 6
connect_four_board = [[0 for _ in range(columns)] for _ in range(rows)]

def print_gap(num):
    for _ in range(num):
        print()

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
        
def check_victory(board, player):
    def check_line(row, col, delta_row, delta_col):
        count = 0
        for _ in range(4):
            if 0 <= row < rows and 0 <= col < columns and board[row][col] == player:
                count += 1
                row += delta_row
                col += delta_col
            else:
                break
        return count == 4

    # Check horizontal, vertical, and diagonal directions
    for row in range(rows):
        for col in range(columns):
            if check_line(row, col, 0, 1):  # Check horizontal
                return True
            if check_line(row, col, 1, 0):  # Check vertical
                return True
            if check_line(row, col, 1, 1):  # Check positive slope diagonal
                return True
            if check_line(row, col, 1, -1): # Check negative slope diagonal
                return True
    return False

def place_checker(player_move, player):
    global connect_four_victory
    for i in range(rows - 1, -1, -1):  # Iterate from bottom to top, including row 0
        if connect_four_board[i][player_move] == 0:
            connect_four_board[i][player_move] = player
            if check_victory(connect_four_board, player):
                print_gap(40)
                if player == 1:
                    print(player_one_wins)
                elif player == 2:
                    print(player_two_wins)
                print_board(connect_four_board)
                connect_four_victory = True
            return
    print("Column full, try another column.")