import random  # Used for making random moves for the bot

# Function to print the current state of the board
def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(f"| {row} |")
        print("+---+---+---+")

# Function to check if a player has won the game
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

# Function to check if the game is a draw
def check_draw(board):
    return all(space in ["X", "O"] for space in board)

# Function to get list of valid (empty) positions
def get_valid_moves(board):
    return [i for i, spot in enumerate(board) if spot not in ["X", "O"]]

# Bot move logic: randomly decide whether to make a smart or random move
def bot_move(board):
    valid_moves = get_valid_moves(board)

    # 50% chance of being smart or random
    if random.random() < 0.5:
        # Smart move attempt
        # Try to win
        for move in valid_moves:
            board_copy = board[:]
            board_copy[move] = "O"
            if check_win(board_copy, "O"):
                return move
        # Try to block player
        for move in valid_moves:
            board_copy = board[:]
            board_copy[move] = "X"
            if check_win(board_copy, "X"):
                return move
        # Take center if free
        if 4 in valid_moves:
            return 4
        # Take corners
        for move in [0, 2, 6, 8]:
            if move in valid_moves:
                return move
        # Take sides
        for move in [1, 3, 5, 7]:
            if move in valid_moves:
                return move
    # Otherwise, pick a random move (the “dumb” move)
    return random.choice(valid_moves)

# One round of Tic-Tac-Toe
def play_game():
    board = [str(i) for i in range(1, 10)]
    print("\nYou are X, the bot is O.")
    print("Pick a number 1-9 to place your X on the board.\n")
    print_board(board)

    while True:
        valid_moves = get_valid_moves(board)

        # --- Player Move ---
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

        if check_win(board, "X"):
            print("You won!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # --- Bot Move ---
        bot_choice = bot_move(board)
        board[bot_choice] = "O"
        print(f"Bot moves to position {bot_choice + 1}:")
        print_board(board)

        if check_win(board, "O"):
            print("You lost!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Loop to allow playing again
def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break

# Run the program
if __name__ == "__main__":
    main()
