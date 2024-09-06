import os

# ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'  # Resets the text color to default

# Connect Four messages
connect_four_message = GREEN + """
   ______     ___     ____  _____   ____  _____   ________     ______   _________     ________     ___     _____  _____   _______     
 .' ___  |  .'   `.  |_   \|_   _| |_   \|_   _| |_   __  |  .' ___  | |  _   _  |   |_   __  |  .'   `.  |_   _||_   _| |_   __ \    
/ .'   \_| /  .-.  \   |   \ | |     |   \ | |     | |_ \_| / .'   \_| |_/ | | \_|     | |_ \_| /  .-.  \   | |    | |     | |__) |   
| |        | |   | |   | |\ \| |     | |\ \| |     |  _| _  | |            | |         |  _|    | |   | |   | '    ' |     |  __ /    
\ `.___.'\ \  `-'  /  _| |_\   |_   _| |_\   |_   _| |__/ | \ `.___.'\    _| |_       _| |_     \  `-'  /    \ \__/ /     _| |  \ \_  
 `.____ .'  `.___.'  |_____|\____| |_____|\____| |________|  `.____ .'   |_____|     |_____|     `.___.'      `.__.'     |____| |___| 
""" + RESET

player_one_wins = RED + """
 __                 ___  __      __        ___                 __     
|__) |     /\  \ / |__  |__)    /  \ |\ | |__     |  | | |\ | /__`    
|    |___ /~~\  |  |___ |  \    \__/ | \| |___    |/\| | | \| .__/                                                                      
""" + RESET

player_two_wins = BLUE + """
 __                 ___  __     ___       __                  __     
|__) |     /\  \ / |__  |__)     |  |  | /  \    |  | | |\ | /__`    
|    |___ /~~\  |  |___ |  \     |  |/\| \__/    |/\| | | \| .__/                                                                         
""" + RESET

# Connect Four board dimensions
columns = 7
rows = 6
connect_four_board = [[0 for _ in range(columns)] for _ in range(rows)]

def clear_screen():
    """
    Clear the terminal screen.

    The implementation differs depending on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_gap(num):
    """
    Print empty lines for spacing.

    Parameters:
    num (int): Number of empty lines to print.
    """
    for _ in range(num):
        print()

def index_to_checker(board, row, column):
    """
    Convert board values into colored text representations.

    Parameters:
    board (list of list of int): The game board.
    row (int): Row index.
    column (int): Column index.

    Returns:
    str: Colored text representation of the board value at (row, column).
    """
    if board[row][column] == 0:
        return ' '
    elif board[row][column] == 1:
        return RED + 'X' + RESET
    elif board[row][column] == 2:
        return BLUE + 'O' + RESET

def print_board(board):
    """
    Print the current state of the board.

    Parameters:
    board (list of list of int): The game board.
    """
    for row in range(rows):
        for column in range(columns):
            x = index_to_checker(board, row, column)
            print(GREEN + " [ " + RESET + x + GREEN + " ] " + RESET, end='')
        print()
    print("   1      2      3      4      5      6      7\n")

def get_input():
    """
    Prompt the player for a column number.

    Returns:
    int: The column number selected by the player (0-indexed).
    """
    print("Choose the column number where you would like to place your checker (1-7):")
    while True:
        try:
            player_move = int(input("> "))
            if 1 <= player_move <= 7:
                return player_move - 1
            else:
                print("Move is out of bounds, please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input, please enter a number.")

def check_victory(board, player):
    """
    Check if the current player has won the game.

    Parameters:
    board (list of list of int): The game board.
    player (int): The player number (1 or 2).

    Returns:
    bool: True if the player has won, otherwise False.
    """
    def check_line(row, col, delta_row, delta_col):
        """
        Check if there is a line of 4 checkers for the current player.

        Parameters:
        row (int): Starting row index.
        col (int): Starting column index.
        delta_row (int): Row direction increment.
        delta_col (int): Column direction increment.

        Returns:
        bool: True if there is a line of 4 checkers, otherwise False.
        """
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
            if check_line(row, col, 0, 1) or check_line(row, col, 1, 0) or \
               check_line(row, col, 1, 1) or check_line(row, col, 1, -1):
                return True
    return False

def place_checker(player_move, player):
    """
    Place a checker in the selected column and check for victory.

    Parameters:
    player_move (int): The column index where the checker will be placed (0-indexed).
    player (int): The player number (1 or 2).

    Returns:
    bool: True if the player won the game with this move, otherwise False.
    """
    for i in range(rows - 1, -1, -1):  # Iterate from bottom to top
        if connect_four_board[i][player_move] == 0:
            connect_four_board[i][player_move] = player
            if check_victory(connect_four_board, player):
                clear_screen()
                if player == 1:
                    print(player_one_wins)
                elif player == 2:
                    print(player_two_wins)
                print_board(connect_four_board)
                return True
            return False
    print("Column full, try another column.")
    return False

def game_loop():
    """
    Main game loop.

    Alternates turns between players until a victory condition is met.
    """
    connect_four_victory = False
    player1 = True

    while not connect_four_victory:
        clear_screen()
        print_gap(35)
        print(connect_four_message)
        print_board(connect_four_board)
        player = 1 if player1 else 2
        player_input = get_input()
        if place_checker(player_input, player):
            connect_four_victory = True
        player1 = not player1

if __name__ == "__main__":
    game_loop()