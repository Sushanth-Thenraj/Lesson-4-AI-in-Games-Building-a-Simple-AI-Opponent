import random
import time  # Import the time module
from colorama import init, Fore, Style
init(autoreset=True)

possible_moves = ['rock', 'paper', 'scissors']

def player_move():
    """Handles the player's move."""
    move = ""
    while True:
        try:
            move = input(f"{Fore.YELLOW}Enter either rock, paper, or scissors: {Style.RESET_ALL}").strip().lower()
            if move in possible_moves:
                print(f"{Fore.GREEN}You chose: {move}{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Invalid Move. Try again...{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Enter either rock, paper, or scissors: {Style.RESET_ALL}")
    return move

def ai_move():
    """Handles the AI's move."""
    ai_move = random.choice(possible_moves)
    print(f"{Fore.BLUE}AI is thinking...", end="", flush=True)
    short_delay() # Call the short delay function
    print(f"{Fore.CYAN} AI chose: {ai_move}{Style.RESET_ALL}")
    return ai_move

def check_win(player_move, ai_move):
    """Checks if the player or AI has won."""
    if player_move == ai_move:
        return f"{Fore.YELLOW}It's a tie!"
    elif (player_move == 'rock' and ai_move == 'scissors') or \
         (player_move == 'paper' and ai_move == 'rock') or \
         (player_move == 'scissors' and ai_move == 'paper'):
        return f"{Fore.GREEN}You win!"
    else:
        return f"{Fore.RED}AI wins!"
    
def short_delay():
    for _ in range(3):
        print(Fore.BLUE + ".", end="", flush=True)
        time.sleep(0.5)

def rps():
    """Main function to play Rock, Paper, Scissors."""
    print(Fore.CYAN + "Welcome to Rock, Paper, Scissors!" + Style.RESET_ALL)
    while True:
        player_symbol = player_move()
        ai_symbol = ai_move()
        result = check_win(player_symbol, ai_symbol)
        print(Fore.YELLOW + result + Style.RESET_ALL)
        play_again = input(Fore.GREEN + "Do you want to play again? (yes/no): " + Style.RESET_ALL).strip().lower()
        if play_again != 'yes':
            print(Fore.GREEN + "Thanks for playing!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    rps()   