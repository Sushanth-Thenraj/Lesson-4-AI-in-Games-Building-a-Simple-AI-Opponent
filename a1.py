import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    """Displays the current state of the board with colors."""
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    """Allows the player to choose their symbol (X or O)."""
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        player_symbol = 'X'
        ai_symbol = 'O'
    else:
        player_symbol = 'O'
        ai_symbol = 'X'
    return player_symbol, ai_symbol  # Explicitly return the symbols

def player_move(board, symbol):
    """Handles the player's move."""
    move = -1
    while True:
        try:
            move = int(input(f"{Fore.YELLOW}Enter a number between 1-9: {Style.RESET_ALL}"))
            if move in range(1, 10) and board[move-1].isdigit():
                break
            else:
                print(f"{Fore.RED}Invalid Move. Try again...{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Enter a valid number between 1-9: {Style.RESET_ALL}")
    board[move-1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    """Handles the AI's move."""
    # Check if AI can win in the next move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return

    # Check if the player can win in the next move and block them
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol  # Place AI's symbol to block the player
                return

    # Choose a random move
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    """Checks if a player has won."""
    win_condition = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    
    for cond in win_condition:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False    

def check_full(board):
    """Checks if the board is full."""
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    print("Welcome to AI Tic-Tac-Toe!")
    name = input(f"{Fore.GREEN} Enter your name: {Style.RESET_ALL}")
    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        player_symbol, ai_symbol = player_choice()
        turn = "Player"
        game_on = True

        while game_on:
            display_board(board)
            if turn == "Player":
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"{Fore.GREEN}Congratulations {name}! You win!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(f"{Fore.YELLOW}It's a draw!")
                        game_on = False
                    else:
                        turn = "AI"
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(f"{Fore.RED}AI wins! Better luck next time {name}!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(f"{Fore.YELLOW}It's a draw!")
                        game_on = False
                    else:
                        turn = "Player"
        play_again = input(f"{Fore.CYAN}Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"{Fore.MAGENTA}Thanks for playing, {name}!")
            break

if __name__ == "__main__":
    tic_tac_toe()