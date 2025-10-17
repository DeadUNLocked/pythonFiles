import random  # Used for making random moves for the bot

# Function to print the current state of the board
def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        # Join each row's items with vertical bars
        row = " | ".join(board[i*3:(i+1)*3])
        print(f"| {row} |")
        print("+---+---+---+")

# Function to check if a player has won the game
def check_win(board, player):
    # All possible winning combinations by index
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    # Return True if any win condition is met
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

# Function to check if the game is a draw (board full, no winner)
def check_draw(board):
    return all(space in ["X", "O"] for space in board)

# Function to return a list of currently available moves (indexes not occupied)
def get_valid_moves(board):
    return [i for i, spot in enumerate(board) if spot not in ["X", "O"]]

# Function to determine the bot's move based on difficulty level
def bot_move(board, difficulty):
    valid_moves = get_valid_moves(board)

    # Easy mode: make a random move
    if difficulty == "easy":
        return random.choice(valid_moves)

    # Normal mode: block the player from winning if possible, otherwise random
    if difficulty == "normal":
        for move in valid_moves:
            board_copy = board[:]           # Copy the board
            board_copy[move] = "X"          # Pretend the player moves there
            if check_win(board_copy, "X"):  # If player could win
                return move                 # Block that move
        return random.choice(valid_moves)

    # Hard mode: smarter AI strategy
    if difficulty == "hard":
        # 1. Try to win
        for move in valid_moves:
            board_copy = board[:]
            board_copy[move] = "O"
            if check_win(board_copy, "O"):
                return move
        # 2. Try to block player
        for move in valid_moves:
            board_copy = board[:]
            board_copy[move] = "X"
            if check_win(board_copy, "X"):
                return move
        # 3. Take the center if available
        if 4 in valid_moves:
            return 4
        # 4. Take a corner if available
        for move in [0, 2, 6, 8]:
            if move in valid_moves:
                return move
        # 5. Take a side if available
        for move in [1, 3, 5, 7]:
            if move in valid_moves:
                return move

    # Fallback: pick a random move
    return random.choice(valid_moves)

# Function to run one full round of the game
def play_game():
    # Initialize board with numbers 1-9 as strings
    board = [str(i) for i in range(1, 10)]
    print("\nYou are X, the bot is O.")
    print("Pick a number 1-9 to place your X on the board.\n")

    # Ask for difficulty and validate input
    while True:
        difficulty = input("Choose difficulty (easy / normal / hard): ").strip().lower()
        if difficulty in ["easy", "normal", "hard"]:
            break
        else:
            print("Invalid choice. Please enter easy, normal, or hard.\n")

    print(f"You selected '{difficulty}' mode!\n")
    print_board(board)  # Display initial board

    # Main game loop
    while True:
        valid_moves = get_valid_moves(board)

        # --- Player's Turn ---
        while True:
            try:
                player_move = int(input("Your move (1-9): ")) - 1
                if player_move in valid_moves:
                    board[player_move] = "X"
                    break
                else:
                    print("Invalid move. That spot is taken or out of range.")
            except ValueError:
                print("Please enter a number from 1 to 9.")

        print_board(board)

        # Check if player has won
        if check_win(board, "X"):
            print("You won!")
            break

        # Check for draw
        if check_draw(board):
            print("It's a draw!")
            break

        # --- Bot's Turn ---
        bot_choice = bot_move(board, difficulty)
        board[bot_choice] = "O"
        print(f"Bot moves to position {bot_choice + 1}:")
        print_board(board)

        # Check if bot has won
        if check_win(board, "O"):
            print("You lost!")
            break

        # Check for draw
        if check_draw(board):
            print("It's a draw!")
            break

# Main function to control replay loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        play_game()  # Play one round
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break  # Exit the loop and end the game

# Only run the game if this script is the main file executed
if __name__ == "__main__":
    main()
