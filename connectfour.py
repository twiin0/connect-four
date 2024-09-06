import os

# ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'  # Resets the text color to default

class ConnectFour:
    """
    A class to represent the Connect Four gamegit 
    """
    # Connect Four messages
    CONNECT_FOUR_MESSAGE = GREEN + """
    ______     ___     ____  _____   ____  _____   ________     ______   _________     ________     ___     _____  _____   _______     
    .' ___  |  .'   `.  |_   \|_   _| |_   \|_   _| |_   __  |  .' ___  | |  _   _  |   |_   __  |  .'   `.  |_   _||_   _| |_   __ \    
    / .'   \_| /  .-.  \   |   \ | |     |   \ | |     | |_ \_| / .'   \_| |_/ | | \_|     | |_ \_| /  .-.  \   | |    | |     | |__) |   
    | |        | |   | |   | |\ \| |     | |\ \| |     |  _| _  | |            | |         |  _|    | |   | |   | '    ' |     |  __ /    
    \ `.___.'\ \  `-'  /  _| |_\   |_   _| |_\   |_   _| |__/ | \ `.___.'\    _| |_       _| |_     \  `-'  /    \ \__/ /     _| |  \ \_  
    `.____ .'  `.___.'  |_____|\____| |_____|\____| |________|  `.____ .'   |_____|     |_____|     `.___.'      `.__.'     |____| |___| 
    """ + RESET

    PLAYER_ONE_WINS = RED + """
    __                 ___  __      __        ___                 __     
    |__) |     /\  \ / |__  |__)    /  \ |\ | |__     |  | | |\ | /__`    
    |    |___ /~~\  |  |___ |  \    \__/ | \| |___    |/\| | | \| .__/                                                                      
    """ + RESET

    PLAYER_TWO_WINS = BLUE + """
    __                 ___  __     ___       __                  __     
    |__) |     /\  \ / |__  |__)     |  |  | /  \    |  | | |\ | /__`    
    |    |___ /~~\  |  |___ |  \     |  |/\| \__/    |/\| | | \| .__/                                                                         
    """ + RESET

    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 1
        self.game_over = False

    def clear_screen(self):
        """
        Clear the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_gap(self, num):
        """
        Print empty lines for spacing.
        """
        print("\n" * num)

    def index_to_checker(self, row, column):
        """
        Convert board values into colored text representations.
        """
        if self.board[row][column] == 0:
            return ' '
        elif self.board[row][column] == 1:
            return RED + 'X' + RESET
        elif self.board[row][column] == 2:
            return BLUE + 'O' + RESET

    def print_board(self):
        """
        Print the current state of the board.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                checker = self.index_to_checker(row, column)
                print(f"{GREEN} [ {RESET}{checker}{GREEN} ] {RESET}", end='')
            print()
        print("   1      2      3      4      5      6      7\n")

    def get_input(self):
        """
        Prompt the player for a column number.
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

    def check_victory(self, player):
        """
        Check if the current player has won the game.
        """
        def check_line(row, col, delta_row, delta_col):
            """
            Check if there is a line of 4 checkers for the current player.
            """
            count = 0
            for _ in range(4):
                if 0 <= row < self.rows and 0 <= col < self.columns and self.board[row][col] == player:
                    count += 1
                    row += delta_row
                    col += delta_col
                else:
                    break
            return count == 4

        # Check horizontal, vertical, and diagonal directions
        for row in range(self.rows):
            for col in range(self.columns):
                if (check_line(row, col, 0, 1) or  # Horizontal
                    check_line(row, col, 1, 0) or  # Vertical
                    check_line(row, col, 1, 1) or  # Positive slope diagonal
                    check_line(row, col, 1, -1)): # Negative slope diagonal
                    return True
        return False

    def place_checker(self, column):
        """
        Place a checker in the selected column and check for victory.
        """
        for row in range(self.rows - 1, -1, -1):  # Iterate from bottom to top
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                if self.check_victory(self.current_player):
                    self.clear_screen()
                    self.print_board()
                    return True
                return False
        print("Column full, try another column.")
        return False

    def switch_player(self):
        """
        Switch the current player.
        """
        self.current_player = 2 if self.current_player == 1 else 1

    def play_game(self):
        """
        Main game loop.
        """
        while not self.game_over:
            self.clear_screen()
            print(self.CONNECT_FOUR_MESSAGE)
            self.print_gap(2)
            self.print_board()
            player_input = self.get_input()
            if self.place_checker(player_input):
                self.clear_screen()
                self.print_board()
                print(f"{self.PLAYER_ONE_WINS if self.current_player == 1 else self.PLAYER_TWO_WINS}Player {self.current_player} wins!{RESET}")
                self.game_over = True
            else:
                self.switch_player()

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()